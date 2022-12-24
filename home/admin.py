from django.contrib import admin

# Register your models here.
from .models import BeritaModel, Profile, BeritaApiBaru, KategoriBerita

admin.site.register(BeritaModel)
admin.site.register(Profile)
admin.site.register(KategoriBerita)

class BeritaApiBaruAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'contentSnippet', 'isoDate', 'image', 'kategori']

admin.site.register(BeritaApiBaru, BeritaApiBaruAdmin)
