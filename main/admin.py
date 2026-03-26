from django.contrib import admin
from .models import Talaba, Muallif, Kitob, Kutubxonachi, Record

class TalabaAdmin(admin.ModelAdmin):
    list_display = ('id','ism', 'guruh', 'kurs', 'kitob_soni')
class KutubxonachiAdmin(admin.ModelAdmin):
    list_filter = ('ish_vaqti',)
    search_fields = ('ism',)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ('id','ism', 'jins', 'tugilgan_sana', 'kitob_soni', 'tirik')
    list_display_links = ('id', 'ism')
    search_fields = ('ism',)
    list_filter = ('tirik',)
    list_editable = ('kitob_soni','tirik')
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'talaba', 'kitob', 'kutubxonachi', 'olingan_sana', 'qaytarish_sana')
    search_fields = ('talaba__ism', 'kitob__nom', 'kutubxonachi__ism')
admin.site.register(Talaba, TalabaAdmin)
admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Kitob)
admin.site.register(Kutubxonachi, KutubxonachiAdmin)
admin.site.register(Record, RecordAdmin)
