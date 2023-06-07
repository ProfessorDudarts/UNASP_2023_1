def eco(string):
    size = len(string)
    j = 1
    has_eco = False
    result = []
    eco_1 = ''
    eco_2 = ''

    for i in range(size - 1, size // 2, -1):
        eco_1 = string[i:size]
        eco_2 = string[i - j:i]
        j += 1

        has_eco = eco_1 == eco_2
        
        if has_eco:
            break

    if has_eco:
        qty_eco = string.count(eco_1)
        index = string.index(eco_1)
        result.append(''.join([string[:index], eco_1]))
        
        for _ in range(qty_eco - 1):
            result.append(eco_1)
    else:
        result.append(string)

    return result

print(eco('Palmeirasrasras'))
