def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

if __name__ == '__main__':
    # print("415-555-4242 is a phone number:")
    # print(isPhoneNumber("415-555-4242"))
    # print("Moshi moshi is a phone number:")
    # print(isPhoneNumber("Moshi moshi"))

    msg = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
    for i in range(len(msg)):
        chuck = msg[i:i + 12]
        if isPhoneNumber(chuck):
            print(f"Phone number found: {chuck}")
    print("Done")