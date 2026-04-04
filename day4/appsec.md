```
from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/user")
def get_user():
    user_id = request.args.get("id")

    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    query = f"SELECT id, username, email FROM users WHERE id = {user_id}"
    cursor.execute(query)

    result = cursor.fetchone()
    conn.close()

    if result:
        return {"id": result[0], "username": result[1], "email": result[2]}
    return {"error": "User not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)
```

# Вопросы:

### Где здесь может быть уязвимость?
### Как её можно эксплуатировать?
### Какие последствия?
### Как исправить?
