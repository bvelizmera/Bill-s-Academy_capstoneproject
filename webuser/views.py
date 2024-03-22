# views.py
from django.shortcuts import render, redirect
from .forms import MyModelForm

def upload_image(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')  # Redirect to a view that displays the uploaded images
    else:
        form = MyModelForm()
    return render(request, 'webuser/upload_image.html', {'form': form})
