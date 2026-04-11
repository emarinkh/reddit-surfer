import sqlite3
from datetime import datetime
from flask import Flask, render_template
app = Flask(__name__)
print(app.template_folder)
@app.route("/")






def home():
    conn = sqlite3.connect("/home/samarine/Desktop/coding/media-bot/media_bot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trend_buffer")
    rows = cursor.fetchall()
    
    cursor.execute("SELECT *FROM scheduling_queue")
    scheduling_rows =cursor.fetchall()




    print(rows)
    formatted_rows = []
    for row in rows:
        dt = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S.%f")
        formatted_date = dt.strftime("%B %d, %Y %I:%M %p")
        formatted_rows.append((row[0], formatted_date, row[2]))
    conn.close()
    return render_template("index.html", rows=formatted_rows, scheduling_rows=scheduling_rows)



if __name__ == "__main__":
    app.run(debug=True)