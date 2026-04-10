```
from flask import Flask, request

app = Flask(name)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "admin123":
        return {"status": "ok"}
    return {"status": "fail"}, 401

if name == "main":
    app.run(debug=True)
```

# Вопросы:

### Где здесь может быть уязвимость?
### Как её можно эксплуатировать?
### Какие последствия?
### Как исправить?
