# django-sphinx-view
Serve your Sphinx docs with Django.

Current status: pre-alpha. You're far too early. 😀

## Basic Usage

Build your Sphinx docs with the `JSONBuilder`, using `make json`.  

Provide a `sphinx_view/page.html` template. This package will ship one in a later 
version.

Route a `DocumentationView` with a `Path` to the output json. 

```python
from pathlib import Path

from django.urls import path
from sphinx_view import DocumentationView

urlpatterns = [
    # ...
    path(
        "docs<path:path>",
        DocumentationView.as_view(
            json_build_dir=Path('/path/to/output/json')
        ),
        name="documentation",
    ),
    # ...
]
```

Enjoy. 

You can subclass `DocumentationView` to require authentication and so add 
access control, and so on. You can customise the template to add other dynamic 
elements.  
