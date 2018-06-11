# 第5回exercise

## submit

https://docs.google.com/forms/d/e/1FAIpQLSeYjvZvmGye26S9CIFmjCMHbqQfsn4r9tvHfTwJEl7_pOW0JQ/viewform

## BIP39

- BIP39に適応したフレーズを教えて下さい。

see https://github.com/bitcoin/bips/tree/master/bip-0039

e.g. https://github.com/bitcoin/bips/blob/master/bip-0039/japanese.txt

例：
あかちゃん
ありがとう
..

  - BIP39 Mnemonic (example answer)

`おおや　たいほ　おんせん　ねぶそく　きゃく　じどう　いどう　ちわわ　りそく　はってん　まもる　きぶん　たいない　こんや　おどり`

  - seed c121952cde151857e1bd06154738ecae2faf63ed1be665698ad457100c78a5ea650fcd71b1985fe4430867ceeeaed1f2544344699c68b50a94296ac6bc72887e

- そのフレーズから生成したシードをBIP32に入れて、 m/44’/0’/0’/0/0 のアドレスを教えて下さい。

  `1BkQiFEsSLtuvBdu8N4vGau7dmqJPKGogY`

  -> see Mnemonic Code Converter

  <https://iancoleman.io/bip39/>

  - 上記はこの作成例

  Derivation Pathにおいて「BIP32」を選択し、BIP32 Derivation Pathに「m/44'/0'/0'/0」と入力するとDerived Addressesの中に以下Pathが表示される

  - Path: m/44'/0'/0'/0/0
  
  - Address: 1BkQiFEsSLtuvBdu8N4vGau7dmqJPKGogY

  - Public Key: 035a11612c4a9179b89d4005a2f6e359dabbb1e13bdb5f293a90f006e645887012
  
  - private key: KwE2zz4QcWPkJ6jhaK7rbJZGf5vNBDZWZGcvaq5EkiTEqDjgBttE


  -> 復習、m/44'/0'/0'はマスタ公開鍵

## BIP44

- BIP44のウォレットの3つ目のアカウントの25個目の非お釣りアドレスの派生の絶対パスを教えて下さい。

  `m/44’/0’/2’/0/24`

  -> see ビットコインウォレットのパスフレーズの互換性の話（簡単なHDウォレットの仕組み）
  
  <http://www.jpbitcoinblog.info/entry/20160522/1463905035>

- マルチシグウォレットにBIP44を使うと思い浮かぶ問題点を述べよ

  -> 複数のウォレット間で互換性が取られていないこと。
  理由は、単一署名向けのBIP44において、他人の公開鍵を確認してP2SHを作る方法が標準化されていないため。
  これに対して、BIP45で標準化が図られたが、2018年月現在、実際のところBIP45を採用したウォレットはなく、マルチシグウォレットには互いに互換性がない。


## Attack Vector (攻撃ベクトル) - コンピュータまたはシステムへの侵入に使用される方法または経路。

- BIP70のペイメントプロトコルを使わないサイトへの攻撃ベクトルを述べよ

e.g. 中間者攻撃のScenario

中間者攻撃のシナリオとして以下のようなケースが考えられる。

1. 本人がSNSでbitcoinアドレスを公開

2. 一方で、攻撃者がなりすましアカウントで偽のアドレスを公開

3. 送金ユーザは、公開されたアドレスが本人のものか区別がつかない。ハッシュ値を見ただけでは判別しにくいため

4. 3の結果、送金ユーザが誤って、攻撃者が公開した偽のアドレス宛に送金してしまう

/