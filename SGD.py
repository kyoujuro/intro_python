class SGD:
    def __init__(self, lr = 0.01):
        self.lr = lr

    def update(self, params, grads):
        for key in params.keys():
            params[key] -= self.lr * grads[key]

class Adam:
    def __init__(self, lr=0.001, rho1=0.9, rho2=0.999):
        self.lr = lr
        self.rho1 = rho1
        self.rho2 = rho2
        self.iter = 0
        self.m = None
        self.v = None
        self.epsilon = 1e-8

    def update(self, params, grads):
        if self.m is None:
            self.m, self.v = {}, {}
            for key, val in params.items():
                self.m[key] = np.zeros_like(val)
                self.v[key] = np.zeros_like(val)

        self.iter += 1

        for key in params.keys():
            self.m[key] = self.rho1*self.m[key] + (1-self.rho1)*grads[key]
            self.v[key] = self.rho2*self.v[key] + (1-self.rho2)*(grads[key]**2)
            m = self.m[key] / (1-self.rho1**self.iter)
            v = self.v[key] / (1-self.rho2**self.iter)

            params[key] -= self.lr * m / (np.sqrt(v) + self.epsilon)
            
