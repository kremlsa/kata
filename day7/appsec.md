```
import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route("/import", methods=["POST"])
def import_data():
    data = request.files["file"].read()
    obj = pickle.loads(data)
    return {"status": "ok", "data": str(obj)}

if __name__ == "__main__":
    app.run(debug=True)

```


# Вопросы:

### Где здесь может быть уязвимость?  
obj = pickle.loads(data) десериализации данных из недоверенного источника  
### Как её можно эксплуатировать?  
впервые вижу такую штуку как pickle. если правильно понял, надо подготовить payload в расширении pkl, в котором защита любая команда. при обработке такого файла на сервере pickle увидит внутри __reduce__ с командой, например, return (os.system, ("cat /etc/passwd",)) - ответ этой команды вернутся пользователю return {"status": "ok", "data": str(obj)}  
### Какие последствия?  
RCE от имени пользователя, из под которго запущено приложение  
### Как исправить?  
не использовать picle? использовать json для десериализации данных из недоверенных источников
