# 第6回 exercise

## submit

not prepared yet. see

<https://drive.google.com/drive/folders/1zrZf9lTxiPJdGJd5WxaLdv6LSPVW6h2b>

### common reference

- Mastering Bitcoin Open Edition in Japanese

    <https://www.bitcoinbook.info/translations/ja/book.pdf>

## 同期するまでのやりとり

`S:version, R:verack, R:version, S:verack,
{S:getblocks, R:inv, S:getdata, R:block}`

### reference

- Mastering Blockchain : Figure 4. ピア同士の最初のハンドシェイク ~

## SPVモードで自分のウォレットと関係ある取引だけ同期したい場合

`S:version,R:verack,R:version,S:getheaders,R:headers,S:filterload,{S:getblocks,R:inv,S:getdata,R:merkleblock,R:tx}`

- solution:

    "Bloom Filters and Inventory Updates"の節によると、SPVで使用されるBloom Filter送信時の順序性は以下の通り

    ```C
    S:filterload`
    この後に
    S:getdata,R:merkleblock,R:tx
    ```

### reference

- Mastering Blockchain

- filterload, filteradd, filterclear, merkleblock - Bitcoin wiki
    <https://en.bitcoin.it/wiki/Protocol_documentation#filterload.2C_filteradd.2C_filterclear.2C_merkleblock>
