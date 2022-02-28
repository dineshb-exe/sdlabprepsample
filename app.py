import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

db_local="details.db"

@app.route("/",methods=['GET','POST'])
def hello_world():
    if request.method == 'GET':
        return render_template("login1.html")
    else:
        login_details=(
            request.form['user-name'],
            request.form['pwd']
        )
        b=check(login_details)
        if b==False:
            return render_template("login_fail.html")
        else:
            return render_template("login_success.html")
def check(ld):
    un=ld[0]
    pwd=ld[1]
    conn=sqlite3.connect(db_local)
    c=conn.cursor()
    post = conn.execute('SELECT username,password FROM credentials WHERE username = ? and password = ?',(un,pwd)).fetchone()
    print(post)
    conn.close()
    if post:
        return True
    return False