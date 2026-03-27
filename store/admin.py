from django.contrib import admin
from .models import Product, DownloadRequest, UserPoints, Favorite, SiteSettings

admin.site.register(Product)
admin.site.register(DownloadRequest)
admin.site.register(UserPoints)
admin.site.register(Favorite)
admin.site.register(SiteSettings)