from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def posts_list(request):
    n = ['Vitalii', 'Petro', 'Oleg', 'Katya']
    return render(request, 'blog/index.html', context={'names': n})

