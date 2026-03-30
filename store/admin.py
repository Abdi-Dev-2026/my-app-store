# store/admin.py
from django.contrib import admin
from .models import Product, DownloadRequest, UserPoints, Favorite, SiteSettings

# Product admin oo labadaba sawir local iyo link URL ka muuqda
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')  # Waxyaabaha lagu soo bandhigo liiska
    fields = ('name', 'description', 'price', 'category', 'image', 'image_url', 'download_link')  # Labadaba field
    search_fields = ('name', 'description')  # Raadinta admin-ka

# Ku diiwaan geli admin-ka
admin.site.register(Product, ProductAdmin)
admin.site.register(DownloadRequest)
admin.site.register(UserPoints)
admin.site.register(Favorite)
admin.site.register(SiteSettings)