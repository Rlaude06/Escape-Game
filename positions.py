positions = [
        ((440, 311), (485, 333)), #post-it
        ((1146, 640), (1240,720))
        
 ]

def check_click(x,y):
    result=False
    for i in positions:
        print(i)
        a = i[0]
        b = i[1]
        if (a[0] < x < b[0]) and (a[1] < y < b[1]):
            result = positions.index(i)
    return result