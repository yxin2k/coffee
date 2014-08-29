import os
import sys

def populate():
    add_country('United States')
    add_province('NY')
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



    # Print out what we have added to the user.
    for c in Country.objects.all():
        print "- {0}".format(str(c))

    for p in Province.objects.all():
        print "- {0}".format(str(p))

    for m in Month.objects.all():
        print "- {0}".format(str(m))

def add_country(name):
    c = Country.objects.get_or_create(name=name)[0]
    return c

def add_province(name):
    p = Province.objects.get_or_create(name=name)[0]
    return p

def add_month(name):
    m = Month.objects.get_or_create(name=name)[0]
    return m

# Start execution here!
if __name__ == '__main__':
    #Locate Project Path
    SETTINGS_DIR = os.path.dirname(__file__)
    PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
    PROJECT_PATH = os.path.abspath(PROJECT_PATH)
    sys.path.append(PROJECT_PATH)

    print "Starting Coffee population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffeesite.settings')
    from memberships.models import Country, Province
    from featuredcoffee.models import Month
    populate()