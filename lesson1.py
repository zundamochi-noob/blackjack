import random

def deal():
    card = random.randint(1,13)
    if card == 1:
        card = 11
    elif card > 10:
        card = 10
    return card

#deal カードを引く時の関数

def is_berst(hand):
    return sum(hand) > 21

#バーストの判定を追加する関数

def is_blackjack(hand):
    return sum(hand) == 21

#ブラックジャックの判定を追加する関数

#プレイヤーの処理

hand = []
hand.append(deal())
hand.append(deal())

if is_berst(hand):
    print("バースト" + str(sum(hand)))
elif is_blackjack(hand):
    print("ブラックジャック")
else:
    print("合計:" + str(sum(hand)))
    action = input("もう一枚引きますか？　(y/n): ")
    while action == "y":
        hand.append(deal())
        print("合計: " + str(sum(hand)))
        if is_berst(hand):
            print("バースト")
            break
        else:
            action = input("もう一枚引きますか？　(y/n): ")

#ディーラーの処理

dealer_hand = []
dealer_hand.append(deal())
dealer_hand.append(deal())

#勝敗判定

while sum(dealer_hand) < 17:
    dealer_hand.append(deal())
else:
    print("----勝敗は----")
    print("ディーラー：　" + str(sum(dealer_hand)) + "  プレイヤー：　" + str(sum(hand))) 
if sum(dealer_hand) >= sum(hand):
    print("ディーラーの勝利")
else:
    print("プレイヤーの勝利")