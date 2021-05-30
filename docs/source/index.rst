.. django-sphinx-view documentation master file, created by
   sphinx-quickstart on Sat May 29 08:57:37 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-sphinx-view's documentation!
==============================================

Serve your Sphinx docs with Django.

🚧  Current status: pre-alpha. You're far too early. 😀



Basic Usage
-----------

Build your Sphinx docs with the ``JSONBuilder``, using ``make json``.

Provide a ``sphinx_view/page.html`` template. This package will ship one in a later
version. See `#7 <https://github.com/carltongibson/django-sphinx-view/issues/7>`_.

Route a ``DocumentationView`` with a ``Path`` to the output json::

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

The ``json_build_dir`` keyword argument is required. You may also set
``template_name`` (default ``sphinx_view/page.html``) and
``base_template_name`` (default ``base.html``) keyword arguments.

Enjoy.

You can subclass ``DocumentationView`` to require authentication and so add
access control, and so on. You can customise the template to add other dynamic
elements.




.. toctree::
   :maxdepth: 2
   :caption: Contents:


.. This is TODO:

    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`
