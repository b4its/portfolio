from django.urls import path
from . import views

urlpatterns = [
	path('utama', views.utama, name='utama'),
	path('', views.gpt, name='gpt'),

	
	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
	
]
