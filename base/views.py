from django.shortcuts import render

# Create your views here.


def home(request):
	return render(request,'base/home.html')

def thankyou(request):
	return render(request,'base/thank you page.html')

def home2(request):
	return render(request,'base/home2.html')


def home3(request):
	return render(request,'base/home3.html')
