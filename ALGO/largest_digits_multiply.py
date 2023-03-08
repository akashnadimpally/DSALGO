import numpy as np

def multiply(num1, num2):
    # Convert the numbers to strings and get their lengths
    str1 = str(num1)
    str2 = str(num2)
    len1 = len(str1)
    len2 = len(str2)
    
    # Pad the shorter number with leading zeros if necessary
    if len1 < len2:
        str1 = '0' * (len2 - len1) + str1
        len1 = len2
    elif len2 < len1:
        str2 = '0' * (len1 - len2) + str2
        len2 = len1
    
    # Initialize the result list with zeros
    result = [0] * (len1 + len2)
    
    # Multiply the numbers digit by digit
    for i in range(len1-1, -1, -1):
        for j in range(len2-1, -1, -1):
            product = int(str1[i]) * int(str2[j])
            pos1 = i + j
            pos2 = i + j + 1
            sum = product + result[pos2]
            result[pos1] += sum // 10
            result[pos2] = sum % 10
    
    # Remove leading zeros from the result
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    
    # Convert the result list to a string and then to an integer
    return int(''.join(map(str, result)))


num1 = 15345224245023567236668445890000
num2 = 345242446446778445478222456557333

print(multiply(num1, num2))

result = np.polymul(num1, num2)
result = np.trim_zeros(result, 'f')

print(int(''.join(str(x) for x in result)))