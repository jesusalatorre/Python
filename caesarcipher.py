#Caesar Cipher

def cipher(unencrypted, key):
	encrypted=''
	for letter in unencrypted:
		encrypted+=chr(ord(letter)+key)
	return encrypted

def decipher(encrypted, key):
	unencrypted=''
	for letter in encrypted:
		unencrypted+=chr(ord(letter)-key)
	return unencrypted

whatever=raw_input('Input:')
key=raw_input('key:')
key=int(key)
result=cipher(whatever,key)

print result

unencryption=decipher(result,key)
print unencryption

