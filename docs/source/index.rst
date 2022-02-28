.. django-sphinx-view documentation master file, created by
   sphinx-quickstart on Sat May 29 08:57:37 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

django-sphinx-view
==================

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

Optionally, you can add ``"sphinx_view"`` to your ``extensions`` in Sphinx's
``conf.py``::

    extensions = [
        ...
        "sphinx_view",
    ]

This will enable a custom JSON builder that makes the global TOC available on
each page. (If you don't add the `sphinx_view` extension, the default JSON
builder will be used.)

Basic Usage
-----------

Build your Sphinx docs with the JSON builder, using ``make json``.

Route a ``DocumentationView`` with a ``Path`` to the output JSON::

    from pathlib import Path

    from django.urls import path
    from sphinx_view import DocumentationView

    urlpatterns = [
        # ...
        path(
            "docs<path:path>",
            DocumentationView.as_view(
                json_build_dir=Path('/path/to/output/json'),
                base_template_name="docs_base.html",
            ),
            name="documentation",
        ),
        # ...
    ]

The ``json_build_dir`` keyword argument is required, providing the location of
the rendered ouput JSON.

The ``base_template_name`` (default ``base.html``) keyword argument allows you
to provide a base template fitting your site's layout. It should provide
``title``, ``doc``, and ``toc`` blocks.

You may also set a ``template_name`` (default ``sphinx_view/page.html``)
keyword arg to provide a custom template.

The page template receives a context with ``base_template_name`` and ``doc``
keys.

The ``doc`` has these properties:

* ``title``
* ``body``
* ``toc`` - the page contents
* ``toctree`` - the global table of contents

The ``body``, ``toc``, and ``toctree`` elements are rendered HTML and should be
output using the ``safe`` filter::

    # In sphinx_view/page.html
    {% block doc %}
    {{ doc.body|safe }}
    {% endblock doc %}

Enjoy.

You can subclass ``DocumentationView`` to require authentication and so add
access control, and so on. You can customise the template to add other dynamic
elements.

Roadmap
-------

``django-sphinx-view`` has two goals and one non-goal.

Goals:

* The key ``DocumentationView`` **view**  class to serve the rendered JSON
  files. Initial version is in place. I imagine small API adjustments going
  forwards but little else.
* A Sphinx **template bridge** that will allow using the DTL when rendering the
  HTML docs using ``make html`` and the ``HTMLBuilder``. This will complete the
  circle, so to speak, and allow building your docs to static HTML or if you
  don't have the Django development server available.

The non-goal is to replace Sphinx themes in general. ``django-sphinx-view`` is
about integrating Sphinx built docs into your Django site. You bring the
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
