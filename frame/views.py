import os

from django.core.mail import EmailMessage
# my stuff here
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Frame

'\'строка\'' ' \' - экран '


def index(request):
    template = loader.get_template('resolution_frames/index.html')
    windows = Frame.objects.all()
    for w in windows:
        os.sys.stderr.write('Window: %s' % w)
    context = {
        #  Разобраться, как передавать шв шаблон из vew
        #  объект окна и как там обращаться к его полям
        'window_height': windows[0].window_height,
        'window': windows[0],
        'wsizes': [70, 130],
        'window_width': 50,
        'something': 'something',
        'raws': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'values_keys': values,
        'values1': values[1],
        'values2': values[2],
        'values3': values[3],
        'values4': values[4],
        'values5': values[5],
        'values6': values[6],
        'values7': values[7],
        'values8': values[8],
        'values9': values[9],
    }
    # html = template.render(context)
    return render(request, 'resolution_frames/index.html', context)


def making_numbers():
    raws_and_cols = 9
    all_numbers = []
    for i in range(raws_and_cols):
        i += 1
        all_numbers.append(i)
    return all_numbers


def making_table():
    all_numbers = making_numbers()
    table = {}
    for i in all_numbers:
        table[i] = []
        table[i].append(i)
        for j in all_numbers:
            table[i].append(i * j)
    print(table)
    return table


values = making_table()


def add(request):
    newheight = None
    if request.method == 'POST':
        if 'newheight' in request.POST:
            newheight = request.POST['newheight']  # записываем значение в переменную без браузера
    elif request.method == 'GET':  # присваиваем значение в строке браузера/переменной
        newheight = request.GET['newheight']
    if newheight is not None:  # сохраняем в базу значение
        f = Frame(
            window_height=int(newheight)
        )
        f.save()
        email = EmailMessage('Hello', 'World', to=['vladeslaw@gmail.com'])
        email.send()
    return HttpResponse("<p>Получили и создали окно: %s<p>" % (
        request.GET['newheight']
    ))


def delete(request):
    delete_item = None
    if request.method == "POST":
        delete_item = request.POST['delete_item']
    elif request.method == 'GET':
        delete_item = request.GET['delete_item']
        Frame.objects.filter(id=delete_item).delete()
        # подключаемся к классу унаследовавшему команды джанго и базы данных
        return HttpResponse('<p>Значение удалено - %s<p>' % (
            request.GET['delete_item']))

# Create your views here.
