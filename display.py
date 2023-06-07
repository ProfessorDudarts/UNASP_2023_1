def display(string_numbers):
    line1 = ''
    line2 = ''
    line3 = ''

    for number in string_numbers:
        digit = None
        if number == '1':
            digit = one()
        elif number == '2':
            digit = two()
        elif number == '3':
            digit = three()
        elif number == '4':
            digit = four()
        elif number == '5':
            digit = five()
        elif number == '6':
            digit = six()
        elif number == '7':
            digit = seven()
        elif number == '8':
            digit = eigth()
        elif number == '9':
            digit = nine()
        elif number == '0':
            digit = zero()
        
        if digit:        
            line1 += digit[0]
            line2 += digit[1]
            line3 += digit[2]
    
    print(line1)
    print(line2)
    print(line3)

def zero():
    line1 = ' _ '
    line2 = '| |'
    line3 = '|_|'
    return (line1, line2, line3)
  
def one():
    line1 = '  '
    line2 = ' |'
    line3 = ' |'
    return (line1, line2, line3)

def two():
    line1 = ' _ '
    line2 = ' _|'
    line3 = '|_ '
    return (line1, line2, line3)

def three():
    line1 = ' _ '
    line2 = ' _|'
    line3 = ' _|'
    return (line1, line2, line3)

def four():
    line1 = '   '
    line2 = '|_|'
    line3 = '  |'
    return (line1, line2, line3)

def five():
    line1 = ' _ '
    line2 = '|_ '
    line3 = ' _|'
    return (line1, line2, line3)

def six():
    line1 = ' _ '
    line2 = '|_ '
    line3 = '|_|'
    return (line1, line2, line3)

def seven():
    line1 = ' _ '
    line2 = '  |'
    line3 = '  |'
    return (line1, line2, line3)

def eigth():
    line1 = ' _ '
    line2 = '|_|'
    line3 = '|_|'
    return (line1, line2, line3)

def nine():
    line1 = ' _ '
    line2 = '|_|'
    line3 = ' _|'
    return (line1, line2, line3)

display('01339661519')