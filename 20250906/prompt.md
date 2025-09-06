了解！明日のお題はこちら👇

# ミニURL短縮サービスを作ろう（CLI版）

## ゴール

コマンドラインから使えるシンプルなURL短縮ツールを実装します。
連番IDを Base62 でエンコードして短いコードを発行し、ファイルに保存・参照できるようにします。

## 要件

* コマンド構成（例）

  * `shorty add <url>` : 新規登録して短縮コードを出力
  * `shorty get <code>` : 元のURLを出力
  * `shorty list` : すべての登録を表示（code, url, 作成日時）
* データ保存：同ディレクトリの `data.json`（または `data.db` など簡易ファイル）
* ID採番：0,1,2,… の連番を採番し、**Base62** でコード化

  * アルファベットは `0-9a-zA-Z`（計62文字）
* バリデーション：`http://` or `https://` 始まりのみ受け付ける（簡易でOK）
* エラー処理：

  * 無効なURL、存在しないコード、壊れた保存ファイルなどはメッセージ表示
* 実装言語：Python / Java / JavaScript / Rust / Go / Ruby / PHP のいずれか

## 仕様詳細

* Base62

  * `encode(n: int) -> string`
  * `decode(s: string) -> int`
* 保存フォーマット（例：JSON）

  ```json
  {
    "next_id": 7,
    "items": [
      {"id":0,"code":"0","url":"https://example.com","created_at":"2025-09-05T10:12:33Z"},
      {"id":1,"code":"1","url":"https://openai.com","created_at":"2025-09-05T10:13:01Z"}
    ]
  }
  ```
* `add` の流れ

  1. `next_id` を取得 → Base62 で `code` 生成
  2. レコード追加 → `next_id` をインクリメント → 保存
  3. 生成した `code` を出力
* `get` の流れ

  * `code` をキーに検索（または `decode` でid→検索）し、URLを出力

## 使用例

```
$ shorty add https://example.com/very/long/path?x=1
-> Code: b9   (例)

$ shorty get b9
-> https://example.com/very/long/path?x=1

$ shorty list
-> b9  https://example.com/very/long/path?x=1  2025-09-05T10:12:33Z
-> ba  https://openai.com                        2025-09-05T10:13:01Z
```

## ヒント

* Base62は「割り算して余りを文字に置き換える」標準的な基数変換で実装できます。
* ファイルロックや排他は今回は不要（シングルプロセス想定）。
* 言語別の簡易CLI：

  * Python：`argparse`
  * Node.js：`process.argv`（or `commander`）
  * Go：`flag`
  * Rust：`clap`
  * Ruby：`OptionParser`
  * PHP：`$argv`

## テスト観点（5分でOK）

* `add` → `get` → 同じURLが返る
* 連続 `add` でコードがユニーク
* 無効URLでエラー
* 存在しない `code` で「見つかりません」

## 発展（時間が余ったら）

* カスタムエイリアス：`shorty add --alias run` → `get run`
* 有効期限（`expires_at`）と期限切れハンドリング
* 同一URLは同一コードを返す（正規化＋逆引きキャッシュ）
* 簡易Webサーバ（`/b/<code>` リダイレクト）

楽しんでどうぞ！実装で詰まったらエラーメッセージと一緒に聞いてください 🙌
