from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'index.html'

class ConstructionPage(TemplateView):
    template_name = 'underconstruction.html'

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class ProjectPage(TemplateView):
    template_name = 'projects.html'
