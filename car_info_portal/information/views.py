# import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from django.db.models import Q

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# class HeaderSearch(generic.FormView):
#     template_name = "base.html"
#     def get_api(request):
#         car = {}
#         # if 'carname' in request.POST:
#         #     carname = request.GET['carname']
#         url = 'https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getYears'
#         # response = requests.get(url)
#         car = response.json()
#         return render(request, 'index.html', {'car': car})



class IndexView(generic.TemplateView):
    template_name = "index.html"
