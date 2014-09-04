from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from faqs.models import Faqs, FaqsCategory
import logging

#App name must be declared in settings.py to use __name__
logger = logging.getLogger(__name__)

def faqs(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    try:
        faqscateg_list = FaqsCategory.objects.order_by('name')
        faqs_list = Faqs.objects.order_by('category')

        context_dict = {
            'faqs_categ': faqscateg_list,
            'faqs': faqs_list
        }
    except Exception as e:
        logger.error(e.message)

    return render_to_response('faqs/faqs.html', context_dict, context)