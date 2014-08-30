import os
import sys

def populate():

    #Memberships Models
    print "Populating Country..."
    add_country('United States')

    print "Populating States..."
    add_province('AL')
    add_province('AK')
    add_province('AZ')
    add_province('AR')
    add_province('CA')
    add_province('CO')
    add_province('CT')
    add_province('DE')
    add_province('FL')
    add_province('GA')
    add_province('HI')
    add_province('ID')
    add_province('IL')
    add_province('IN')
    add_province('IA')
    add_province('KS')
    add_province('KY')
    add_province('LA')
    add_province('ME')
    add_province('MD')
    add_province('MA')
    add_province('MI')
    add_province('MN')
    add_province('MS')
    add_province('MO')
    add_province('MT')
    add_province('NE')
    add_province('NV')
    add_province('NH')
    add_province('NJ')
    add_province('NM')
    add_province('NY')
    add_province('NC')
    add_province('ND')
    add_province('OH')
    add_province('OK')
    add_province('OR')
    add_province('PA')
    add_province('RI')
    add_province('SC')
    add_province('SD')
    add_province('TN')
    add_province('TX')
    add_province('UT')
    add_province('VT')
    add_province('VA')
    add_province('WA')
    add_province('WV')
    add_province('WI')
    add_province('WY')

    print "Populating Grind Types..."
    add_grindtype('Whole Beans')
    add_grindtype('Drip')

    print "Populating Subscription Types..."
    add_subscriptiontype('Monthly')
    add_subscriptiontype('6 Months')
    add_subscriptiontype('12 Months')

    print "Populating Action Types..."
    add_actiontype('Subscribe')
    add_actiontype('Cancel')
    add_actiontype('Update Billing Address')
    add_actiontype('Add Shipping Address')
    add_actiontype('Change Password')
    add_actiontype('Change Email')
    add_actiontype('Change Subscription Type')

    #featured coffee
    print "Populating Months..."
    add_month('January')
    add_month('February')
    add_month('March')
    add_month('April')
    add_month('May')
    add_month('June')
    add_month('July')
    add_month('August')
    add_month('September')
    add_month('October')
    add_month('November')
    add_month('December')

    #Faqs Models
    print "Populating Faqs Category"
    add_faqscategory('General')
    add_faqscategory('Billing')
    add_faqscategory('Shipping')
    add_faqscategory('Coffee')

    #Communications Models
    print "Populating Content Types"
    add_contenttype('Question')
    add_contenttype('Feedback')

    # Print out what we have added to the user.
    print "Countries:"
    for c in Country.objects.all():
        print "- {0}".format(str(c))

    print "States:"
    for p in Province.objects.all():
        print "- {0}".format(str(p))

    print "Months:"
    for m in Month.objects.all():
        print "- {0}".format(str(m))

    print "GrindType:"
    for g in GrindType.objects.all():
        print "- {0}".format(str(g))

    print "Subscription Types:"
    for s in SubscriptionType.objects.all():
        print "- {0}".format(str(s))

    print "Faqs Categories:"
    for f in FaqsCategory.objects.all():
        print "- {0}".format(str(f))

    print "Content Types:"
    for ct in ContentType.objects.all():
        print "- {0}".format(str(ct))

    print "Action Types:"
    for a in ActionType.objects.all():
        print "- {0}".format(str(a.action))


def add_country(name):
    try:
        c = Country.objects.get_or_create(name=name)[0]
    except Exception as e:
        print "Add Country Error: " + e.message
    return c


def add_province(name):
    try:
        p = Province.objects.get_or_create(name=name)[0]
    except Exception as e:
        print "Add Privince Error: " + e.message
    return p


def add_grindtype(name):
    try:
        g = GrindType.objects.get_or_create(type=name)[0]
    except Exception as e:
        print "Add Grind Type Error: " + e.message
    return g


def add_subscriptiontype(name):
    try:
        s = SubscriptionType.objects.get_or_create(type=name)[0]
    except Exception as e:
        print "Add Subscription Type Error: " + e.message
    return s


def add_month(name):
    try:
        m = Month.objects.get_or_create(name=name)[0]
    except Exception as e:
        print "Add Month Error: " + e.message
    return m


def add_faqscategory(name):
    try:
        faqscategory = FaqsCategory.objects.get_or_create(name=name)[0]
    except Exception as e:
        print "Add Faqs Category Error: " + e
    return faqscategory


def add_contenttype(name):
    try:
        contenttype = ContentType.objects.get_or_create(name=name)[0]
    except Exception as e:
        print "Add Content Type Error: " + e.message
    return contenttype


def add_actiontype(name):
    try:
        actiontype = ActionType.objects.get_or_create(action=name)[0]
    except Exception as e:
        print "Add Action Type Error: " + e.message
    return actiontype

# Start execution here!
if __name__ == '__main__':
    #Locate Local Project Path
    SETTINGS_DIR = os.path.dirname(__file__)
    PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
    PROJECT_PATH = os.path.abspath(PROJECT_PATH)
    sys.path.append(PROJECT_PATH)

    print "Starting Coffee population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffeesite.settings')
    from memberships.models import Country, Province, GrindType, SubscriptionType, ActionType
    from featuredcoffee.models import Month
    from faqs.models import FaqsCategory
    from communications.models import ContentType
    populate()