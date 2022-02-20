from sphinxcontrib.serializinghtml import JSONHTMLBuilder
from sphinx.environment.adapters.toctree import TocTree


class SphinxViewBuilder(JSONHTMLBuilder):

    name = 'json'  # Overriding the default

    def get_doc_context(self, docname, body, metatags):
        doc = super().get_doc_context(docname, body, metatags)
        self_toctree = TocTree(self.env).get_toctree_for(docname, self, True)
        toctree = self.render_partial(self_toctree)['fragment']
        doc['toctree'] = toctree
        return doc
