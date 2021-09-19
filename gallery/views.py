from django.shortcuts import render
from upload.models import Images
from .filters import TypeFilter

def gallery(request):
    # Gets all image objects
    images = Images.objects.all()
    
    # Responds to filter's get request
    type_filter = TypeFilter(request.GET, queryset=images)
    filtered_images = type_filter.qs

    context={'page_name':'Gallery', 'type_filter':type_filter, 'images':filtered_images}
    
    return render(request, 'gallery/home.html', context)