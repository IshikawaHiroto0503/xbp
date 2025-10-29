# acchi_muite_hoi.py
# あっち向いてホイ

import random

def input_choice(prompt, choices):
    """choices に許可するキー（文字列）のリストを渡す。正しい入力が来るまで聞く。"""
    while True:
        s = input(prompt).strip()
        if s in choices:
            return s
        print("入力が不正です。もう一度入力してください。")

def rps_user_choice():
    print("\n--- じゃんけん ---")
    print("1: グー  2: チョキ  3: パー")
    c = input_choice("あなたの手を入力（1/2/3）: ", ["1","2","3"])
    return int(c)  # 1,2,3

def rps_computer_choice():
    return random.choice([1,2,3])

def rps_result(user, comp):
    # 1:グー 2:チョキ 3:パー
    if user == comp:
        return "draw"
    # 勝ちパターン：グー(1)はチョキ(2)に勝ち、チョキ(2)はパー(3)に勝ち、パー(3)はグー(1)に勝ち
    if (user == 1 and comp == 2) or (user == 2 and comp == 3) or (user == 3 and comp == 1):
        return "user"
    return "comp"

def direction_name(n):
    return {1:"上", 2:"下", 3:"左", 4:"右"}[n]

def acchi_user_choice():
    print("\n--- 向く方向を選んでください ---")
    print("1: 上  2: 下  3: 左  4: 右")
    c = input_choice("あなたの向く方向（1/2/3/4）: ", ["1","2","3","4"])
    return int(c)

def acchi_comp_choice():
    return random.choice([1,2,3,4])

def play_round():
    # 1) じゃんけんを行う（あいこは繰り返し）
    while True:
        u = rps_user_choice()
        c = rps_computer_choice()
        names = {1:"グー", 2:"チョキ", 3:"パー"}
        print(f"あなた: {names[u]}  コンピュータ: {names[c]}")
        res = rps_result(u, c)
        if res == "draw":
            print("あいこ！もう一回じゃんけんします。")
            continue
        elif res == "user":
            print("あなたがじゃんけんに勝ちました → 「指す側」になります。")
            attacker = "user"
        else:
            print("コンピュータがじゃんけんに勝ちました → コンピュータが「指す側」です。")
            attacker = "comp"
        break

    # 2) あっち向いてホイ
    print("\n--- あっち向いてホイ！ ---")
    if attacker == "user":
        user_dir = acchi_user_choice()
        comp_dir = acchi_comp_choice()
        print(f"あなたは {direction_name(user_dir)} を指しました。")
        print(f"コンピュータは {direction_name(comp_dir)} を向きました。")
        if user_dir == comp_dir:
            print("\n=== おめでとう！ あなたの勝ちです！ ===")
            return "user"
        else:
            print("\n一致しません。勝敗決定ならず。続けます。\n")
            return None
    else:
        # コンピュータが指す側
        comp_dir = acchi_comp_choice()
        user_dir = acchi_user_choice()
        print(f"コンピュータは {direction_name(comp_dir)} を指しました。")
        print(f"あなたは {direction_name(user_dir)} を向きました。")
        if comp_dir == user_dir:
            print("\n=== 残念！ コンピュータの勝ちです。 ===")
            return "comp"
        else:
            print("\n一致しません。勝敗決定ならず。続けます。\n")
            return None

def main():
    print("=== あっち向いてホイ （Python版） ===")
    print("ルール: まずじゃんけんで『指す側』を決め、指した方向と相手が向いた方向が同じなら指した側の勝ちです。\n")
    while True:
        result = play_round()
        if result == "user" or result == "comp":
            # 終了
            break
        # まだ勝者が決まっていない場合、もう一度最初から（じゃんけんから）繰り返す
        cont = input_choice("続けますか？ はい:y  いいえ:n : ", ["y","n"])
        if cont == "n":
            print("ゲームを終了します。")
            break
    print("プレイありがとうございました！")

if __name__ == "__main__":
    main()
