from pymongo import MongoClient
import certifi
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from bson.json_util import dumps


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

SECRET_KEY = 'SPARTA'

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.2zjwb.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        user_info = db.users.find_one({"userid": payload["id"]})

        return render_template('index.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    userid_receive = request.form['userid_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one(
        {'userid': userid_receive, 'password': pw_hash})

    if result is not None:
        payload = {
                'id': userid_receive,
                'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24),  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    userid_receive = request.form['userid_give']
    password_receive = request.form['password_give']
    username_receive = request.form['username_give']
    password_hash = hashlib.sha256(
        password_receive.encode('utf-8')).hexdigest()
    doc = {
        "userid": userid_receive,                               # 아이디
        "password": password_hash,                              # 비밀번호
        "username": username_receive,                           # 이름
        "code": ""
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    userid_receive = request.form['userid_give']
    exists = bool(db.users.find_one({"userid": userid_receive}))
    return jsonify({'result': 'success', 'exists': exists})

@app.route("/schedule", methods=["POST"])
def schedule_post():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"userid": payload["id"]})
        stitle_receive = request.form['stitle_give']
        sdate_receive = request.form['sdate_give']
        edate_receive = request.form['edate_give']
        stime_receive = request.form['stime_give']
        etime_receive = request.form['etime_give']
        sdesc_receive = request.form['sdesc_give']

        schedule_list = list(db.schedule.find({}, {'_id': False}))
        count = len(schedule_list) + 1

        doc = {
            'userid': user_info['userid'],
            'stitle': stitle_receive,
            'sdate': sdate_receive,
            'edate': edate_receive,
            'stime': stime_receive,
            'etime': etime_receive,
            'sdesc': sdesc_receive,
            'snumber': count
        }
        db.schedule.insert_one(doc)
        return jsonify({'msg': '등록 완료!'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("/"))

@app.route("/get_events", methods=["GET"])
def get_events():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"userid": payload["id"]})
        res = list(db.schedule.find({'userid': user_info['userid']}))
        # print(res)
        if res is not None:
            return jsonify({'result': 'success', 'res': dumps(res)})
    # 찾지 못하면
        else:
            return jsonify({'result': 'fail'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("/"))

@app.route("/comment/save", methods=["POST"])
def memo_post():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"userid": payload["id"]})
        memo_receive = request.form['memo_give']
        memotime_receive = request.form['memotime_give']

        memo_list  = list(db.memo.find({}))
        count = len(memo_list) + 1

        doc = {
            'userid': user_info['userid'],
            'memonum': count,
            'memo': memo_receive,
            'memotime': memotime_receive
        }

        db.memo.insert_one(doc)
        return jsonify({'result': 'success'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("/"))

# @app.route("/comment/show", methods=["GET"])
# def memo_get():
#     memo_list = list(db.memo.find({}, {'_id': False}))
#     return jsonify({'memos': memo_list})

@app.route("/comment/show", methods=["GET"])
def memo_get():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"userid": payload["id"]})
        memo_list = list(db.memo.find({'userid': user_info['userid']}))
        print(memo_list)
        if memo_list is not None:
            return jsonify({'result': 'success', 'memos': dumps(memo_list)})
    # 찾지 못하면
        else:
            return jsonify({'result': 'fail'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("/"))

@app.route("/comment/delete", methods=["DELETE"])
def memo_delete():
    memonum_receive = request.form['memonum_give']
    db.memo.delete_many({'memonum': int(memonum_receive)})
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
