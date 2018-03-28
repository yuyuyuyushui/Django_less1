from django.shortcuts import render

# Create your views here.

def register(request):
    # if request.method =='post':
    #     return 'success'

    return render(request,'index.html')