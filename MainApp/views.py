from django.shortcuts import render
from django.http import *
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from MainApp.models import Item

# Create your views here.

author = {
    "Имя": "Алексей",
    "Отчество": "Сергеевич",
    "Фамилия": "Плахута",
    "телефон": "8-923-600-01-02",
    "email": "emerax7@gmail.com",
}

#items = [
#   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#  {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
#   {"id": 7, "name": "Картофель фри" ,"quantity":0},
#   {"id": 8, "name": "Кепка" ,"quantity":124},
#]

ret_item_str = """<p><a href="/items">К списку товаров</a></p>"""

def home(request):
    context = {
        "name": "Иванов Сидр Петрович",
        "email": "isp@mail.ru",
    }
    return render(request, "index.html", context)

def about(request):
    #text = """
    #<a href="/">Главная</a> / 
    #<a href="/about">Об авторе</a> / 
    #<a href="/items">Товары</a>
    #<h2>Об авторе</h2>
    #"""
    #for k,v in author.items():
    #    text += f"{k}: <b>{v}</b><br>"
    #return HttpResponse(text)
    #
    context = {
        "author": author,
    }
    return render(request, "about.html", context)


def get_item(request, item_id):
    context = {}
    try:
        it = Item.objects.get(id=item_id)
        context = model_to_dict(it)
    except ObjectDoesNotExist:
        context["id"] = -1 # товар не найден
    return render(request, "item.html", context)

def item_null(request):
    # Особый обработчик, когда не указан идентификатор
    return HttpResponseNotFound(f"""<p>Укажите идентификатор</p>{ret_item_str}""")

def get_items(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items.html", context)
