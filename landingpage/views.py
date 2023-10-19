import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from .forms import ClientDataForm, ImageForm
from .models import Image

def generate_html_with_images(product_name, images):
    # Load the HTML template
    template_path = os.path.join(os.path.dirname(__file__), 'templates/landingpage/landing_page.html')

    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    # Replace background image placeholders with the chosen image URLs
    for i, image in enumerate(images):
        template_content = template_content.replace(f'{{{{ image.image_file.url{i} }}}}', image.image_file.url)

    # Save the HTML content to a new file
    save_dir = os.path.join(os.path.dirname(__file__), f'templates/landingpage/product/')
    html_file_path = os.path.join(save_dir, f'{product_name}.html')

    with open(html_file_path, 'w') as html_file:
        html_file.write(template_content)

    return html_file_path

def landing_page(request):
    # Fetch all images from the Image model
    images = Image.objects.all()

    if request.method == 'POST':
        form = ClientDataForm(request.POST)
        if form.is_valid():
            form.save()

            # Generate HTML content and save to a file
            product_name = form.cleaned_data['product_name']  # Assuming product_name is a field in ClientDataForm
            html_file_path = generate_html_with_images(product_name, images)

            return HttpResponse(f'HTML file generated: <a href="{html_file_path}">{product_name}.html')
    else:
        form = ClientDataForm()

    return render(request, 'landingpage/landing_page.html', {'form': form, 'images': images})
