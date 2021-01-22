
# define:rec contains 4 item
# x1,y1,x2,y2
# define (x1,y1) is left_top
# define (x2,y2) is right_bottom
def overlap_area(rec1, rec2):
    r1w = abs(rec1[0] - rec1[2])
    r2w = abs(rec2[0] - rec2[2])
    w1 = sorted([rec1[0], rec1[2], rec2[0], rec2[2]])
    c1 = w1[3] - w1[0]


    r1h = abs(rec1[1] - rec1[3])
    r2h = abs(rec2[1] - rec2[3])
    h1 = sorted([rec1[1], rec1[3], rec2[1], rec2[3]])
    c2 = h1[3] - h1[0]
    if (r1w + r2w) <= c1 or (r1h + r2h) <= c2:
        return 0
    return abs(w1[1] - w1[2]) * abs(h1[1] - h1[2])


if __name__ == '__main__':
    rec1 = [1, 4, 3, 2]
    rec2 = [1, 4, 3, 2]
    rec1 = [1, 7, 10, 3]
    rec2 = [2, 6, 5, 0]
    rec1 = [-3, 0, 0, -3]
    rec2 = [2, 5, 4, 3]
    rec1 = [1, 5, 6, 2]
    rec2 = [4, 4, 7, 1]
    k = overlap_area(rec1, rec2)
    print(k)
