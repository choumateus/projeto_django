from django.shortcuts import render
from django.http import HttpResponse

#create views
def index (response):
    return HttpResponse("<h1>Mat Chou monster</h1>")

def v1(response):
    return HttpResponse(r'<h1 style="color:red;">NATH LINDA</h1>')