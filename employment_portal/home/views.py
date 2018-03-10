from django.shortcuts import render
from django.views import generic

class IndexView(generic.ListView):
    template = 'index.html'

    def get_queryset(self):
        return "BITCHES"