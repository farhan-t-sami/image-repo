from django.shortcuts import render
from .forms import ModelFormWithFileField

def upload(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Returns cleared form
            form = ModelFormWithFileField()
            return render(request, 'upload/upload.html', {'page_name':'Upload', 'form': form})
    else:
        form = ModelFormWithFileField()
    return render(request, 'upload/upload.html', {'page_name':'Upload', 'form': form})