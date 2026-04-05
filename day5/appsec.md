```
from flask import Flask, request, send_file
import os

app = Flask(__name__)

BASE_DIR = "./uploads"

@app.route("/download")
def download():
    filename = request.args.get("file")
    path = os.path.join(BASE_DIR, filename)

    if os.path.exists(path):
        return send_file(path)
    return {"error": "File not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)
```

# Вопросы:

### Где здесь может быть уязвимость?
### Как её можно эксплуатировать?
### Какие последствия?
### Как исправить?
