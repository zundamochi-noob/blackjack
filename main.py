from fastapi import FastAPI

from fastapi.responses import HTMLResponse

from blackjack import play_game,start_game,deal,deck,judge_result

app = FastAPI()

current_hand = []
current_dealer_hand = []

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/home", response_class=HTMLResponse)
def home():
    return """
<h1>Blackjack</h1>
<button onclick="location.href='/game'">ゲームスタート</button>
"""
@app.get("/game", response_class=HTMLResponse)
def game():
    global current_hand, current_dealer_hand
    current_hand, current_dealer_hand = start_game()
    return f"""
<h1>Blackjack</h1>
<p>ディーラー: {current_dealer_hand[0]} ▧</p>
<p>プレイヤー: {current_hand} 合計: {sum(current_hand)}</p>
<button onclick="location.href='/hit'">もう一枚</button>
<button onclick="location.href='/stand'">ストップ</button>
"""
@app.get("/hit", response_class=HTMLResponse)
def hit():
    global current_hand
    current_hand.append(deal(deck))
    return f"""
<h1>Blackjack</h1>
<p>ディーラー: {current_dealer_hand[0]} ▧</p>
<p>プレイヤー:{current_hand} 合計: {sum(current_hand)}</p>
<button onclick="location.href='/hit'">もう一枚</button>
<button onclick="location.href='/stand'">ストップ</button>
"""
@app.get("/stand", response_class=HTMLResponse)
def stand():
    global current_dealer_hand
    while sum(current_dealer_hand) < 17:
        current_dealer_hand.append(deal(deck))
    result = judge_result(current_hand, current_dealer_hand)
    return f"""
<h1>結果</h1>
<p>プレイヤー: {sum(current_hand)}</p>
<p>ディーラー: {sum(current_dealer_hand)}</p>
<p>{result}</p>
<button onclick="location.href='/game'">もう一度</button>
"""