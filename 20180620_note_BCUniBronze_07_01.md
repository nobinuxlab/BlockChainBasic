# Note of BCCC Bronze #7 on 20th June - ビットコイン・コア：元祖クライアント

## Mainnet/Testnet/Regnet

- Mainnet: for production

- Testnet

  -> coinに価値が生じたら、再起動

- Regtest

  - miningが最も簡単で、そもそもルールがない

  - 自動テストを容易にするもの

  - 自動的にプライベートブロックチェーンを新規に作成するところからテスト実行されるために利用

### reference of Testnet/Regnet

- Bitcoinを使ったアプリケーションのテスト環境

    <https://techmedia-think.hatenablog.com/entry/2015/05/10/123243>

- source code : chainparams.cppを見てみると良いよ～

## JSON RPC : 現在の主流

講師が注目するのはほかに

## health check : getblockchaininfo

以前はgetinfoでhealth check -> getblockchaininfoほか2に分割

## generate numblocks: 最近は使用されない

miningをbitcoin coreのものを使用されない、独自ツールを使用されるのが主流

## getmininginfo

- prioritisetransaction : メモリプールの取引の優先度を手動で上げ、優先的に自分が採掘しているブロックに入れる

  -> これもbitcoin coreを使用することはないが、ほとんどのソフトで同じ機能を実装されている

## createrawtransaction -> signrawtransaction ->

bitcoin coreの中で最も使用されるもの、signrawtransaction、sendrawtransactionとセットで使用される

bitcoin core以外の（wallet/soft）の秘密鍵に対しても使用できる

-> 他に実装しているものがなければ普通にRPCを実行して取引生成に利用可能

  - getrawtransaction で情報取得して解析、その上signrawtransaction で署名

  - signrawtransaction :　signrawtransactionではredeemScriptなどの検証など詳細な処理は行わない、各ノードですでに検証などされている前提

  - sendrawtransaction

    *ここで、allowhighfees = Trueで強制送信も可

## createmultisig

- 注意点は公開鍵 ["key",...] の順序

  bitcoin coreでは自動sortはあえてせずに制御可能だがほか一般のソフトでは固定順序にしているものが大半

## 重要！！: estimatesmartfee

- e.g. estimatesmartfee 3 CONSERVATIVE などとして試算した手数料で送信する、などという使用方法

  -> ただし、試算結果よりはるかに大きな手数料で他のノードが送信されると受諾されない、という手数料問題あり！！

- 手数料問題に対する対応方法のひとつ：RBFという機能を付けるかどうかのフラグあり

  しかし、P2P networkの中で許容するノードとそうでないノードの両方があり

## validateaddress : 各ソフトで個別に実装されているためbitcoin coreは使用されず

## verifymessage <-> signmessageでの署名結果を検証できる

- signmessage "bitcoinaddress" "message": 自分などのウォレットのアドレス（秘密鍵）でmessageを署名

- verifymessage "bitcoinaddress" "signature"  "message": ウォレットのアドレス（秘密鍵）、署名、messageが妥当かをチェック

## dumpprivkey (util for begginer)

bitcoin coreで伝播、受信するまで自分のアドレスが表示されない、つまり、まだ同期していないという状況に対して、便利なwallet softなどにインポートして確認する、といった用途が可能

## getbalance ( "account" minconf  includeWatchonly )

minconf = 10 など指定して、過去の特定時点におけるbitcoin金額などを確認可能

## getnewaddress

"address_type"について

- p2sh-segwit: 現在ほとんどのアカウントが使用

- Bech32アドレスフォーマット: 未対応のソフトも多くあり as of June 2018

## getreceivedbyaccount / getreceivedbyaddress

便利

アカウントごと、アドレスごとなどで取得可

## importprivkey "bitcoinprivkey" ( "label"  rescan )

rescan = false推奨、最後以外は。

外部、例えばブレッドウォレット(Breadwallet) からbitcoin coreへインポートする際に時間をかけないでインポートすることが難しい

※ブレッドウォレット(Breadwallet) の場合は、秘密鍵をインポートする際に外部APIを使用

bitcoin coreは外部APIに依存しないつくりにしているため、rescanの考慮が必要

## sendtoaddress : 現在送金で外部からも良く使用されるRPC

sendfrom、sendmany (複数あて先、*指定可)よりも容易に送金可で良く利用されているもの
