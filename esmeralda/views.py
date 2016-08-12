from django.views.generic.base import TemplateView
from stream.models import StreamEvent

class HomePageView(TemplateView):
    template_name = 'esmeralda/home.html'
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['events'] = StreamEvent.objects.all().order_by('-when')[:10]
        return context

