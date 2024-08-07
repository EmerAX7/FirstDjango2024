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

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Плахута А.С.</i>
    """
    #text = f"{vars(request)}"
    return HttpResponse(text)

def about(request):
    text = ""
    for k,v in author.items():
        text += f"{k}: <b>{v}</b><br>"
    return HttpResponse(text)

def get_item(request, item_id):
    for i in items:            
        if i['id'] == item_id:
            r = f"""
            <b>Название:</b> {i['name']}
            <br>
            <b>Количество:</b> {i['quantity']}
            """
            return HttpResponse(r)
    return HttpResponseNotFound(f"Товар [{item_id}] не найден")

def item_null(request):
    return HttpResponse("Укажите идентификатор")
