from django.urls import path
from addproduct.views import generate_html,view_generated_html

urlpatterns = [
    # ... your other URL patterns
    path('addproduct/', generate_html, name='generate_html'),
    path('view_html/<int:product_id>/', view_generated_html, name='view_generated_html'),

]

