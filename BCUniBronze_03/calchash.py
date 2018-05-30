# exercise 3
# 「Blockchain Daigakko」という文字列の後に数字を文字列としてくっ付けて、
# ハッシュ値の頭に0x00バイトが1個あるまで数字を進めて下さい。その数値を教えて下さい。
# => 78
#
from hashlib import sha256

# test data (integer)
data = [i for i in range(1, 10000)]

checkstring: str


for value in data:
    checkstring = 'Blockchain Daigakko' + str(value)
    hexdigest = sha256(sha256(checkstring.encode()).digest()).digest()
    # convert to little endian
    lehexdigest = hexdigest[::-1].hex()

    if lehexdigest[0:2] == '00':
        print(str(value) + " : " + str(lehexdigest))
