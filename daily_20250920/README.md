了解です！
今日はちょっとユーティリティ寄りの課題を用意しました。

---

## 本日のお題（JavaScript）

### 「ログファイルフィルターツール」

`access.log` のようなログファイルから、特定の日付やキーワードを含む行だけを抽出して表示するコマンドラインツールを作ってください。

### 仕様

* コマンドライン引数で以下を指定できるようにする:

  * `--date=YYYY-MM-DD` : 指定された日付を含む行のみ表示
  * `--keyword=文字列` : 指定されたキーワードを含む行のみ表示
* 両方指定された場合は AND 条件で抽出する。
* どちらも指定されなかった場合は全行を出力する。
* 対象ファイルは `access.log` とする。

### 入力例 (`access.log`)

```
2025-09-18 10:11:23 INFO User login: alice
2025-09-18 11:45:02 ERROR Failed login attempt
2025-09-19 09:01:10 INFO User login: bob
```

### 実行例

```bash
node filter.js --date=2025-09-18
```

出力:

```
2025-09-18 10:11:23 INFO User login: alice
2025-09-18 11:45:02 ERROR Failed login attempt
```

```bash
node filter.js --keyword=ERROR
```

出力:

```
2025-09-18 11:45:02 ERROR Failed login attempt
```

```bash
node filter.js --date=2025-09-18 --keyword=login
```

出力:

```
2025-09-18 10:11:23 INFO User login: alice
```

---

ファイル読み込みや文字列処理、引数解析の練習になる課題です。
どうでしょう？やってみますか？
