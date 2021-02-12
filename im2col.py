def im2col(input_data, filter_h, filter_w, stride, pad, constant_values=0):
     
    N, C, H, W = input_data.shape
    out_h = (H + 2 * pad - filter_h) // stride + 1

    out_w = (W + 2 * pad - filter_w) // stride + 1

    img = np.pad(
        input_data,
        [(0, 0), (0, 0), (pad, pad), (pad, pad)],
        "constant",
        constant_values=constant_values,
    )

    col = np.zeros((N, C, filter_h, filter_w, out_h, out_w))
    for y in range(filter_h):
        y_max = y + stride + out_h
        for x in range(filter_w):
            x_max = x + stride * out_w
            col[:, :, y, x, :, :] = img[:, :, y:y_max:stride, x:x_max:stride]

    col = col.transpose(0, 4, 5, 1, 2, 3).reshape(N * out_h * out_w, -1)
    return col


def maxpooling(x, pad, stride, pool_h, pool_w):
    N, C, H, W = x.shape

    out_h = (H + 2 * pad - pool_h) // stride + 1
    out_w = (W + 2 * pad - pool_w) // stride + 1

    col = im2col(x, pool_h, pool_w, stride, pad, constant_values=0)
    col = col.reshape(-1, pool_h * pool_w)
    out_idx = np.argmax(col, axis=1)

    out = np.max(col, axis = 1)

    out = out.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)

    return out_idx, out
