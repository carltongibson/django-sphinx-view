"""Serve your Sphinx docs with Django."""
from .builders import SphinxViewBuilder
from .views import DocumentationView


__version__ = '23.1a7'

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
