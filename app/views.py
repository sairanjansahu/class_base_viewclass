from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *

# Create your views here.
def fbv(request):
    return HttpResponse('this is function based view')

class cbv(View):
    def get(self,request):
        return HttpResponse('this is class based view')
    
# html page rendring using view class

def fbv_html(request):
    return render(request,'fbv_html.html')

class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')
    
#using class base view inserting form

def fbv_form(request):
    to=TopicForm()
    d={'to':to}
    if request.method=='POST':
        tod=TopicForm(request.POST)
        if tod.is_valid():
            tod.save()
            return HttpResponse('DATA insertion done succesfully')
    return render(request,'fbv_form.html',d)

class cbv_form(View):
    def get(self,request):
        to=TopicForm()
        d={'to':to}
        return render(request,'cbv_form.html',d)
    
    def post(self,request):
        tod=TopicForm(request.POST)
        if tod.is_valid():
            tod.save()
            return HttpResponse('data instertion done successfully')