import hashlib

print('input Data :')
_input_string = input()

print('Data D : ' + str(_input_string))

print('sha1(D) : ' + hashlib.sha1(
    str(_input_string).encode()).hexdigest())

print('sha256(D) : ' + hashlib.sha256(
    str(_input_string).encode()).hexdigest())

print('sha512(D) : ' + hashlib.sha512(
    str(_input_string).encode()).hexdigest())

print('sha256(sha256(D)) : ' + hashlib.sha256(
    hashlib.sha256(str(_input_string).encode()).digest()).hexdigest())

print('ripemd160(D) : ' + hashlib.new('ripemd160',
    str(_input_string).encode()).hexdigest())

print('ripemd160(sha256(D)): ' + hashlib.new('ripemd160',
    hashlib.sha256(str(_input_string).encode()).digest()).hexdigest())
