import random

ANSWER_MIN = 1
ANSWER_MAX = 100

TRY_COUNT = 10

answer = random.randint(ANSWER_MIN, ANSWER_MAX)

guesses = []

while True:
    guess = input(f"推測してください（残り {TRY_COUNT - len(guesses)} 回）: ")
    if not guess.isdigit():
        print("数字を入力してください。")
        continue
    
    guess_number = int(guess)
    if guess_number < ANSWER_MIN or guess_number > ANSWER_MAX:
        print(f"{ANSWER_MIN} から {ANSWER_MAX} の範囲で指定しましょう。")
        continue
    else:
        guesses.append(guess)
    
    if guess_number == answer:
        print(f"正解！(入力回数: {len(guesses)} 回)")
        break
    elif len(guesses) >= TRY_COUNT:
        print("ゲームオーバー！")
        break
    elif guess_number > answer:
        print(f"大きいです。（これまでの入力: {', '.join(guesses)}）\n")
    else:
        print(f"小さいです。（これまでの入力: {', '.join(guesses)}）\n")
    