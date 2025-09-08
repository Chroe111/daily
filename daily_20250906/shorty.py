import json
import os
import re
import sys
from datetime import datetime as dt


DATA_FILE_PATH = "data.json"
data = {"next_id": 0, "items": []}


def init_data() -> None:
    global data

    try:
        if os.path.exists(DATA_FILE_PATH):
            with open(DATA_FILE_PATH) as f:
                data = json.load(f)
        assert data.keys() == {"next_id", "items"}
        assert isinstance(data["next_id"], int)
        assert isinstance(data["items"], list)

    except Exception:
        print("保存ファイルが破損しています。削除したうえでもう一度実行してください。")
        sys.exit(1)


def encode(n: int) -> str:
    chars = []
    r = 62
    while True:
        p = n % r
        if p < 10:
            char = str(p)
        elif p < 10 + 26:
            char = chr(p - 10 + ord("a"))
        else:
            char = chr(p - 10 - 26 + ord("A"))
        chars.insert(0, char)
        n = n // r

        if n == 0:
            break

    return "".join(chars)


def decode(s: str) -> int:
    if re.fullmatch("[0-9a-zA-Z]+", s) is None:
        raise ValueError
    
    sum = 0
    r = 62
    for i, char in enumerate(reversed(s)):
        if ord(char) >= ord("A"):
            n = 10 + 26 + ord(char) - ord("A")
        elif ord(char) >= ord("a"):
            n = 10 + ord(char) - ord("a")
        else:
            n = int(char)
        sum += n * (r ** i)
    return sum


def is_valid_url(url: str) -> bool:
    return url.startswith(("http://", "https://"))


def add(url: str) -> None:
    if not is_valid_url(url):
        print("無効なURLです。")
        return

    code = encode(data["next_id"])
    data["next_id"] += 1
    data["items"].append({
        "id": data["next_id"],
        "code": code,
        "url": url,
        "created_at": str(dt.now().replace(microsecond=0))
    })

    with open(DATA_FILE_PATH, mode="w") as f:
        json.dump(data, f)
    print(f"データを追加しました。コード: {code}")


def get(id: str) -> None:
    try:
        decoded_id = decode(id)
    except ValueError:
        print("無効なコードです。")
        return
    
    if decoded_id > len(data["items"]):
        print(f"コード: {id} は存在しません。")
    else:
        print(data["items"][decoded_id]["url"])


def show_all_data() -> None:
    for d in data["items"]:
        print(d["code"], d["url"], d["created_at"])


def main() -> None:
    init_data()

    if len(sys.argv) < 2:
        print("コマンドを指定してください。")
        print("使用例: python shorty.py [COMMAND] [ARGUMENT]")
        return
    
    if sys.argv[1] == "add":
        if len(sys.argv) < 3:
            print("URLを指定してください。")
            print("使用例: python shorty.py add <URL>")
            return
        add(sys.argv[2])
    elif sys.argv[1] == "get":
        if len(sys.argv) < 3:
            print("コードを指定してください。")
            print("使用例: python shorty.py get <CODE>")
            return
        get(sys.argv[2])
    elif sys.argv[1] == "list":
        show_all_data()
    else:
        print("無効なコマンドです。使用できるコマンド:")
        print("add   新規登録して短縮コードを出力")
        print("get   元のURLを出力")
        print("list  すべての登録を表示")


if __name__ == "__main__":
    main()
