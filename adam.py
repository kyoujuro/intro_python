class Adam:

    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.iter = 0
        self.m = None
        self.v = None
        
    def update(self, params, grads):
        if self.m is None:
            self.m, self.v = {}, {}
            for key, val in params.items():
                self.m[key] = np.zeros_like(val)
                self.v[key] = np.zeros_like(val)
    
        self.iter += 1
        for key in params.keys():
            #self.m[key] = self.beta1 * self.m[key] + (1 - np.power(self.beta1,self.iter))
            #self.v[key] = self.beta2 * self.v[key] + (1 - np.power(self.beta1,self.iter))
            self.m[key] = self.beta1 * self.m[key] + (1 - self.beta1) * grads[key]
            self.v[key] = self.beta2 * self.v[key] + (1 - self.beta2) * (grads[key] * grads[key])
            #self.v[key] = self.beta2 * self.v[key] + (1 - self.beta2) * (grads[key]**2)
            #m_unbias = (1 - self.beta1) * (grads[key] - self.m[key])
            #v_unbias = (1 - self.beta2) * (grads[key]**2 - self.v[key])
            m_unbias = self.m[key] / (1 - self.beta1 ** self.iter)
            v_unbias = self.v[key] / (1 - self.beta2 ** self.iter)
            params[key] -= self.lr * m_unbias / (np.sqrt(v_unbias) + 1e-7)
