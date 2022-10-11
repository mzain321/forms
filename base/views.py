from django.shortcuts import render

# Create your views here.


def home(request):
	return render(request,'base/home.html')

def thankyou(request):
	return render(request,'base/thank you page.html')

def tabeebform(request):
	return render(request,'base/tabeebform.html')


def home3(request):
	return render(request,'base/home3.html')

def homenew(request):
	return render(request,'base/homenew.html')
def login(request):
	return render(request,'base/signin.html')
