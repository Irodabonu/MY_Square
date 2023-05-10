def check(h, w, j, k):
    if j == 0 and k == 0:
        return 1
    elif j == 0 and k == w - 1:
        return 1
    elif j == h -1 and k == 0:
        return 1
    elif j == h -1 and k == w -1:
        return 1
    return 0

def next(h, w, j, k):
    if j == 0:
        if k != 0 and k < w - 1:
            return 1
    elif j == h - 1:
        if k != 0 and k < w - 1:
            return 1
    return 0

def after(h, w, j, k):
    if j != 0 and j != h - 1:
        if k == 0 or k == w - 1:
            return 1
    return 0
    
def sq(w, h):
    j = 0
    c = 0
    print(h, w)
    while j < h:
        k = 0
        while k < w:
            c = check(h, w, j, k)
            if c == 1:
                print('o', end='')
            else :
                n_c = next(h, w, j, k)
                w_c = after(h, w, j, k)
                if n_c == 1:
                    print('-', end='')
                elif w_c == 1:
                    print(">", end='')
                else :
                    print(' ', end='')  
            k += 1
        j += 1
        print('')
        
    
w = int(input("Enter width of sq\n"))
h = int(input("Enter height of sq\n"))
sq(w, h)
