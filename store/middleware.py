from django.shortcuts import render
from .models import SiteSettings

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            settings = SiteSettings.objects.first()
            
            if settings and settings.maintenance_mode:
                if request.path.startswith('/admin/') or (request.user.is_authenticated and request.user.is_superuser):
                    return self.get_response(request)

                return render(request, 'maintenance.html')
        except:
            pass

        return self.get_response(request)