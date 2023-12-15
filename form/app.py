from flask import Flask, request,  make_response, jsonify
import sqlite3 as sql

app=Flask(__name__)

@app.route("/events")
def events():
    con = sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from events")
    data=cur.fetchall()
    return make_response(jsonify([dict(ix) for ix in data]))

@app.route("/event/<string:id>", methods=["GET"])
def get_event(id):
    con = sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from events where id=?", (id))
    data=cur.fetchall()
    return make_response(jsonify([dict(ix) for ix in data]))

@app.route("/add_event", methods=["POST"])
def add_event():
    form = request.json
    usuario=form["usuario"]
    nome_evento=form["nome_evento"]
    local=form["local"]
    data=form["data"]
    con=sql.connect("form_db.db")
    cur=con.cursor()
    cur.execute("insert into events(USUARIO,NOME_EVENTO,LOCAL,DATA) values (?,?,?,?)", (usuario, nome_evento, local, data))
    con.commit()
    return make_response(jsonify(form))

@app.route("/edit_event/<string:id>", methods=["PATCH"])
def edit_event(id):
    form = request.json
    usuario=form["usuario"]
    nome_evento=form["nome_evento"]
    local=form["local"]
    data=form["data"]
    con=sql.connect("form_db.db")
    cur=con.cursor()
    cur.execute("update events set USUARIO=?,NOME_EVENTO=?,LOCAL=?,DATA=? where ID=?", (usuario,nome_evento,local,data,id))
    con.commit()
    con=sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from events where ID =?", (id,))
    new_data=cur.fetchall()
    return make_response(jsonify([dict(ix) for ix in new_data]))

@app.route("/delete_event/<string:id>", methods=["DELETE"])
def delete_event(id):
    con=sql.connect("form_db.db")
    cur=con.cursor()
    cur.execute("delete from events where ID=?", (id,))
    con.commit()
    return make_response('Data deleted')

if __name__=='__main__':
    app.secret_key="admin123"
    app.run(debug=True)






