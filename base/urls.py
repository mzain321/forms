from django.urls import path
from . import views


urlpatterns = [

	path('',views.homenew),
	path('thank you page.html',views.thankyou),
	path('tabeeb',views.tabeebform),
	path('login',views.login),
	path('new',views.home3),
	path('old',views.home)



]
