from django.shortcuts import render

def index(request):
    return render(request, 'cpns/home.html')

def contact(request):
    return render(request, 'cpns/contact.html', {'content' : ['Please email me','tomblok.id@gmail.com']})

def help(request):
    return render(request, 'cpns/htmlku.html', {'content' : ['Pusat Bantuan']})
