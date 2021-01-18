from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Main

def Index(request):
    # busca e page
    '''busca = request.GET.get('search')
    page = request.GET.get('page')
    if busca:
        main = Main.objects.filter(nome__icontains=busca)
        paginator = Paginator(main, 3)
        main = paginator.get_page(page)
        
        
    else:
        main_list = Main.objects.all()
        paginator = Paginator(main_list, 3)


        main = paginator.get_page(page)'''
    
    return render(request, 'index.html',
    {'main':main}) 