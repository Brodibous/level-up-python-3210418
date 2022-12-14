def find_factors(numb):
    factors = []
    count = 2
    while count <= numb:
        if numb % count == 0:
            factors.append(count)
            numb = numb // count
        else:
            count += 1
    return factors
