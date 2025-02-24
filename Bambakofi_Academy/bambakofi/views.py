#!/ismailmwarumba/bin/env python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def who_we_are(request):
    return render(request, 'who_we_are.html')

def teaching_learning(request):
    return render(request, 'teaching_learning.html')

def staff(request):
    return render(request, 'staff.html')

def news_events(request):
    # Example data: in a production app these might come from a database.
    event_images = [
        {'url': '/static/images/event1.jpg', 'alt': 'Students at Science Fair', 'caption': 'Science Fair 2025'},
        {'url': '/static/images/event2.jpg', 'alt': 'Sports Day', 'caption': 'Annual Sports Day'},
        # Add more images as needed
    ]
    pdf_files = [
        {'url': '/static/pdfs/magazine_march_2025.pdf', 'title': 'March 2025 School Magazine'},
        {'url': '/static/pdfs/brochure_2025.pdf', 'title': '2025 School Brochure'},
        # Add more PDFs as needed
    ]
    return render(request, 'news_events.html', {
        'event_images': event_images,
        'pdf_files': pdf_files,
    })

def admissions(request):
    return render(request, 'admissions.html')
