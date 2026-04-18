```
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/ping")
def ping():
    host = request.args.get("host")
    result = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return {"result": result.decode()}

if __name__ == "__main__":
    app.run(debug=True)
```


# Вопросы:

### Где здесь может быть уязвимость?
### Как её можно эксплуатировать?
### Какие последствия?
### Как исправить?
