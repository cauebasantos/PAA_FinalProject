import math

def sum(num1,num2):
	tamNum1 = len(num1)
	tamNum2 = len(num2)
	minTam = min(tamNum1,tamNum2)
	maxTam = max(tamNum1,tamNum2)
	result = ''
	carryOne = 0
	for i in range(1,minTam+1):
		auxResult = str(int(num1[-i]) + int(num2[-i]) + carryOne)
		if len(auxResult) == 2:
			carryOne= int(auxResult[0])
			result = auxResult[1] + result
		else:
			result = auxResult + result
			carryOne = 0	

	larguerNum = num1 if(tamNum1 > tamNum2) else num2
	restDigits = len(larguerNum)-minTam
	larguerNum = larguerNum[:restDigits]

	if carryOne == 0:
		return larguerNum[:restDigits]+result		

	for i in range(1,restDigits+1):
		auxResult = str(int(larguerNum[-i]) + carryOne)
		if len(auxResult) == 2:
			carryOne= int(auxResult[0])
			result = auxResult[1] + result
		else:
			result = auxResult + result
			carryOne = 0


	return result if carryOne == 0 else '1'+result


def mult(n1, n2):
    """
    Multiplicação de dois bignumbers usando o algorítmo de karatsuba:
    https://courses.csail.mit.edu/6.006/spring11/exams/notes3-karatsuba
    
    Entradas:
    n1: número 1
    n2: número 2

    Saída:
    n3: um bignumber cujo valor é n1*n2
    """
    n1_len = len(str(n1))
    n2_len = len(str(n2))
    n1 = int(n1)
    n2 = int(n2)

    # caso base: somente um digito
    if n1_len <= 1 or n2_len <= 1:
        return n1*n2

    # get the m value, this is where we will split a and b
    m = int(math.ceil(max(n1_len, n2_len)/2))

    # get the high(n[:m]) and low(n[m:]) parts of n1 and n2
    h1 = n1 // 10**m
    l1 = n1 % 10**m
    h2 = n2 // 10**m
    l2 = n2 % 10**m

    # calculate the 3 karatsuba multiplications
    a = mult(h1, h2)
    d = mult(l1, l2)
    e = mult(h1+l1, h2+l2) - a - d

    return (a * 10**(m*2)) + (e * 10**m) + d

def div(n, d):
    """
    Divisão de dois bignumbers usando o seguinte algorítmo:
    http://justinparrtech.com/JustinParr-Tech/an-algorithm-for-arbitrary-precision-integer-division/

    Entradas:
    n: numerador
    d: denominador

    Saída:
    q, r: uma tupla que contém quociente, resto
    """
    m = len(d) - 1
    n = int(n)
    d = int(d)

    a = d - d%10**m
    q = n//a
    r = d + 1

    while abs(r) >= d:
        r = n - mult(q, d)
        qn = q + r//a
        q = (qn+q)//2

    r = n - mult(q, d)
    if r < 0:
        q = q - 1
        r = r+d
        
    return q, r

