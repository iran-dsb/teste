from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class Home(View):
    def get(self, request):
        return render(request, 'home.html', {})