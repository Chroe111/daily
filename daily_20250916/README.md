了解しました！
今日は **Go** を使ったシンプルなプログラムのお題を用意しました。

---

## お題: URL短縮サービスの簡易版

### 内容

* 入力された長いURLに対して、短いIDを生成して対応付けを保存するプログラムを書いてください。
* 短縮IDは連番やランダム文字列でもOKです。
* 短縮IDとURLの対応はメモリ上のmapで管理しましょう。
* ユーザーは以下の操作ができるようにします:

  1. `shorten <URL>`: 新しい短縮URLを生成して表示する
  2. `lookup <ID>`: 短縮IDから元のURLを取得する
  3. `list`: 登録済みの短縮URL一覧を表示する
  4. `exit`: プログラムを終了

### 例

```
> shorten https://example.com/very/long/path
短縮ID: 1

> shorten https://golang.org/
短縮ID: 2

> list
1 -> https://example.com/very/long/path
2 -> https://golang.org/

> lookup 1
https://example.com/very/long/path
```

---

これは30分〜1時間くらいでできると思います。
やってみますか？
