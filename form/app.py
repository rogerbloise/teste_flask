from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app=Flask(__name__)

@app.route("/")
@app.route("/index")

def index():
    con = sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from events")
    data=cur.fetchall()
    return render_template ("index.html", datas=data)

@app.route("/add_event", methods=["POST", "GET"])
def add_event():
    if request.method=="POST":
        usuario=request.form["usuario"]
        nome_evento=request.form["nome_evento"]
        local=request.form["local"]
        data=request.form["data"]
        con=sql.connect("form_db.db")
        cur=con.cursor()
        cur.execute("insert into events(USUARIO,NOME_EVENTO,LOCAL,DATA) values (?,?,?,?)", (usuario, nome_evento, local, data))
        con.commit()
        flash("Dados cadastrados", "success")
        return redirect(url_for("index"))
    return render_template("add_event.html")

@app.route("/edit_event/<string:id>", methods=["POST","GET"])
def edit_event(id):
    if request.method=="POST":
        usuario=request.form["usuario"]
        nome_evento=request.form["nome_evento"]
        local=request.form["local"]
        data=request.form["data"]
        con=sql.connect("form_db.db")
        cur=con.cursor()
        cur.execute("update events set USUARIO=?,NOME_EVENTO=?,LOCAL=?,DATA=? where ID=?", (usuario,nome_evento,local,data,id))
        con.commit()
        flash("Dados atualizados", "success")
        return redirect(url_for("index"))
    con=sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from events where ID =?", (id,))
    data=cur.fetchone()
    return render_template("edit_event.html", datas=data)

@app.route("/delete_event/<string:id>", methods=["GET"])
def delete_event(id):
    con=sql.connect("form_db.db")
    cur=con.cursor()
    cur.execute("delete from events where ID=?", (id,))
    con.commit()
    flash("Dados deletados", "warning")
    return redirect(url_for("index"))

if __name__=='__main__':
    app.secret_key="admin123"
    app.run(debug=True)






