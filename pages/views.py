from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from random import randint

from .models import Attack, Defence

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attack'] = randint(1,29)
        context['defence'] = randint(1,29)
        return context


class AttackPageView(DetailView):
    template_name = 'attack.html'
    model = Attack

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attack'] = randint(1,29)
        return context


class DefencePageView(DetailView):
    template_name = 'defence.html'
    model = Defence

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['defence'] = randint(1,29)
        return context


    
