from django.views.generic import TemplateView

class DemoPage(TemplateView):
    template_name = 'web/base.html'

    def get_context_data(self, **kwargs):
        context = super(DemoPage, self).get_context_data(**kwargs)
        return context
