from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('search/', views.search, name='search'),
    path('manali/', views.manali, name='manali'),
    path('varanasi/', views.varanasi, name='varanasi'),
    path('explore/', views.explore, name='explore'),
    path('glossary/', views.glossary, name='glossary'),
    path('chat/', views.chat, name='chat'),
    path('index/', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
]
