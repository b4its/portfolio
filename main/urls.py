from django.urls import path

from . import views


urlpatterns = [
    path('', views.indexe, name="indexes"),
    path('permainan/batu-gunting-kertas', views.stone, name="stone"),
]