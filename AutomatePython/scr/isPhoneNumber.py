def isPhoneNumber(text):
    if len(text) != 13:
        return False  # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # not an area code
    if text[3] != '-':
        return False  # does not have first hyphen
    for i in range(4, 8):
        if not text[i].isdecimal():
            return False  # does not have first 4 digits
    if text[8] != '-':
        return False  # does not have second hyphen
    for i in range(9, 13):
        if not text[i].isdecimal():
            return False  # does not have last 4 digits
    return True  # "text" is a phone number!

message = 'Call me at 415-5155-1011 tomorrow. 415-5155-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+13]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')