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

    path('talabalar/<int:pk>/delete', talaba_delete_view, name='talaba_delete'),
    path('talabalar/<int:pk>/delete-confirm', talaba_delete_confirm_view),
    path('kitob/<int:pk>/delete', kitob_delete_view, name='kitob_delete'),
    path('kitoblar/<int:pk>/delete-confirm/', kitob_delete_confirm_view, name='kitob_delete_confirm'),
    path('muallif/<int:pk>/delete', muallif_delete_view, name='muallif_delete'),
    path('mualliflar/<int:pk>/delete-confirm/', muallif_delete_confirm_view, name='muallif_delete_confirm'),
    path('record/<int:pk>/delete', record_delete_view, name='record_delete'),
    path('kutubxonachi/<int:pk>/delete', kutubxonachi_delete_view, name='kutubxonachi_delete'),
]