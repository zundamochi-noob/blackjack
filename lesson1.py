import random

def deal():
    card = random.randint(1,13)
    if card == 1:
        card = 11
    elif card > 10:
        card = 10
    return card

hand = []
hand.append(deal())
hand.append(deal())

if sum(hand) >21:
    print("バースト" + str(sum(hand)))
elif sum(hand) == 21:
    print("ブラックジャック")
else:
    print("合計:" + str(sum(hand)))
    action = input("もう一枚引きますか？　(y/n): ")
    while action == "y":
        hand.append(deal())
        print("合計: " + str(sum(hand)))
        if sum(hand) >= 21:
            print("バースト")
            break
        else:
            action = input("もう一枚引きますか？　(y/n): ")
#ブラックジャック
#かぶりあり、1player、1,11選択なし