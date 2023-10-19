from django.contrib import admin
from .models import Product
from django.urls import reverse
from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'generate_html_link']

    def generate_html_link(self, obj):
        # Construct the URL for viewing the generated HTML
        html_file_url = reverse('view_generated_html', kwargs={'product_id': obj.id})
        return format_html('<a href="{}">View HTML</a>', html_file_url)

    generate_html_link.short_description = 'Generated HTML'
