def splitSquare(width, length):
    squares = []
    if length == width or length == 0 or width == 0:
        return squares

    while(width > 0):
        if width < length:
            width, length = _reverseSize(width, length)
        
        squares.append(length)
        width = width - length

    result = []
    previous = None
    for square in squares:
        if previous == square:
            continue
        else:
            previous = square        
            qty = squares.count(square)
            result.append(f'{qty} - {square}x{square}')
    
    return result

def _reverseSize(width, length):
    aux = width
    width = length
    length = aux
    return width, length

print(splitSquare(22, 6))