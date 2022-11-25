positions = [
        ((680, 466), (752, 498)), #post-it
        
 ]

def check_click(x,y):
    for i in positions:
        a = i[0]
        b = i[1]
        if (a[0] < x < b[0]) and (a[1] < y < b[1]):
            return positions.index(i)
        return False