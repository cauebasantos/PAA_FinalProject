import bn_operators as bn
import fast_rad_exp as re
import sequence_matrices_product as mp 

# Defining the Input BigNumbers
n1 = "9999999999999999999999999999999999"
n2 = "99999999999"

# Doing the Sum
res_sum = bn.sum(n1, n2)

# Doing the Multiplication
res_mult = bn.mult(n1, n2)

# Doing the Division
q, r = bn.div(n1, n2)

# Doing all the print
print('#####################################################')
print('BIG NUMBER CALCULATOR\n')
print('The numbers are:')
print('n1: ', n1)
print('n2: ', n2)
print()
print('Sum: ', res_sum)
print('Multiplication: ', res_mult)
print('Division:')
print('      Quotient: ', q)
print('      Remainder: ', r)
print('#####################################################\n')

# Define the Exponential and Radical numbers
n1 = 227
n2 = 4

# Doing the Exponential
res_exp = re.pow(n1, n2)

# Doing the Radical
res_rad = re.rad(n1, n2)

# Doing all the print
print('#####################################################')
print('EXPONENTIAL AND RADICAL\n')
print('The numbers are:')
print('n1: ', n1)
print('n2: ', n2)
print()
print('Exponential: ', res_exp)
print('Radical: ', res_rad)
print('#####################################################\n')

# Defining the Matrices
n = 5 # Number of matrices
m = [] # Array to store the size of the matrices
matrices = [] # The actual matrices

# Create the First Matrix
m.append([2, 3]) 
matrices.append([])
matrices[0].append([6, 3, 3])
matrices[0].append([4, 3, 9])

# Create the Second Matrix
m.append([3, 1])
matrices.append([])
matrices[1].append([1])
matrices[1].append([8])
matrices[1].append([3])

# Create the Third Matrix
m.append([1, 3])
matrices.append([])
matrices[2].append([2, 2, 8])

# Create the Fourth Matrix
m.append([3, 1])
matrices.append([])
matrices[3].append([9])
matrices[3].append([6])
matrices[3].append([8])

# Create the Fifth Matrix
m.append([1, 7])
matrices.append([])
matrices[4].append([5, 2, 5, 2, 1, 6, 7])

# Create the memo
memo = [ [0] * n for i in range(n) ]

# Doing all the print
print('#####################################################')
print('SEQUENCE MATRICES PRODUCT\n')
print('Input matrices: \n')
for matrix in matrices:
    mp.printMatrix(matrix)
    print()
print("The cost is:", mp.bestForm(m, memo, 0,len(m))) # Calculate the cost of the best form of multiplication
print()
print("The final result is:")
mp.printMatrix(mp.multiplyMatrices(matrices, memo, 0, len(m))) # Calculate the actual multiplication
print('#####################################################')