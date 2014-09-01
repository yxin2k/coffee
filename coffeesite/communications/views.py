from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from communications.forms import SubmissionForm
import logging

#App name must be declared in settings.py to use __name__
logger = logging.getLogger(__name__)


def index(request):
    return render_to_response('index.html')


def contact_us(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = SubmissionForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = SubmissionForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('communications/contact.html', {'form': form}, context)