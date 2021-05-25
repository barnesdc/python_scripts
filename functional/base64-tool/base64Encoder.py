import codecs


def hexTobase64(hexString):
    if hexString is None:
        return
    if isinstance(hexString, str) and hexString is hex:
        base64String = codecs.encode(codecs.decode(hexString, 'hex'), 'base64')
        return base64String.replace("\n", "")
    else:
        return 'Error with string'
    if hexString is list:
        base64StringArray = []
        for hexStr in hexString:
            print('hex: ', hexStr)
            if checkHex(hexStr):
                hexStr = codecs.encode(codecs.decode(
                    hexStr, 'hex'), 'base64').replace("\n", "")
                base64StringArray.append(hexStr)
            else:
                return 'Error with String'
        return(base64StringArray)


def checkHex(hexString):
    if hexString is not hex:
        print('error with string')
        return 1
    else:
        return 0
