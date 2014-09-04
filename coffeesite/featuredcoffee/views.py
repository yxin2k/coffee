from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from featuredcoffee.models import Coffee, Month
import datetime
import logging

#App name must be declared in settings.py to use __name__
logger = logging.getLogger(__name__)

def coffee(request, year, month):

    if year and month is None:
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        logger.error('month is:' + month)
    # Obtain the context from the HTTP request.
    context = RequestContext(request)
    context_dict = {'year': year, 'month': month}

    try:
        m = Month.objects.get(name=month)
        coffee_list = Coffee.objects.all().filter(highlight_year=year, highlight_month=m.id).order_by('sort_number')
        context_dict['coffee_list'] = coffee_list

    except Exception as e:
        logger.error(e.message)

    return render_to_response('featuredcoffee/coffee.html', context_dict, context)

# def coffee(request):
#
#     year = datetime.datetime.today().year
#     month = datetime.datetime.today().strftime('%B')
#
#     # Obtain the context from the HTTP request.
#     context = RequestContext(request)
#     context_dict = {'year': year, 'month': month}
#
#     return render_to_response('featuredcoffee/coffee.html', context_dict, context)