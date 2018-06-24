# 第7回 exercise

## submit

<https://docs.google.com/forms/d/e/1FAIpQLScAFLD5lGNhiFIZt8SvUJIFA-nVy2GKcMZLho0kx0_ZAFSYHQ/viewform>

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

- answer

`0.00001000`

<http://chainquery.com/>でgetnetworkinfoコマンドを実行

 ![result of getnetworkinfo (getnetworkinfo_25thJune2018.txt)](getnetworkinfo_25thJune2018.txt)

- solution : getnetworkinfoコマンドを使用、relayfee以外にも以下確認可能

  - Bitcoin Coreのバージョン ”version”:
  
  - 取引、トランザクションをこのノードが中継するときに支払う料金設定 ”relayfee”:

  - ノードの接続数 ”connections”:

  - 自ノードのアドレス ”localaddresses”:

## ④自分のCoreにあるアドレスで「Blockchain Daigakko」を署名してその結果(アドレスも含めて)を述べよ

- example answer

  - address

  ```c
  2N7ixyfRLcqDAjJSUx7qRAqqUQtM2qPPyyW
  ```

  - message signed

  ```c
  xxxxxxxxxxxxx
  ```

- solution

1. bitcoin core インストール

  - Windows: bitcoin-0.16.1-win32-setup.exe

  - reference :
  <https://bitcoin.org/en/developer-examples#testing-applications>

2. daemon 起動

- bitcoin.conf

```conf
testnet = 3
txindex = 1

server = 1

rpcuser=nobutanaka
rpcpassword=Password123
rpcport = 18332
```

windows の場合、%AppData%\Roaming\Bitcoin\bitcoin.conf に保存

$ bitcoind -testnet -daemon

* windows 10で実行時は以下のようにエラーとなるためdaemonオプション指定なしに
`Error: -daemon is not supported on this operating system`

```c
> bitcoind -testnet
```

3. コマンド実行

Windowsの場合には、別のコマンドプロンプトを起動して

```c
> bitcoin-cli -testnet getnetworkinfo
```

```c
> bitcoin-cli -testnet getnewaddress
2N7ixyfRLcqDAjJSUx7qRAqqUQtM2qPPyyW
```

```c
> bitcoin-cli -testnet signmessage "2N7ixyfRLcqDAjJSUx7qRAqqUQtM2qPPyyW" "Blockchain Daigakko"
```