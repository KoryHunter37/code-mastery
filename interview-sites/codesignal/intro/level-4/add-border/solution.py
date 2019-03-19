# https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN

def addBorder(picture):
    width = len(picture[0])   
    border_picture = []
    
    star_border = '*' * (width + 2)
    border_picture.append(star_border)
    
    for row in picture:
        border_picture.append('*' + row + '*')
        
    border_picture.append(star_border)
    
    return border_picture
    