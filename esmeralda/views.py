from cgi import escape
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.urls import resolve
from django.views.generic.base import TemplateView
import re
from stream.models import StreamEvent
from xhtml2pdf import pisa
import cStringIO as StringIO

class HomePageView(TemplateView):
    template_name = 'esmeralda/home.html'
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['events'] = StreamEvent.objects.all().order_by('-when')[:10]
        return context

def render_page_pdf(request, **kwargs):
    path = request.path[:-4] # Remove .pdf
    view, args, kwargs = resolve(path)
    kwargs['request'] = request
    html = view(*args, **kwargs).rendered_content
    html = html.replace('\n', '').replace('\r', '')
    html = re.sub('<nav.+</nav>', '', html);
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
