from django.contrib import admin

# Register your models here.
from django.shortcuts import render

class ClientDataAdmin(admin.ModelAdmin):
    # ... other configurations ...

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_confirm_cancel'] = True
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    
    # ... rest of your configurations ...
