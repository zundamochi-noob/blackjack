import random
import time

suits = ["♠", "♥", "♦", "♣"]
deck = []

for suit in suits:
    for num in range(1,14):
        deck.append((num,suit))
        
def is_blackjack(hand):
   return sum(hand) == 21

def is_bust(hand):
    return sum(hand) > 21

def deal(deck):
    card = deck.pop()
    num = card[0]
    if num > 10:
        return 10
    if num == 1:
        return 11
    else:
        return num

def convert_ace(hand):
    if 11 in hand:
        i = hand.index(11)
        hand[i] = 1

def judge(hand,dealer_hand):
    print("====勝敗結果====")
    
    p_bj = is_blackjack(hand)
    d_bj = is_blackjack(dealer_hand)
    p_b = is_bust(hand)
    d_b = is_bust(dealer_hand)

    if p_bj and d_bj:
         print("両者ブラックジャックです！引き分けです。")
    elif p_bj:
         print("プレイヤーのブラックジャック！プレイヤーの勝ちです。")
    elif d_bj:
         print("ディーラーのブラックジャック！ディーラーの勝ちです。")

    elif p_b and d_b:
         print("両者バースト！引き分けです。")
    elif p_b:
         print("プレイヤーがバースト！ディーラーの勝ち。") 
    elif d_b:
         print("ディーラーがバースト！プレイヤーの勝ち。")
    
    elif sum(hand) > sum(dealer_hand):
         print("プレイヤーの勝ちです。")
    elif sum(hand) < sum(dealer_hand):
         print("ディーラーの勝ちです。")
    else:
         print("引き分けです。")
    
    print("プレイヤー： " + str(sum(hand)) + "　ディーラー：　" + str(sum(dealer_hand)))

def start_game():

     random.shuffle(deck)
     hand = []
     dealer_hand = []

     hand.append(deal(deck))
     hand.append(deal(deck))
     dealer_hand.append(deal(deck))
     dealer_hand.append(deal(deck))

     return hand,dealer_hand

def judge_result(hand,dealer_hand):
    
    p_bj = is_blackjack(hand)
    d_bj = is_blackjack(dealer_hand)
    p_b = is_bust(hand)
    d_b = is_bust(dealer_hand)

    if p_bj and d_bj:
         return "両者ブラックジャックです！引き分けです。"
    elif p_bj:
         return "プレイヤーのブラックジャック！プレイヤーの勝ちです。"
    elif d_bj:
         return "ディーラーのブラックジャック！ディーラーの勝ちです。"

    elif p_b and d_b:
         return "両者バースト！引き分けです。"
    elif p_b:
         return "プレイヤーがバースト！ディーラーの勝ち。"
    elif d_b:
         return "ディーラーがバースト！プレイヤーの勝ち。"
    
    elif sum(hand) > sum(dealer_hand):
         return "プレイヤーの勝ちです。"
    elif sum(hand) < sum(dealer_hand):
         return "ディーラーの勝ちです。"
    else:
         return "引き分けです。"
    
    print("プレイヤー： " + str(sum(hand)) + "　ディーラー：　" + str(sum(dealer_hand)))

def play_game():
     random.shuffle(deck)
     hand = []
     dealer_hand = []

     hand.append(deal(deck))
     hand.append(deal(deck))

     dealer_hand.append(deal(deck))
     dealer_hand.append(deal(deck))

     if is_bust(hand):
          convert_ace(hand)
          print("aceをコンバートしました")
     if is_bust(dealer_hand):
          convert_ace(dealer_hand)

     print("ディーラー: " + str(dealer_hand[0]) + " ▧ ")
     print("プレイヤー : " + str(hand[0]) + " " + str(hand[1]) + " 合計: " + str(sum(hand)))     

     action = input("もう一枚引きますか(y/n):")
     while action == "y":
          hand.append(deal(deck))
          if is_bust(hand):
               convert_ace(hand)
               print("aceをコンバートしました")
          print("プレイヤー： " + str(sum(hand)))
          if is_bust(hand):
               print("プレイヤー： " + str(sum(hand)))
               time.sleep(1)
               judge(hand,dealer_hand)
               return(hand,dealer_hand)
               
          action = input("もう一枚引きますか(y/n):")

     else:
          while sum(dealer_hand) < 17:
               dealer_hand.append(deal(deck))
               print("ディーラーが引きました")
               if is_bust(dealer_hand):
                    convert_ace(dealer_hand)
                    
          time.sleep(1)
          judge(hand,dealer_hand)
          return(hand,dealer_hand)