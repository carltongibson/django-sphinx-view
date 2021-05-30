import json
from pathlib import Path

from django.http import Http404
from django.views.generic.base import TemplateView


class DocumentationView(TemplateView):
    json_build_dir: Path = None
    base_template_name = "base.html"
    template_name = "sphinx_view/page.html"

    def get_doc_json(self):
        path: str = self.kwargs["path"]
        print(path)
        if not path.endswith("/"):
            raise Http404

        base = Path(self.json_build_dir)
        options = [
            Path(path[1:] + "index.fjson"),
            Path(path[1:-1] + ".fjson"),
        ]
        for o in options:
            candidate = base / o
            print(candidate)
            if candidate.exists():
                with candidate.open("r") as f:
                    return json.load(f)

        raise Http404

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["base_template_name"] = self.base_template_name
        context["doc"] = self.get_doc_json()
        return context
