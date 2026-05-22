from fastapi import FastAPI
import sqlite3

app = FastAPI()

conn = sqlite3.connect("rank.db", check_same_thread=False) 
cur = conn.cursor()

cur.execute(
"""
CREATE TABLE IF NOT EXISTS ranking(
    name TEXT PRIMARY KEY, 
    level INTEGER
)
""")

conn.commit() 


@app.post("/save") 
def save(name: str, level: int):
    
    cur.execute(
    "SELECT level FROM ranking WHERE name=?",
    (name,)
    )
    row = cur.fetchone()
    if row is None:
        cur.execute(
        "INSERT INTO ranking (name, level) VALUES (?, ?)",
        (name, level)
        )
    elif level > row[0]:
        cur.execute(
        "UPDATE ranking SET level=? WHERE name=?",
        (level, name)
        )

    conn.commit()

    return {"success": "True"}


@app.get("/ranking")
def ranking():

    cur.execute("""
    SELECT * FROM ranking
    ORDER BY level DESC
    LIMIT 10
    """)

    data = cur.fetchall()

    return data

@app.post("/reset")
def reset():

    cur.execute("DELETE FROM ranking")

    conn.commit()

    return {"message": "ranking reset"}