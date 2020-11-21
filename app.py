from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(host="remotemysql.com",user="Rliijh7Lll",password="MMnpw6UqWX",database="Rliijh7Lll")
cursor = conn.cursor()

@app.route("/")
def register():
    return render_template("register.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/add_user", methods=['POST','GET'])
def add_user():
    name = request.form.get('uname')
    password = request.form.get('upassword')
    
    cursor.execute("INSERT INTO users(name,password) VALUES('{}','{}')".format(name,password))
    conn.commit()
    return "User inserted"

if __name__ == "__main__":
    app.run(debug=True)
