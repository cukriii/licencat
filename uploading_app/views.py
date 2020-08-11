from django.shortcuts import render
from .forms import UploadFileForm
from somewhere import handle_uploaded_file
from django.http import HttpResponseRedirect

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'uploading.html', {'form': form})