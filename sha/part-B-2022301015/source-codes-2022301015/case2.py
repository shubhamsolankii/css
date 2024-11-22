import sha512
import polyalphabetic

# sender's side
M = input('Message: ')
K = input('Key: ')

H = sha512.hash(M)
print('Hash computed at sender side:\n', H)

eH = polyalphabetic.encrypt(H, K)

combined = f"{M}#,#{eH}"


# the message which is sent
print('\nMessage sent via unsecure medium')
print(combined)



# receiver's side
rM, reH = combined.split('#,#')

dH = polyalphabetic.decrypt(reH, K)
computeH = sha512.hash(rM)
print('\nHash computed at receiver side:\n', computeH)

print()
if dH == computeH:
    print('Hash matches')
    print('Message integrity verified')
else:
    print('Message has been tampered')