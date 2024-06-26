from django.shortcuts import render
from .models import Events, Impressum, InformationImage, Impressum

def index(request):
    events = Events.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'events/event_list.html', context)


def information(request):
    images = InformationImage.objects.all()
    context = {
        'images': images
    }
    return render(request, 'events/information.html', context)


def impressum_view(request):
    impressum_item = Impressum.objects.get(id=2)  # Adjust the query to fetch the correct Impressum object
    return render(request, 'events/impressum.html', {'item': impressum_item})
