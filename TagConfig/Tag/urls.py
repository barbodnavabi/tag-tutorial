from .views import home_view,detail_view,tagged

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',home_view),
    path('article/<slug:slug>',detail_view,name='detail'),
    path('tagged/<slug:slug>',tagged,name='tagged')
]
