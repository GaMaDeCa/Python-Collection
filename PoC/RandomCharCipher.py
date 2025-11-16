# Random Char Cipher

#Random Alphabet Generation Method
#from random import shuffle
#ralpha=list(alphabet)
#for i in range(99):
#	shuffle(ralpha)
#
#print("".join(alpha))
alphabet="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?:;+-*/\\\n\"=<>(){}[]~^'&#$@|"
alphabet_random="QN2V>#Wv]mc~kxLywKd6-JZG)}P<qDt8S0\"$fRT9i[M:C\nUHjs71l5aY|/z{O=.3\\F'(o;g*Eb!,Bu+n&pX@re^AI?4h"

import sys
out=sys.stdout.write
#Or
#global outCar
#outCar=""
#def out(car):
#	outCar+=car

def cipher(text):
	for car in text:
		i=alphabet.find(car)
		if i>-1:
			out(alphabet_random[i])
		else:
			out(car)

def decipher(text):
	for car in text:
		i=alphabet_random.find(car)
		if i>-1:
			out(alphabet[i])
		else:
			out(car)

#cipher("Ola Mundo")
#print("\n")
#decipher("7Jc jtGx)")

(cipher(input()) if input("Cipher(C) or Decipher(D): ").upper().startswith("C") else decipher(input()))