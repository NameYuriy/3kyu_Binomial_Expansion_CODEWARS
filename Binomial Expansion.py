def expand(expr):
    #__________________________
    def factorial(n):
        z = 1
        for x in range(1, n+1):
            z *=x
        return z 
    #__________________________    
    list_expr = expr.split('^')
    degree = int(list_expr[1])
    if degree == 0:
        return '1'
    poly = list_expr[0].replace('(', '').replace(')', '')
    for i in poly:
        if i.isalpha() == True:
            coeff_list = poly.split(i)
            var = i
    if coeff_list[0] == '' or coeff_list[0] == '-':
        coeff_list[0] = coeff_list[0] + '1'
    coeff_list = [int(i) for i in coeff_list]
    if coeff_list[1] == 0:
        return str(coeff_list[0]**degree) + var + '^' + str(degree)
    result = [coeff_list[0]**degree]
    for k in range(1, degree):
        binom = factorial(degree)/(factorial(k)*factorial(degree - k))
        result.append(int(binom * coeff_list[0]**(degree - k) * coeff_list[1]**k))
    result.append( int(coeff_list[1]**degree))
    for k in range(0, len(result)):
        if result[k] == -1 and k != len(result)-1:
            result[k] = '-'
        if result[k] == 1 and k == 0:
            result[k] = ''
        if str(result[k]).find('-') == -1 and k != 0:
            result[k] = '+' + str(result[k])
        if degree - k != 0 and degree - k != 1:
            result[k] = str(result[k]) + var + '^' + str(degree - k)
        if degree - k == 1:
             result[k] = str(result[k]) + var
        else:
            result[k] = str(result[k])
    result = ''.join(result)
    return result
