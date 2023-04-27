問題１のドキュメントです。
## エンドポイントURL
https://fibonacci-b55h.onrender.com
## ソースコードの構成
fib.pyが指定したn番目のフィボナッチ数を返すREST APIで、test.pyがユニットテストです。renderを使って外部からリクエストを送信できるサーバ構築を行いました。
## REST API(fib.py)の概要
* Pythonのflaskを使用した。
* フィボナッチ数を求める際には動的計画法を用いた。
* 入力値が1以上の整数の時は、HTTPステータスコードの200とフィボナッチ数列の値をJSON形式で返すようにしている。
* 入力値が１以上の整数でない時は、JSON形式で、HTTPステータスコードの400とエラーメッセージの"Bad request"を返すようにしている。

## ユニットテスト(test.py)の概要
* Pythonのunittestを用いてユニットテストを行なった。
* 入力が空、負の整数、文字列、小数の時HTTPステータスコード400とエラーメッセージ"Bad request"がJSON形式で返ってくることを検証している。
* 入力が正の整数の時(入力が1,99の時)にHTTPステータスコード200と正しい値が返ってくることを検証している。



