from django.contrib.auth.views import PasswordResetView
from django.contrib import admin

def admin_header_processor(request):
    site_header = getattr(admin.site, 'site_header')  # get site header text. For django 2.X it should be 
    return {"site_header": site_header} 