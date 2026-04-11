import requests
import sqlite3
from datetime import datetime





print(f"data fetched at {datetime.now()}")
conn= sqlite3.connect("media_bot.db")
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS trend_buffer(
               id INTEGER  PRIMARY KEY AUTOINCREMENT ,
               fetched_at TEXT ,
               analysis TEXT) """)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS scheduling_queue(
               
               id INTEGER  PRIMARY KEY AUTOINCREMENT ,
               platform TEXT ,
               content TEXT,
               scheduled_time TEXT,
               status TEXT
               )""")
      
def fetch_posts(topic):

 url=(f"https://www.reddit.com/r/{topic}/hot.json")
 response = requests.get(url, headers={"User-Agent":"my bot"})

 if response.status_code!= 200:
  print(f"failed to fetch posts for {topic} : status code {response.status_code}")  
  return
   
 data = response.json()

 posts = data["data"]["children"]
 my_list = []
 if not posts:
    print(f"No posts found for the subreddit {topic}")
 for post in posts:        
  print(f"⭐ Score: {post['data']['score']} | {post['data']['title']}") 
  my_list.append(post['data']['title'])
 return my_list

topics =["technology","pakistan","linux"]
all_titles=[]

for topic in topics:
 titles=fetch_posts(topic)
all_titles = all_titles + titles

prompt = f"Here are trending Reddit posts: {all_titles}. What are the top 3 themes?"
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }
)
print (response.json()["response"])




cursor.execute("""
    INSERT INTO trend_buffer (fetched_at, analysis)
    VALUES (?, ?)
""", (str(datetime.now()), response.json()["response"]))




cursor.execute("""
    INSERT INTO scheduling_queue (platform, content, scheduled_time, status)
    VALUES (?, ?, ?, ?)
""", ("linkedin", response.json()["response"], str(datetime.now()), "pending"))


conn.commit()
cursor.execute("SELECT * FROM trend_buffer")
rows = cursor.fetchall()
for row in rows:
    print(row)