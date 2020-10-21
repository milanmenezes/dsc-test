from flask import Flask,render_template,abort,jsonify,request,redirect,url_for
import os
from model import db,save_db

app =Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html",
                           cards=db)

@app.route("/environ")
def environ():
    return "Hello "+os.environ.get("Name","Stranger")

@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card,index=index,max_index=len(db)-1)
    except IndexError:
        abort(404)

@app.route("/api/card/")
def api_card_list():
    return jsonify(db)

@app.route("/api/card/<int:index>")
def api_card_details(index):
    try:
        return db[index]
    except IndexError:
        abort(404)

@app.route('/add_card/', methods=["GET" , "POST"])
def add_card():
    if request.method == "POST":
        card = {"question" : request.form['question'],
              "answer" : request.form['answer']}
        db.append(card)
        save_db()
        return redirect(url_for('card_view', index=len(db)-1))
    else:
        return render_template("create_card.html")

if __name__ == '__main__':
   app.run()




