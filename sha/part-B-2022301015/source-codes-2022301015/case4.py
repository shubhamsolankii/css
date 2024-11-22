import sha512
import polyalphabetic

# at sender's side
M = input('Message: ')
K = input('Key: ')


MK = f"{M},{K}"
print("Concatenated Message and Key")
print(MK)


hMK = sha512.hash(MK)
print("\nHash computed at sender side")
print(hMK)

combined = f"{M}#,#{hMK}"

cipher = polyalphabetic.encrypt(combined, K)

# Message sent
print("\nMessage sent")
print(cipher)


# at receiver's side
decipher = polyalphabetic.decrypt(cipher, K)
rM, rH = decipher.split('#,#')

computeH = sha512.hash(f"{rM},{K}")
print("\nHash computed at receiver's side")
print(computeH)
print()

if computeH == rH:
    print('Hash matches')
    print("Message received with integrity intact")
    print('Confidentiality achieved')
else:
    print("Message has been tampered with")
