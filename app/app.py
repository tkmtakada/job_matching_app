from flask import Flask,render_template,request,session,redirect,url_for
from sqlalchemy import and_
from models.models import Student,Circle,Favorite,Message
from models.database import db_session, engine
from datetime import datetime
from app import key
from hashlib import sha256
from pdb import set_trace as db
from app.relavant_circle import relavant_sml1_dict, relavant_area_dict

app = Flask(__name__)
app.secret_key = key.SECRET_KEY
# app.config.from_object('models.config.Config')

# ========================
#    TOP:  opを表示するだけ
# ======================
@app.route("/")
@app.route("/top")
def top():
    name = request.args.get("name")
    if name == None: name = "Noneでした"
    return render_template("top.html", name=name)

# =======================
#       LOGIN
# =======================
# get request はただHTMLを表示するだけ
@app.route("/login_s")
def login_s():
    name = request.args.get("name")
    name = "TBF"
    status = request.args.get("status")
    return render_template("login_student.html", name=name,status=status)

@app.route("/login_student", methods=["post"])
def login_student():
    # DBと照会，合致したら/indexへ，そうでなければstatusに
    # 理由を入れて/login_s に戻す
    s_name = request.form["name"]
    user = Student.query.filter_by(s_name=s_name).first()
    if user:
        s_password = request.form["password"]
        s_hashed_password = sha256((s_name + s_password + key.SALT).encode("utf-8")).hexdigest()
        if user.s_hashed_password == s_hashed_password:
            session["s_name"] = s_name
            session["s_id"] = user.s_id
            return redirect(url_for("index_student"))
        else:
            return redirect(url_for("login_s",status="wrong_password"))
    else:
        return redirect(url_for("login_s",status="user_notfound"))


# get request はただHTMLを表示するだけ
@app.route("/login_c")
def login_c():
    c_name = request.args.get("name")
    c_name = "TBF"
    status = request.args.get("status")
    return render_template("login_circle.html", c_name=c_name,status=status)

@app.route("/login_circle", methods=["post"])
def login_circle():
    # DBと照会，合致したら/indexへ，そうでなければstatusに
    # 理由を入れて/login_s に戻す
    c_name = request.form["name"]
    cir = Circle.query.filter_by(c_name=c_name).first()
    if cir:
        password = request.form["password"]
        c_hashed_password = sha256((c_name + password + key.SALT).encode("utf-8")).hexdigest()
        if cir.c_hashed_password == c_hashed_password:
            session["c_name"] = c_name
            session["c_id"] = cir.c_id
            return redirect(url_for("index_circle"))
        else:
            return redirect(url_for("login_c",status="wrong_password"))
    else:
        return redirect(url_for("login_c",status="user_notfound"))
# ===================
#    REGISTER
# ===================

# 要求されたHTMLを表示するだけ
@app.route("/new_student")
def new_student():
    status = request.args.get("status")
    return render_template("new_student.html",status=status)  # 実際は使われてないけど

# データベースへの書き込みを行うpost リクエスト
@app.route("/register_student",methods=["post"])
def registar_student():
    # name = request.form["name"]
    # univ = request.form["univ"]
    # tag1 = request.form["tag1"]
    s_name = request.form["user_name"]
    s_email = request.form["user_email"]
    s_area = request.form["user_area"]
    s_univ = request.form["user_univ"]
    s_big_tag = request.form["user_big_tag"]
    s_mid_tag = request.form["user_mid_tag"]
    s_sml_tag_1 = request.form["user_sml_tag_1"]
    s_sml_tag_2 = request.form["user_sml_tag_2"]
    # return render_template("index_student.html",name=name)   # tmp set
    if True:  # ハッシュ化する
        user = Student.query.filter_by(s_name=s_name, s_email=s_email).first()  # name,emailが一致すれば同一ユーザと判定
        if user: # もし既に登録していた
            return redirect(url_for("new_student",status="exist_user"))
        else:
            s_password = request.form["user_password"]
            s_hashed_password = sha256((s_name + s_password + key.SALT).encode("utf-8")).hexdigest()
            user = Student(s_name, s_email, s_area, s_univ, s_big_tag, s_mid_tag, s_sml_tag_1, s_sml_tag_2, s_hashed_password)
            db_session.add(user)
            db_session.commit()
            user = Student.query.filter_by(s_name=s_name).first()
            session["s_name"] = s_name
            session["s_id"] = user.s_id
            return redirect(url_for("index_student"))
    else:
        content = Student(s_name, s_email, s_area, s_univ, s_big_tag, s_mid_tag, s_sml_tag_1, s_sml_tag_2, s_hashed_password)
        db_session.add(content)
        db_session.commit()
        return top()


@app.route("/new_circle")
def newcircle():
    status = request.args.get("status")
    return render_template("new_circle.html", status = status)

@app.route("/register_circle", methods=["post"])
def register_circle():
    # name = request.form["name"] # ただのstrオブジェクト
    # univ = request.form["univ"]
    # tag1 = request.form["tag1"]
    c_name = request.form["circle_name"]
    c_area = request.form["circle_area"]
    c_univ = request.form["circle_univ"]
    c_big_tag = request.form["circle_big_tag"]
    c_mid_tag = request.form["circle_mid_tag"]
    c_sml_tag_1 = request.form["circle_sml_tag_1"]
    c_sml_tag_2 = request.form["circle_sml_tag_2"]
    c_desc = request.form["circle_text"]
    c_image = request.form["circle_image"]
    # return redirect(url_for("index_student"))   # tmp set
    if True:
        cir = Circle.query.filter_by(c_name=c_name).first() # サークル名が一致すればリダイレクト
        if cir:
            return redirect(url_for("new_circle",status="exist_user"))
        else:
            c_password = request.form["circle_password"]
            c_hashed_password = sha256((c_name + c_password + key.SALT).encode("utf-8")).hexdigest()
            cir = Circle(c_name, c_area, c_univ, c_big_tag, c_mid_tag, c_sml_tag_1, c_sml_tag_2, c_desc, c_image, c_hashed_password)
            db_session.add(cir)
            db_session.commit()
            cir = Circle.query.filter_by(c_name=c_name).first()
            session["c_name"] = c_name
            session["c_id"] = cir.c_id
            return redirect(url_for("index_circle"))
    else:
        # db()
        # ---  My Code ---
        # conn = engine.connect()
        # ----------------
        content = Circle(c_name, c_area, c_univ, c_big_tag, c_mid_tag, c_sml_tag_1, c_sml_tag_2, c_desc, c_image, c_hashed_password)
        db_session.add(content)
        db_session.commit()

        # conn.execute(content.insert(), content)
        return top()




# =============================
#      INDEX
# =============================
import pandas as pd

@app.route("/index_student")
def index_student():

    user_name = session["s_name"]

    #ユーザテーブルから情報を取得する
    user = pd.read_sql_query(sql="SELECT * FROM t_student ;", con=engine)

    #可能性のあるサークルテーブルを持ってくる
    circle = pd.read_sql_query(sql="select * from t_student join t_circle on t_student.s_area =  t_circle.c_area where t_student.s_name = '{}';".format(user_name), con=engine)

    circle['score'] = 0   #スコアカラムを追加
    #各サークルに点数を付ける
    for num, i in enumerate(circle.iterrows()):
        # クラブの大学名がユーザーの大学名だったらスコアに100点足す
        if i[1].c_univ == i[1].s_univ:
            circle.loc[num, "score"] += 100

        if i[1].c_big_tag == i[1].s_big_tag:
            circle.loc[num, "score"] += 5

        if i[1].c_mid_tag == i[1].s_mid_tag:
            circle.loc[num, "score"] += 10

        if i[1].c_sml_tag_1 == i[1].s_sml_tag_1:
            circle.loc[num, "score"] += 20

        if i[1].c_sml_tag_2 == i[1].s_sml_tag_2:
            circle.loc[num, "score"] += 20

    #スコアが105以上のサークルを抽出
    matched_circle_beta = circle[circle['score'] >= 105]

    #スコアが高い順にソートする
    matched_circle = matched_circle_beta.sort_values('score', ascending=False)
    print(matched_circle)

    return render_template("index_student.html", matched_circle=matched_circle)

@app.route("/index_circle")
def index_circle():
    if "c_name" in session:
        return render_template("index_circle.html")
    else:
        return render_template("login_circle.html", status="logout")




# ============================
# 受信メッセージ表示
# ============================

@app.route("/message_list")
def message_list():
    s_id = session["s_id"]
    # message_list = Message.query.filter_by(s_id=s_id).first()
    # l=[]
    # for message in message_list:
    #     l.append(message.c_id)
    # l=list(set(l))
    # for l
    message_list = pd.read_sql_query(sql="SELECT distinct t_message.s_id, t_message.c_id, t_circle.c_name FROM t_message join t_circle on t_message.c_id = t_circle.c_id where t_message.s_id = '{}';".format(s_id), con=engine)
    return render_template("message_list.html", message_list=message_list)

@app.route("/message_list/<int:circle_id>")
def watch_message(circle_id):
    s_id = session["s_id"]
    s_name=session["s_name"]
    c_name=Circle.query.filter_by(c_id=circle_id).first().c_name
    message_list = pd.read_sql_query(sql="SELECT t_message.*, t_circle.c_name FROM t_message join t_circle on t_message.c_id = t_circle.c_id where t_message.s_id = '{}' and t_message.c_id = '{}';".format(s_id,circle_id), con=engine)
    return render_template("watch_message.html", message_list=message_list,s_name=s_name,c_name=c_name)

# ============================
# サークル詳細ページ表示
# ============================

@app.route("/circle/<int:circle_id>")
def circle_info(circle_id):
    # --- サークル詳細情報取得  -----
    current_circle = Circle.query.filter_by(c_id=circle_id).first()
    s_id = session["s_id"]
    c_id = circle_id
    fav = Favorite(s_id,c_id)
    exist = Favorite.query.filter_by(s_id=s_id,c_id=c_id).first()

    # ---関連サークル情報取得  ----
    # 関連タグを持ってくる
    relavant_sml_tags = relavant_sml1_dict[current_circle.c_sml_tag_1]
    # 一致するタグを持つサークルを抽出．やや複雑なWHEREくなのでfilter_byではなくfilterをつかう
    # エリアは一致していないといけない
    area_lst = relavant_area_dict[current_circle.c_area]
    relavant_circles = Circle.query.filter(and_(Circle.c_sml_tag_1.in_(relavant_sml_tags),
                                                Circle.c_area.in_(area_lst))).all()
    print(relavant_circles)
    # -------------------------
    if exist:
        return  render_template("circle_info.html",current_circle=current_circle,
                            relavant_circles=relavant_circles,check=1)
    else:
        return  render_template("circle_info.html",current_circle=current_circle,
                            relavant_circles=relavant_circles,check=0)


@app.route("/circle/<int:circle_id>/favorite")
def circle_favorite(circle_id):
    s_id = session["s_id"]
    c_id = circle_id
    fav = Favorite(s_id,c_id)
    current_circle = Circle.query.filter_by(c_id=c_id).first()
    exist = Favorite.query.filter_by(s_id=s_id,c_id=c_id).first()
    if exist:
        pass
    else:
        db_session.add(fav)
        db_session.commit()
        return render_template("favorited.html",c_id=c_id)

@app.route("/circle/<int:circle_id>/unfavorite")
def circle_unfavorite(circle_id):
    s_id = session["s_id"]
    c_id = circle_id
    fav = Favorite(s_id,c_id)
    exist = Favorite.query.filter_by(s_id=s_id,c_id=c_id).first()
    #print(exist,s_id)
    current_circle = Circle.query.filter_by(c_id=c_id).first()
    if exist:
        db_session.delete(exist)
        db_session.commit()
        #return render_template("circle_info.html", check=0)
        #return redirect(url_for("/circle/%s" % str(c_id)),current_circle=current_circle,check=0)
        return render_template("unfavorited.html",c_id=c_id)
    else:
        pass
        # db_session.add(fav)
        # db_session.commit()
        # return  render_template("circle_info.html", check=1)



# ===================
#    LOGOUT
# ===================
@app.route("/logout")
def logout():
    session.pop("name", None)
    return redirect(url_for("top",status="logout"))

if __name__ == "__main__":
    app.run(debug=True)
