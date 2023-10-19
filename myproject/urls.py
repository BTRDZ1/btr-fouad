from django.contrib import admin
from django.urls import path, include
from landingpage.views import landing_page
from addproduct.views import generate_html, view_generated_html  # Import the view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Add this line for the admin interface
    path('', landing_page, name='landing_page'),  # Your existing landing page URL
    path('custom_panel/', include('custom_panel.urls')),
    path('addproduct/', generate_html, name='generate_html'),
    path('view/<int:product_id>/', view_generated_html, name='view_generated_html'),  # Add this line
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
