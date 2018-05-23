#
# preparation : $ pip install base58
# see : https://github.com/keis/base58
#
# exercise :
# 2. 任意のデータ(D)をbase58checkでエンコーディングする。
# デコードも行って、チェックサムが一致していることも確認する。

import base58
import sys

def main(args):
    assert args
    
    _input_string = str(args[0])

    while len(str(_input_string).strip()) < 1 :
        print('input Data :')
        _input_string = input()

    show_verification_result(_input_string)

    
def show_verification_result(target_data):
    print('Data : ' + str(target_data))

    # task 2-1 : 任意のデータ(D)をbase58checkでエンコーディング
    encoded_string = base58.b58encode_check(str(target_data).encode())
    print('Base58Check : ', encoded_string)
    
    # task 2-2 : デコードも行って、チェックサムが一致していることも確認
    decode_result = base58.b58decode_check(encoded_string)
    print('Decode result : ', decode_result, " => same checksum")


if __name__ == '__main__':
    main(sys.argv[1:])
