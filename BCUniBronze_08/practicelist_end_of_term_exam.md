# Blockchain University end of term exam practice list

## #2 page 3~4 ハッシュ関数

- データはどのようにハッシュ関数によって変わるのか

  - ハッシュ値の長さは固定(20バイト、32バイトなど)

  - 不可逆: 逆算不可、唯一（衝突しない前提で）という特性を利用

- 弱いハッシュ関数：MD5、SHA1

- Bitcoinで使用：RIPE160、SHA-256

## #2 page 7 取引とブロック

取引ID：取引のsha256sha256ハッシュ - 表示されたときは、常にリトルエンディアン

ブロックIDとハッシュ値が逆になっている：little vs big endian

```json
ジェネシスブロックのハッシュ値：(big endian)
6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000
ジェネシスブロックのID：(little endian)
000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```

## #2 Page 8 Base58：example data

example data 2-> example data 3では末尾の「X」が「Y」に進んだだけといった特徴

- データ：「example data 2」 Base58：eJdMDAKCH14zqi4DMKX

- データ：「example data 3」 Base58：eJdMDAKCH14zqi4DMKY

## #2 Page 9 Base58Check の仕組み

Base58Checkエンコード：データのsha256sha256から頭4バイトを取って、データの後にくっ付けてbase58エンコード

-> Base58(data + hash(data)[:4])

## #2 Page 15~17 ECDSA

- ECDSAは暗号化ではない

- 秘密鍵から署名を作成 -> 公開鍵から署名の信憑性を検証(一般的な普通の公開鍵暗号の署名方式)

- ECDSAで使用している楕円曲線の方程式を記憶

    y^2 = x^3 + ax + b mod p

    M_1 + M_2 = M_3

## #2 Page 21 secp256k1

- secp256k1

## #2 

## #2 

## #2 

## #2 
