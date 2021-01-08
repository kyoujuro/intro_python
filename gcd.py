def gcd(x, y):
    x_list = []
    y_list = []
    
    cnt = 1
    while x > cnt :
        if x % cnt == 0:
            x_list.append(cnt)
        cnt += 1

    cnt = 1
    while y > cnt:
        if y % cnt == 0:
            y_list.append(cnt)
        cnt += 1

    cnt_x, cnt_y = 0, 0
    gcd_list = []
    for t_x in x_list:
        for  t_y in y_list:
            if t_x == t_y:
                gcd_list.append(t_y)

    return max(gcd_list)
