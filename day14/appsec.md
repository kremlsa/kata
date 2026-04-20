```
from flask import Flask, request

app = Flask(__name__)

comments = []

@app.route("/comment", methods=["POST"])
def comment():
    text = request.form.get("text")
    comments.append(text)
    return {"status": "ok"}

@app.route("/comments")
def get_comments():
    return "<br>".join(comments)

if __name__ == "__main__":
    app.run(debug=True)
```





# Вопросы:

### Где здесь может быть уязвимость?
### Как её можно эксплуатировать?
### Какие последствия?
### Как исправить?
    
