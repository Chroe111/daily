import os
import re
import sys


FILENAME = "memos.txt"
memo: list[str] = []

def load(filename: str) -> None:
    global memo
    if os.path.exists(filename):
        with open(filename) as f:
            memo = f.readlines()


def write(filename: str) -> None:
    with open(filename, "w") as f:
        f.writelines(memo)


def get_id(content: str) -> int:
    return int(re.match(r"(\d+)\.", content).group(1))


def add(content: str) -> int:
    if len(memo) == 0:
        id = get_id(memo[-1]) + 1
    else:
        id = 1
    memo.append(f"{id}. {content}\n")
    return id


def print_all() -> None:
    for m in memo:
        print(m)


def delete(id: int) -> None:
    for i, m in enumerate(memo):
        if get_id(m) == id:
            del memo[i]
            return
    raise IndexError


def main():
    load(FILENAME)

    if len(sys.argv) < 2:
        print("コマンドを指定してください。")
        exit(1)
    elif sys.argv[1] == "add":
        if len(sys.argv) < 3:
            print("メモの内容を指定してください。")
            exit(1)
        memo_id = add(sys.argv[2])
        print(f"メモを追加しました。ID: {memo_id}")
    elif sys.argv[1]  == "list":
        print_all()
    elif sys.argv[1] == "delete":
        if len(sys.argv) < 3:
            print("削除するIDを指定してください。")
            exit(1)
        elif not sys.argv[2].isdigit():
            print("無効なIDです。")
            exit(1)
        else:
            try:
                delete(int(sys.argv[2]))
                print(f"メモ {sys.argv[2]} を削除しました。")
            except IndexError:
                print("存在しないIDです。")
                exit(1)
    else:
        print("無効なコマンドです。")
        exit(1)

    write(FILENAME)


if __name__ == "__main__":
    main()
