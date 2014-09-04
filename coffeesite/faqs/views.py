from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

def faqs(request):
    return render_to_response('faqs/faqs.html')