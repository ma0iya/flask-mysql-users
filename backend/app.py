from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def index():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "password"),
        database=os.getenv("DB_NAME", "mydb")
    )
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    output = "Users from MySQL:<br>" + "<br>".join(f"- {user[0]}" for user in users)
    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0")