# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.conf import settings
from .models import buy_energy
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from .smart_meter_data_with_datetime import smart_meter
from .forms import buyForm
from django.views.decorators.csrf import csrf_exempt





def buy_view(request):
    formb=buyForm(request.POST or None)
    print(formb.is_valid)
    if formb.is_valid():
        objb=formb.save(commit=False)
        objb.save()

        sellers = buy_energy.objects.all()
        context={
            'formb':formb, 
            'sellers':sellers,
                 }

        html_template = loader.get_template('home/buy_page.html')
        return HttpResponse(html_template.render(context,request))
    
    sellers = buy_energy.objects.all()
    for i in sellers:
        print(i.cus_name)
    context = { 'formb' : formb , 'sellers' : sellers } 

    html_template = loader.get_template('home/buy_page.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))   


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
