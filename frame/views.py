from django.shortcuts import render

# my stuff here
from django.http import HttpResponse
from django.template import loader

'\'строка\'' ' \' - экран '

def index(request):
    template = loader.get_template('resolution_frames/index.html')
    context = {
        'window_height': 50,
        'window_width': 100,
        'raws': [1, 2, 3, 4, 5, 6, 7, 8, 9],
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
    return HttpResponse(template.render(context))

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
            table[i].append(i*j)
    print(table)
    return table
values = making_table()

# Create your views here.