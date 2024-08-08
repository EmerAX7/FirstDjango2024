from django.shortcuts import render
from django.http import *

# Create your views here.

author = {
    "Имя": "Алексей",
    "Отчество": "Сергеевич",
    "Фамилия": "Плахута",
    "телефон": "8-923-600-01-02",
    "email": "emerax7@gmail.com",
}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

ret_item_str = """<p><a href="/items">К списку товаров</a></p>"""

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Плахута А.С.</i>
    """
    #text = f"{vars(request)}"
    #return HttpResponse(text)
    #return render(request, "index.html")
    context = {
        "name": "Иванов Сидр Петрович",
        "email": "isp@mail.ru",
    }
    return render(request, "index.html", context)

def about(request):
    text = ""
    for k,v in author.items():
        text += f"{k}: <b>{v}</b><br>"
    return HttpResponse(text)

def get_item(request, item_id):
    for item in items:            
        if item['id'] == item_id:
            r = f"""
            <b>Название:</b> {item['name']}
            <br>
            <b>Количество:</b> {item['quantity']}
            {ret_item_str}
            """
            return HttpResponse(r)
    return HttpResponseNotFound(f"Товар [{item_id}] не найден{ret_item_str}")

def item_null(request):
    # Особый обработчик, когда не указан идентификатор
    return HttpResponseNotFound(f"""<p>Укажите идентификатор</p>{ret_item_str}""")

def get_items(request):
    text = "<h2>Список товаров:</h2><ol>"
    for item in items:
        text += f"""<li><a href="/item/{item['id']}">{item['name']}</li>"""
    text += "</ol>"
    return HttpResponse(text)
