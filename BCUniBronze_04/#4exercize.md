# 第4回

## submit

    https://docs.google.com/forms/d/e/1FAIpQLSdXeEUA5dUmPXmj1d2NetzrRN4hCGGd2Sa6GqR6Nyw1IndWGA/viewform?usp=sf_link

## Q-A

### Q.それぞれのscriptPubkeyの解答となりうるscriptSigを解答。

- OP_ADD OP_7 OP_EQUAL

  `OP_1 OP_6 SIG_1`

  - variation (swap OK)

    - `OP_2 OP_5 SIG_1` / `OP_5 OP_2 SIG_1`

    - `OP_3 OP_4 SIG_1` / `OP_4 OP_3 SIG_1`

  - initial(input) : X Y -> X+Y=7

- OP_SUB OP_3 OP_EQUAL

  `OP_4 OP_1 SIG_1`

  - variation

    - `OP_5 OP_2 SIG_1`

    - `OP_6 OP_3 SIG_1`

    - `OP_7 OP_4 SIG_1`

  - initial(input) : X Y -> X-Y=3

- OP_SWAP OP_4 OP_EQUAL OP_SWAP OP_7 OP_EQUAL OP_BOOLAND

  `OP_4 OP_7 SIG_1`

  - solution :

    initial(input) : X Y

    \* scriptPubKey(output)の最初のオペランドOP_SWAPが2つの項目を扱うため

    [X Y] OP_SWAP -> [Y X]

    [Y X] OP_4 OP_EQUAL -> [Y (X=4)] -> X=4 result is True(1) -> [Y 1]

    [Y 1] OP_SWAP -> [1 Y]  \* あえて表現するならば [(X=4) Y]

    [1 Y] OP_7 OP_EQUAL -> [1 (Y=7)] -> Y=7 result is True(1) -> [1 1]

    [1 1] OP_BOOLAND -> True(1) x True(1) = True : OK

    /

- OP_3DUP OP_ADD OP_8 OP_EQUAL OP_SWAP OP_ROT OP_ADD OP_10 OP_EQUAL OP_2SWAP OP_ADD OP_4 OP_EQUAL OP_BOOLAND OP_BOOLAND

  `OP_3 OP_1 OP_7 SIG_1`

  - solution :

    initial(input) : X Y Z

    \* scriptPubKeyの最初のオペランドOP_3DUPが3つの項目を扱うため

    [X Y Z] OP_3DUP -> [X Y Z X Y Z]

    [X Y Z X Y Z] OP_ADD -> [X Y Z X Y+Z]

    [X Y Z X Y+Z] OP_8 OP_EQUAL -> [X Y Z X (Y+Z=8)]  \* result (Y+Z=8) is 1

    [X Y Z X 1] OP_SWAP -> [X Y Z 1 X]

    [X Y Z 1 X] OP_ROT -> [X Y 1 X Z]  \* OP_ROT: [... x1 x2 x3] to [... x2 x3 x1]

    [X Y 1 X Z] OP_ADD -> [X Y 1 X+Z]

    [X Y 1 X+Z] OP_10 OP_EQUAL -> [X Y 1 (X+Z=10)]  \* result (X+Z=10) is 1

    [X Y 1 1] OP_2SWAP -> [1 1 X Y]  \* OP_2SWAP: [... x1 x2 x3 x4] to [... x3 x4 x1 x2]

    [1 1 X Y] OP_ADD -> [1 1 X+Y]

    [1 1 X+Y] OP_4 OP_EQUAL -> [1 1  (X+Y=4)]  \* result (X+Y=4) is 1

    [1 1 1] OP_BOOLAND OP_BOOLAND .. -> 1 AND (1 AND 1) -> True

    X+Y=4, X+Z=10, Y+Z=8 -> X=3, Y=1, Z=7

/