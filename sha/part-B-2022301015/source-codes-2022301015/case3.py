import sha512

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

# Message sent
print("\nMessage sent")
print(combined)


# at receiver's side
rM, rH = combined.split('#,#')

computeH = sha512.hash(f"{rM},{K}")
print("\nHash computed at receiver's side")
print(computeH)
print()

if computeH == rH:
    print('Hash matches')
    print("Message received with integrity intact")
else:
    print("Message has been tampered with")
