from django.shortcuts import render
# Create your views here.
def mainpage(request):
    return render(request,'MainPage/mainpage.html')

def page1(request):
    return render(request,'MainPage/page1.html')

def page2(request):
    return render(request,'MainPage/page2.html')
