
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

print("Number 1 + Number 2")
number1 = input("Enter number 1: ")
number2 = input("Enter number 2: ")

print("Result: ", sum(number1,number2))
