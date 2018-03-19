from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse


class IndexView(generic.ListView):
    template_name = 'index.html'


    def get_queryset(self):
        return "BITCHES"

#def index(request):
    #return render(request, "index.html")

