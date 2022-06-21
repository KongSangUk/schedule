from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://eachkwon:kug11029**@cluster0.hmug9qa.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('schedule.html')


@app.route("/schedule", methods=["POST"])
def schedule_post():
    stitle_receive = request.form['stitle_give']
    sdate_receive = request.form['sdate_give']
    edate_receive = request.form['edate_give']
    stime_receive = request.form['stime_give']
    etime_receive = request.form['etime_give']
    sdesc_receive = request.form['sdesc_give']

    schedule_list = list(db.schedule.find({}, {'_id': False}))
    count = len(schedule_list) + 1

    doc = {
        'stitle' : stitle_receive,
        'sdate' : sdate_receive,
        'edate' : edate_receive,
        'stime' : stime_receive,
        'etime' : etime_receive,
        'sdesc' : sdesc_receive,
        'snumber': count
    }

    db.schedule.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
