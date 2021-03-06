# How to exec test site to solve exercise

 scriptPubkeyの解答となりうるscriptSig

## preparation

- open link :

  <https://bip32jp.github.io/english/createp2sh.html>

- reference

  <https://en.bitcoin.it/wiki/Script>

## 例題：OP_3 SIG_1（True:入力誤りを意味するFalseではいけないため)

0100000001731a3ff159a85582e4ea69fdd507ca52e4c709cf68cc4f84a6da510fd5b7b2310000000072
53
48
3045022100fc74c734d314bff0ae288bdb30b25b890256ae10f22d11889be31373778377aa02204992c4cbc0c11fb225a29dab9299e81c2e7ea78e78fcca45e31a46d0889cc600012721022d4549c2f5aca5697dc232390770a99d6ee6ee139fda0fa0412e77a7bcd4b3eead55935887ffffffff012493b35f0000000017a91454080827c0212bce22f827d1728d8480975de9338700000000

## 第1問: 2MyDa63t2Jc7s6hnMTMdzQANmToqCFxT1gw, 37fN2Jwzh9cWtv9onE27nDPWFTd2UpH8Nw

```java
022d4549c2f5aca5697dc232390770a99d6ee6ee139fda0fa0412e77a7bcd4b3ee
OP_CHECKSIGVERIFY
OP_8
OP_SUB
OP_14
OP_ADD
OP_16
OP_EQUAL
```

solution :

{X}-8+14=16
-> {X} = OP_10 (数値10)

OP_10 SIG_1と入力

## 第2問

```java
OP_CHECKSIGVERIFY
OP_IF
OP_TRUE
OP_ELSE
OP_RETURN
OP_ENDIF
```

```basic
{X}
IF
  TRUE
ELSE
  RETURN
ENDIF
```

-> RETURN何も値が何もないではなく、TRUEを返してほしいため
OP_FALSE以外の何でも正解

 e.g. OP_TRUE, OP_1, OP_2, ...

## 第3問

```java
OP_CHECKSIGVERIFY
OP_3DUP OP_ADD
OP_12 OP_EQUAL
OP_SWAP OP_ROT
OP_ADD OP_9
OP_EQUAL OP_2SWAP
OP_ADD OP_7
OP_EQUAL OP_BOOLAND
OP_BOOLAND
```

OP_3DUP : 必要なOP_mは3つ -> x, y, zとする

solution :

-> 上記OPを紐解くと次が導かれる

```basic
x+y=12
x+z=9
y+z=7
```

answer :

x=7
y=5
z=2

(option) exercise: 問題4,5を提出
