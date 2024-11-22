import sha512
import polyalphabetic

# sender's side
M = input('Message: ')
K = input('Key: ')

H = sha512.hash(M)

combined = f"{M}#,#{H}"
print("Combined payload M || H")
print(combined)

cipher = polyalphabetic.encrypt(combined, K)

# the message which is sent
print('\nMessage sent via unsecure medium')
print(cipher)


# receiver's side

D = polyalphabetic.decrypt(cipher, K)
print("\nDecrypted Message at receiver's side")
print(D)
rM, rH = D.split('#,#')

checkH = sha512.hash(rM)

if rH == checkH:
    print('Computed hash equals sent hash')
    print('Authentication successful and integrity maintained')
else:
    print("Computed hash does not equal to sent hash")
    print("Hence, message is from unreliable source or tampered with")
