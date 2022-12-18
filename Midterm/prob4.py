def solve(s):
    x1, x2, x3, x4 = 0, 0, 0, 0
    while s != 0:
        if s > x1:
            x1 = s // 25
            s = s  % 25
        if s > x2:
            x2 = s // 10
            s = s  % 10
        if s > x3:
            x3 = s // 5
            s = s  % 5
        if s < 5:
            x4 = s
            break
        
    # print(f"x1: {x1}")
    # print(f"x2: {x2}")
    # print(f"x3: {x3}")
    # print(f"x4: {x4}")
    return [x1, x2, x3, x4]
    
solve(2)