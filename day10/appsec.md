```
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/hello")
def hello():
    name = request.args.get("name", "")
    template = f"<h1>Hello {name}</h1>"
    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=True)
```


# Вопросы:

### Где здесь может быть уязвимость?
- тут XXS  
### Как её можно эксплуатировать?
- аргумент приходит  без какой либо обработки, можно внедрить любой код, в том числе и js, который потом отрисуется любому пользователю  
### Какие последствия?
- фишинг (угон кредов, токенов)  
- распространение вредоноса  
### Как исправить?
```python
template = f"<h1>Hello {{name}}</h1>"  
```
