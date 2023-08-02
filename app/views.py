from django.shortcuts import render

# Create your views here.

def forloop(request):
    d={'name':'SWATI','name1':'Surya','hobiies':['reading novels','painting']}
    return render(request,'forloop.html',context=d)