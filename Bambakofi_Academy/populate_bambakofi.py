#!/ismailmwarumba/bin/env python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bambakofi_Academy.settings')

import django
django.setup()

from bambakofi.models import Category, Page


def populate():

    python_pages = [
        {"title": "Official Python Tutorial",
         "views": 128,
         "url": "http://docs.python.org/2/tutorial/"},

        {"title": "How to Think like a Computer Scientist",
         "views": 64,
         "url": "http://www.greenteapress.com/thinkpython/"},

        {"title": "Learn Python in 10 Minutes",
         "views": 32,
         "url": "http://www.korokithakis.net/tutorials/python/"}
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "views": 128,
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},

        {"title": "Django Rocks",
         "views": 64,
         "url": "http://www.djangorocks.com/"},

        {"title": "How to Tango with Django",
         "views": 32,
         "url": "http://www.tangowithdjango.com/"}
    ]

    other_pages = [
        {"title": "Bottle",
         "views": 128,
         "url": "http://bottlepy.org/docs/dev/"},

        {"title": "Flask",
         "views": 64,
         "url": "http://flask.pocoo.org"}
    ]

    cats = {'Python': {'pages': python_pages},
            'Django': {'pages': django_pages},
            'Other Frameworks': {'pages': other_pages} }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])


    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()