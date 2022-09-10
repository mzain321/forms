from django.urls import path
from . import views


urlpatterns = [

	path('',views.home),
	path('thank you page.html',views.thankyou),
	path('form2',views.home2),
	path('new',views.home3)



]
