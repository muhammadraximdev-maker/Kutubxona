from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),

    path('talabalar/', talabalar_view, name='talabalar'),
    path('kitoblar/', kitoblar_view, name='kitoblar'),
    path('mualliflar/', mualliflar_view, name='mualliflar'),
    path('recordlar/', recordlar_view, name='recordlar'),
    path('kutubxonachilar/', kutubxonachilar_view, name='kutubxonachilar'),

    path('talaba/<int:pk>/', talaba_detail_view, name='talaba_detail'),
    path('kitob/<int:pk>/', kitob_detail_view, name='kitob_detail'),
    path('muallif/<int:pk>/', muallif_detail_view, name='muallif_detail'),
    path('kutubxonachi/<int:pk>/', kutubxonachi_detail_view, name='kutubxonachi_detail'),

    path('talaba-ochirish/<int:pk>/', talaba_delete_view, name='talaba_delete'),
    path('kitob-ochirish/<int:pk>/', kitob_delete_view, name='kitob_delete'),
    path('muallif-ochirish/<int:pk>/', muallif_delete_view, name='muallif_delete'),
    path('record-ochirish/<int:pk>/', record_delete_view, name='record_delete'),
    path('kutubxonachi-ochirish/<int:pk>/', kutubxonachi_delete_view, name='kutubxonachi_delete'),
]