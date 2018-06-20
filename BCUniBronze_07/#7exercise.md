# 第7回 exercise

## submit

<https://xxxx>

## ①testnetとregtestの二つのモードの違いを述べよ

- Testnet

  -> coinに価値が生じたら、再起動

- Regtest

  - miningが最も簡単で、そもそもルールがない

  - 自動テストを容易にするもの

  - 自動的にプライベートブロックチェーンを新規に作成するところからテスト実行されるために利用

## ②Coreのウォレットにあるビットコインを手動で取引作成して、署名して、配信したい場合に使用するRPCコールを順番に述べよ

1. createrawtransaction

2. signrawtransaction

3. sendrawtransaction

## ③現行バージョンの初期値で「relayfee」はいくらになっているか述べよ (ヒント：ノードの情報を教えてくれるRPCはどれ)

## ④自分のCoreにあるアドレスで「Blockchain Daigakko」を署名してその結果(アドレスも含めて)を述べよ
