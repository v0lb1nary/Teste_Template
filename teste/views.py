from django.shortcuts import render

def home(request):
    """ Função para encaminhamento "Home" """
    return render(request, 'teste/home.html')