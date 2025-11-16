from hashlib import md5

# Example of a simple salted password hash(with MD5), the salt is appended at the end of the password.
# And a cracking class, that is used to try to break the salted hash inserted by the user.
# Author: github.com/GaMaDeCa
password_bytes=input('Input the password here: ').encode('utf-8')
salt=b'\x12\x34' # can use random bytes too> bytes([randint(0,255) for r in range(randint(2,100))])

md5_hash=md5()
md5_hash.update(password_bytes)
normal_hash=md5_hash.hexdigest()

print(f'\nNormal MD5 Hash: {normal_hash}')

md5_hash=md5()
md5_hash.update(password_bytes)
md5_hash.update(salt)
salted_hash=md5_hash.hexdigest()

print(f'Salted MD5 Hash: {salted_hash}')

# Crack a simple salted MD5 password hash:
#  - Each salt has it's own logic, the logic used here is to add the salt in the end of the password and hash it.
#  - There's some programmers who salt the hash modifying the own hashing algorithm using it's own logic(more xor, or a custom hash).
#  - This program is just a educational example.
class SaltBruteForce:
    def __init__(self,yourHash): # your hash, md5 or sha512, non initialized(the crack needs to reutilize the same hash)
        self.hashModule=yourHash
    def setSalt(self,salt:bytes): # the salt you just discovered, if it is a simple salt(added in the end of password)
        self.salt=salt            # if it's a complex salt modify the code into your needs(just copy the salting method in the crack function)
    def setHashedPassword(self,toCrack): # the password hashed with salt("unknown"), in hex
        self.hashedPass=toCrack.lower()
    def setBruteForceDictionary(self,dictionary): # insert a tuple or list of common used passwords, setBruteForceDictionary((admin,default,root,toor))
        self.dictionary=dictionary
    def crack(self): # return the password if it's in the dictionary else return None
        cracked=None
        for password in self.dictionary:
            hMod=self.hashModule()

            #hMod.update(self.salt) # if the salt is in the start of the password
            hMod.update(password.encode('utf-8'))
            hMod.update(self.salt)
            if self.hashedPass==hMod.hexdigest().lower():
                cracked=password
                break
        return cracked

sbf=SaltBruteForce(md5)
sbf.setSalt(salt)
sbf.setHashedPassword(salted_hash)
sbf.setBruteForceDictionary(
    (
        'admin',
        '1234',
        'qwerty',
        'default',
        'root',
        'toor',
        'pass',
        'password'
    )
)

discovered=sbf.crack()
if discovered!=None:
    print('\nSalted password hash cracked!\nPassword = '+discovered)
