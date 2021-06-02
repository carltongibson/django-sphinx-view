.. django-sphinx-view documentation master file, created by
   sphinx-quickstart on Sat May 29 08:57:37 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-sphinx-view's documentation!
==============================================

Serve your Sphinx docs with Django.

Installation
------------

Install using ``pip``:

.. code-block::

    pip install django-sphinx-view

Then add ``sphinx_view`` to ``INSTALLED_APPS`` for template discovery::

   INSTALLED_APPS = [
       ...
       "sphinx_view",
       ...
   ]

That's it. You're good to go.

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

Roadmap
-------

``django-sphinx-view`` has three goals and one non-goal.

Goals:

* The key ``DocumentationView`` **view**  class to serve the rendered JSON
  files. Initial version is in place. I imagine small API adjustments going
  forwards but little else.
* A Sphinx **template bridge** that will allow using the DTL when rendering the
  HTML docs using ``make html`` and the ``HTMLBuilder``. This will complete the
  circle, so to speak, and allow building your docs to static HTML or if you
  don't have the Django development server available.
* Provide a **doc page template** for the 80% case. My current development
  template has too much of my site's markup in it. I need to move that towards
  the base template, and then what's left should (in theory) be good for most
  sites to use. It should be just the blocks containing the sections from the
  JSON.

The non-goal is to replace Sphinx themes in general. ``django-sphinx-view`` is
about integrating Sphinx build docs into your Django site. You bring the
styling, you bring the theme.

.. toctree::
   :maxdepth: 2
   :caption: Contents:


.. This is TODO:

    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`
