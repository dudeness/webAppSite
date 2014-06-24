from django.views.generic import TemplateView
from application.settings import config as settings

class DemoPage(TemplateView):
    template_name = 'web/base.html'

    def get_context_data(self, **kwargs):
        context = super(DemoPage, self).get_context_data(**kwargs)
        context['INSTALLED_MODULES'] = settings.INSTALLED_MODULES
        context['SECTION_MODULES'] = settings.SECTION_MODULES
        return context


class EnvironmentJS(TemplateView):
    template_name = 'web/js/environment.js'

    def get(self, request, *args, **kwargs):
        self.content_type = 'application/javascript'
        return super(EnvironmentJS, self).get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EnvironmentJS, self).get_context_data(**kwargs)
        context['INSTALLED_MODULES'] = settings.INSTALLED_MODULES
        context['SECTION_MODULES'] = settings.SECTION_MODULES
        return context
