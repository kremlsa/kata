```
from flask import Flask, request

app = Flask(__name__)

api_keys = {
    "alice": "key-alice-123",
    "bob": "key-bob-456"
}

@app.route("/key")
def get_key():
    username = request.args.get("user")
    return {"api_key": api_keys.get(username)}

if __name__ == "__main__":
    app.run(debug=True)
```


# Вопросы:

### Где здесь может быть уязвимость?
### Как её можно эксплуатировать?
### Какие последствия?
### Как исправить?
    
