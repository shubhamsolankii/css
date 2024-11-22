import hashlib

def hash(input_string):
    sha512 = hashlib.sha512()
    sha512.update(input_string.encode('utf-8'))
    return sha512.hexdigest()

