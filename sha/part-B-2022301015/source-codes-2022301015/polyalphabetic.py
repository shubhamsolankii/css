
def encrypt(msg, key):
    key = key.upper()
    key_len = len(key)
    key_int = [ord(x) - 65 for x in key]
    msg_len = len(msg)
    msg_int = [ord(x) - 65 for x in msg]
    cip = ""
    for i in range(msg_len):
        cip += chr(((msg_int[i] + key_int[i % key_len])) + 65)
    return cip


def decrypt(cip, key):
    key = key.upper()
    key_len = len(key)
    key_int = [ord(x) - 65 for x in key]
    cip_len = len(cip)
    cip_int = [ord(x) - 65 for x in cip]
    msg = ""
    for i in range(cip_len):
        msg += chr(((cip_int[i] - key_int[i % key_len])) + 65)
    return msg
