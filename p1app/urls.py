from django.urls import path,include
from .views import index,second

urlpatterns = [
    path('second/',second, name="second"),

]
