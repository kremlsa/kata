```
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "1": {"id": "1", "name": "Alice", "role": "user"},
    "2": {"id": "2", "name": "Bob", "role": "admin"}
}

@app.route("/profile")
def profile():
    user_id = request.args.get("id")
    user = users.get(user_id)

    if not user:
        return {"error": "Not found"}, 404

    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)
```

# Вопросы:

### Где здесь может быть уязвимость?
### Как её можно эксплуатировать?
### Какие последствия?
### Как исправить?

1. тут IDOR и CWE-306  
2. в данном примере мы по указанию id получаем айди, имя и роль пользователя без авторизации
3. фактически - доступ от имени чужого пользователя. а там полет последствий в заивисимости от роли и ее привилегий  
4. если тут смотреть с точки зрения IDOR - можно просто пользователю не отдавать жсонку с информацией о пользователе. с точки зрения CWE-306 - добавить авторизацию  
