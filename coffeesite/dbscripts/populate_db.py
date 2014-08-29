import os

def populate():
    add_country('USA')
    add_province('NY')

    # Print out what we have added to the user.
    for c in Country.objects.all():
         print "- {0}".format(str(c))

    for p in Province.objects.all():
         print "- {0}".format(str(p))

def add_country(name):
    c = Country.objects.get_or_create(name=name)[0]
    return c

def add_province(name):
    p = Province.objects.get_or_create(name=name)[0]
    return p

# Start execution here!
if __name__ == '__main__':
    print "Starting Coffee population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffeesite.settings')
    from communications.models import ContentType
    from memberships.models import ActionType, Country, Province
    populate()