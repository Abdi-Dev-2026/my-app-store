from django.conf import settings
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('games', 'Games'),
        ('apps', 'Apps'),
        ('tools', 'Tools'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    download_link = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='apps')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DownloadRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20) 
    status = models.CharField(max_length=20, default='pending') 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product.name} - {self.status}"

class UserPoints(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.points} Points"

    def balance_in_usd(self):
        return self.points * 0.01

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

class SiteSettings(models.Model):
    maintenance_mode = models.BooleanField(default=False)

    def __str__(self):
        return "Site Settings"