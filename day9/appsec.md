```
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/go")
def go():
    url = request.args.get("next")
    return redirect(url)

if __name__ == "__main__":
    app.run(debug=True)
```

# Вопросы:

### Где здесь может быть уязвимость?
### Как её можно эксплуатировать?
### Какие последствия?
### Как исправить?
