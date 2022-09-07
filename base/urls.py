from django.urls import path
from . import views


urlpatterns = [

	path('',views.home),
	path('thank you page.html',views.thankyou)



]
