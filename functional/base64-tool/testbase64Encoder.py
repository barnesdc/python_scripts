import base64Encoder

testString = ''
testString2 = '45766964696e74'
testString3 = ['45766964696e74', '10000000000002ae', '']


# baseString = base64Encoder.hexTobase64(testString)
# print(baseString)

baseString = base64Encoder.hexTobase64(testString2)
print('Hex: ', testString2)
print('Base64: ', baseString)

# baseStringArray = base64Encoder.hexTobase64(testString3)
# print('Hex: ', testString3)
# print('Base64: ', baseStringArray)
