import hashlib

# test data (integer)
data = [i for i in range(1, 1000000)]

checkstring : str

for value in data:
    checkstring = "Blockchain Daigakko" + str(value)
    sha256sha256 = hashlib.sha256(hashlib.sha256(checkstring.encode()).digest())
    decodedhash = hashlib.sha256(hashlib.sha256(checkstring.encode()).digest()).hexdigest()

#    print(str(value) + " : " + hashlib.sha256(hashlib.sha256(checkstring.encode()).digest()).hexdigest())
#    print(str(value) + " : " + str(sha256sha256))
#    print(str(value) + " : " + str(decodedhash) + " " + str(sha256sha256))

    if "0x00" in str(sha256sha256) or "00" in str(sha256sha256) :
        print(str(value) + " : " + str(decodedhash) + " " + str(sha256sha256))
