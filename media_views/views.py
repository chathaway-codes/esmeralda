from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

import mimetypes
import os
import time

from .forms import UploadFileForm

def upload_file(request, **kwargs):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            my_file = request.FILES['file']
            full_path = os.path.join(settings.MEDIA_ROOT, kwargs['path'], my_file.name)
            assert(full_path.startswith(settings.MEDIA_ROOT))
	    with open(full_path, 'wb+') as destination:
		for chunk in my_file.chunks():
		    destination.write(chunk)
            return HttpResponseRedirect(reverse('media-file', kwargs={"path": kwargs['path']}))
    raise Http404("File not found")

class FolderView(TemplateView):
    template_name = 'media_views/folder.html'
    def get_path(self, **kwargs):
        path = str(kwargs['path'])
        path = os.path.join(settings.MEDIA_ROOT, path)
        if not os.path.exists(path):
            raise Http404("File not found")
        if not path.startswith(settings.MEDIA_ROOT):
            raise Http404("File not found")
        return path
    def returns_file(self, **kwargs):
        path = self.get_path(**kwargs)
        if os.path.isfile(path):
            # Return file
            filename = path.split('/')[-1]
            with open(path, 'r') as f:
                self.blob = {
                    'name': filename,
                    'data': f.read(),
                    'size': os.path.getsize(path),
                }
            return True
        return False
    def get_context_data(self, **kwargs):
        context = super(FolderView, self).get_context_data(**kwargs)
        path = self.get_path(**kwargs)
        # Construct the list of files; make sure all are valid
        files = []
        for f in os.listdir(path):
            filename = f
            f = os.path.join(path, f)
            assert(f.startswith(settings.MEDIA_ROOT))
            # Get dir info
            file_stats = os.stat(f)
            file_stats = {
                'name': filename,
                'dir': os.path.isdir(f),
                'size': file_stats.st_size,
                'last_modified': time.ctime(file_stats.st_mtime),
                'path': os.path.join(self.url_path, filename),
            }
            files += [file_stats]
        # Sort
        files = sorted(files, key=lambda j: j['name'])
        context['object_list'] = files
        context['path_parts'] = self.url_path.split("/")
        context['path'] = self.url_path
        context['upload_form'] = UploadFileForm()
        return context
    def get(self, request, *args, **kwargs):
        self.url_path = kwargs['path']
        if self.returns_file(**kwargs):
            response = HttpResponse(content_type=mimetypes.guess_type(self.blob['name'])[0])
            response['Content-Length'] = self.blob['size']
            response.write(self.blob['data'])
            return response
        return super(FolderView,self).get(request, *args, **kwargs)

