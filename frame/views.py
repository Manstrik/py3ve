from django.shortcuts import render
from django.http import HttpResponse
'\'строка\'' ' \' - экран '

def index(request):
    return HttpResponse(
        '''<table border="1">
        <tr>
            <td width="100" height="50" colspain="2">Ячейка - 1
            </td>
            <td width="100" height="50" colspain="2"> Ячейка - 2
            </td>
        </tr>
        <tr>
            <td width="100" height="50"> Ячейка - 3
            </td>
            <td width="100" height="50"> Ячейка - 4
            </td>
        </tr>
    </table>
        ''')

# Create your views here.