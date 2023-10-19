import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProductForm
from .models import Product

def generate_html(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Create an HTML template and inject the product data
            product = form.save()
            html_content = f"<h1>{product.name}</h1><p>{product.description}</p><p>Price: ${product.price}</p>"

            # Specify a directory within MEDIA_ROOT where you want to save HTML files
            html_directory = os.path.join(settings.MEDIA_ROOT, 'generated_html')
            os.makedirs(html_directory, exist_ok=True)  # Create the directory if it doesn't exist

            # Construct the file path for the HTML file
            html_file_path = os.path.join(html_directory, f'product_{product.id}.html')

            # Save the HTML content to the file
            with open(html_file_path, 'w') as html_file:
                html_file.write(html_content)

            return HttpResponse(f'HTML file generated: <a href="{html_file_path}">View</a>')

    else:
        form = ProductForm()

    return render(request, 'addproduct/generate_html.html', {'form': form})

def view_generated_html(request, product_id):
    # Retrieve the product object
    product = Product.objects.get(pk=product_id)
    print("---------------------------")
    print(product.name)
    # Construct the file path for the HTML file
    html_file_path = os.path.join(settings.MEDIA_ROOT, f'generated_html/product_{product.id}.html')

    try:
        # Open the HTML file and read its content
        with open(html_file_path, 'r') as html_file:
            html_content = html_file.read()
        return HttpResponse(html_content, content_type='text/html')

    except FileNotFoundError:
        return HttpResponse("HTML file not found.", status=404)
