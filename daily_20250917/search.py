import os
import sys


def main():
    if len(sys.argv) < 2:
        print("検索キーワードを指定してください。")
        exit(1)
    keyword = sys.argv[1]
    content = len(sys.argv) == 3 and sys.argv[2] == "--content"

    for current_dir, _, files in os.walk(os.path.dirname(__file__)):
        for file in files:
            filepath = os.path.join(current_dir, file)
            if keyword in file:
                print(filepath)
            elif content:
                with open(filepath, encoding="utf-8", errors="ignore") as f:
                    if keyword in f.read():
                        print(filepath)

if __name__ == "__main__":
    main()
