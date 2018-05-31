# 第4回

## submit

    <https://docs.google.com/forms/d/e/1FAIpQLSdXeEUA5dUmPXmj1d2NetzrRN4hCGGd2Sa6GqR6Nyw1IndWGA/viewform?usp=sf_link>

## Q-A

### Q.それぞれのscriptPubkeyの解答となりうるscriptSigを解答。

- OP_ADD OP_7 OP_EQUAL

    OP_1 OP_6 SIG_1

  - variation (swap OK)

    - OP_2 OP_5 SIG_1 / OP_5 OP_2 SIG_1

    - OP_3 OP_4 SIG_1 / OP_4 OP_3 SIG_1

    - OP_0 OP_7 SIG_1 / OP_7 OP_0 SIG_1

- OP_SUB OP_3 OP_EQUAL

    OP_4 OP_1 SIG_1

  - variation

    - OP_5 OP_2 SIG_1

    - OP_6 OP_3 SIG_1

    - OP_7 OP_4 SIG_1

- OP_SWAP OP_4 OP_EQUAL OP_SWAP OP_7 OP_EQUAL OP_BOOLAND

    `OP_4 OP_7 SIG_1 ` ?

- OP_3DUP OP_ADD OP_8 OP_EQUAL OP_SWAP OP_ROT OP_ADD OP_10 OP_EQUAL OP_2SWAP OP_ADD OP_4 OP_EQUAL OP_BOOLAND OP_BOOLAND
