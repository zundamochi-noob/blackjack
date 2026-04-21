# 仮想環境を有効化
venv\Scripts\activate

# サーバーを起動
uvicorn main:app --reload

# ブラウザで開く
http://127.0.0.1:8000

# 仮想環境を作成
python -m venv venv

# FastAPIをインストール
python -m pip install fastapi uvicorn