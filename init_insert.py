
# ==============================
#   JUST EXECUTE THE CODE BELOW
#
# python3 init_insert.py
# ============================
# from pdb import set_trace as db
# Init .db files.
from models.database import init_db
init_db()

# Insert sample data.
from models.database import db_session
from models.models import Circle
# インスタンスの作成
# 引数を調整する
#           name     area      univ    big         mid     small-1     small-2    desc                     image(存在してないです)
cir_lst = [
Circle("circleA","東京都", "早稲田", "スポーツ系", "屋外", "サッカー",  "飲み",   "１和気藹々とやっています", "sample.png", "password"),
Circle("circleB","東京都", "早稲田", "スポーツ系", "屋内", "バスケ",    "飲み",   "２陽キャになれます",       "sample.png", "password"),
Circle("circleC","東京都", "早稲田", "スポーツ系", "屋内", "フットサル","真面目", "３一球入魂！！",           "sample.png", "password"),
Circle("circleD","東京都", "早稲田", "文化系",     "音楽", "軽音,"    "真面目", "４和気藹々とやっています", "sample.png", "password"),
Circle("circleE","東京都", "早稲田", "文化系",     "音楽", "吹奏楽",   "飲み",  "５和気藹々とやっています", "sample.png", "password"),
Circle("circleF","東京都", "早稲田", "文化系",     "屋内", "セパタクロー",   "飲み",  "５和気藹々とやっています", "sample.png", "password"),
Circle("circleG","東京都", "早稲田", "文化系",     "屋内", "室内競技サークル",   "飲み",  "５和気藹々とやっています", "sample.png", "password"),
Circle("circleH","東京都", "早稲田", "文化系",     "屋内", "カバディ",   "飲み",  "５和気藹々とやっています", "sample.png", "password"),
Circle("circleI","東京都", "早稲田", "文化系",     "屋内", "茶道",   "飲み",  "５和気藹々とやっています", "sample.png", "password"),
Circle("circleJ","東京都", "早稲田", "文化系",     "屋内", "学祭",   "飲み",  "５和気藹々とやっています", "sample.png", "password"),
Circle("circleK","東京都", "早稲田", "文化系",     "屋外", "ヨット",   "飲み",  "５和気藹々とやっています", "sample.png", "password"),
Circle("circleL","東京都", "早稲田", "文化系",     "屋外", "ダイビング",   "飲み",  "５和気藹々とやっています", "sample.png", "password"),
Circle("circleM","東京都", "慶應義塾","スポーツ系", "屋内", "バレーボール",    "飲み",   "６和気藹々とやっています", "sample.png", "password"),
Circle("circleN","東京都", "慶應義塾","スポーツ系", "屋外", "サッカー",  "飲み",   "７和気藹々とやっています", "sample.png", "password"),
Circle("circleO","沖縄県", "琉球", "文化系",    "屋内",   "バスケ",    "飲み",   "８和気藹々とやっています", "sample.png", "password"),
Circle("circleP","北海道", "明治", "スポーツ系", "屋内",   "バスケ",    "飲み",   "９和気藹々とやっています", "sample.png", "password"),
Circle("circleQ","神奈川県","横浜市立","スポーツ系","屋内","セパタクロー","真面目", "１０和気藹々とやっています", "sample.png", "password"),
]


# サークルデータ登録
# db_session.add(c1)
# db_session.add(c2)
# db_session.add(c3)
# db_session.add(c4)
# db_session.add(c5)
# db_session.add(c6)
# db_session.add(c7)
# db_session.add(c8)
# db_session.add(c9)
# db_session.add(c10)
for cir in cir_lst:
    db_session.add(cir)
# コミット
db_session.commit()
