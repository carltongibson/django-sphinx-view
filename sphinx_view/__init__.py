"""Serve your Sphinx docs with Django."""
from .builders import SphinxViewBuilder
from .views import DocumentationView


__version__ = '22.1a6'

__all__ = [
    "__version__",
    "DocumentationView",
    "SphinxViewBuilder",
]


def setup(app):
    app.add_builder(SphinxViewBuilder, override=True)
    return {
        'version': __version__,
        'parallel_read_safe': True
    }
