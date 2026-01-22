from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT entity_name, breach_type, country
        FROM breaches
    """)
    rows = cursor.fetchall()

    conn.close()
    return render_template("dashboard.html", rows=rows)

@app.route("/check_email", methods=["POST"])
def check_email():
    email = request.form["user_email"]

    # Simple simulation (like before)
    if email.endswith("@temp.com"):
        result = "⚠️ Email may be compromised"
    else:
        result = "✅ No breach found"

    return render_template("email_result.html", email=email, result=result)

if __name__ == "__main__":
    app.run(debug=True)
