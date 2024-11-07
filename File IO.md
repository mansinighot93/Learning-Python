In Django, handling File I/O (input/output) operations is typically done with the help of Django’s `FileField` and `ImageField`, or using Python's built-in file handling capabilities. Here’s how you can manage file uploads, saving files to the server, and reading from files within a Django application.

### 1. **Handling File Uploads in Django**

To upload files in Django, you can use the `FileField` or `ImageField` in your model, then handle the file upload through forms.

#### Example: Creating a model with a file field

```python
# models.py
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

- `upload_to='documents/'` specifies the folder inside the `MEDIA_ROOT` directory where the files will be uploaded.

#### Example: Creating a form to upload the file

```python
# forms.py
from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'file')
```

#### Example: Handling file upload in a view

```python
# views.py
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')  # Redirect to the file listing page
    else:
        form = DocumentForm()

    return render(request, 'upload_file.html', {'form': form})

def file_list(request):
    documents = Document.objects.all()
    return render(request, 'file_list.html', {'documents': documents})
```

#### Example: HTML templates

**upload_file.html**
```html
<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>
```

**file_list.html**
```html
<h2>Uploaded Files</h2>
<ul>
    {% for document in documents %}
        <li>{{ document.title }} - <a href="{{ document.file.url }}">Download</a></li>
    {% endfor %}
</ul>
```

### 2. **Configuring `MEDIA_ROOT` and `MEDIA_URL`**

To properly serve media files, ensure that your `settings.py` is configured as follows:

```python
# settings.py

import os

# Define the root directory for storing uploaded files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Also, add this to the `urls.py` to serve media files during development:

```python
# urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Your other URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 3. **Reading and Writing Files in Views (Custom File I/O)**

If you need to read or write files outside of the `FileField` or `ImageField` context, you can use Python's standard file I/O functions.

#### Example: Writing to a text file

```python
# views.py

from django.http import HttpResponse

def write_to_file(request):
    with open('myfile.txt', 'w') as f:
        f.write("Hello, Django file I/O!")
    return HttpResponse("File has been written.")
```

#### Example: Reading a file

```python
# views.py

from django.http import HttpResponse

def read_from_file(request):
    with open('myfile.txt', 'r') as f:
        content = f.read()
    return HttpResponse(content)
```

