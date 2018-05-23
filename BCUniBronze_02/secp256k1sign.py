#
# preparation : $ pip install ecdsa
# see : https://github.com/warner/python-ecdsa
#
# exercise :
# 3. ECDSAのsecp256k1曲線を用いて秘密鍵を生成し、そこから公開鍵を算出する。
# 4. 3番の秘密鍵を用いて任意のデータ(D)を署名し、公開鍵で署名を検証する

from ecdsa import SigningKey, SECP256k1

# task 3-1 : ECDSAのsecp256k1曲線を用いて秘密鍵を生成
private_key = SigningKey.generate(curve=SECP256k1)

print('private key : ' + str(private_key.to_string().hex()))

# task 3-2 : 公開鍵を算出
public_key = private_key.get_verifying_key()
print('public key : ' + str(public_key.to_string().hex()))

# task 4-1 : 3番の秘密鍵を用いて任意のデータ(D)を署名
signature = private_key.sign(b'sample payload') # D = 'sample payload'
# task 4-2 : 3番の秘密鍵を用いて任意のデータ(D)を署名
print('verification result : ' + str(public_key.verify(signature, b'sample payload')))
