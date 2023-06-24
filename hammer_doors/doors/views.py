import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from doors.models import Door, CTA


# Create your views here.
def index(request):
    doors = Door.objects.order_by('popular')[:10]
    try:
        cta = CTA.objects.get(show=True)
    except ObjectDoesNotExist:
        cta = CTA.objects.first()

    if not request.COOKIES.get('history'):
        response = render(request, "pages/index.html", context={'doors': doors, 'cta': cta, 'title': 'Главная', 'history': []})
        response.set_cookie(
            "history", json.dumps({"products_uuid": []}).replace(" ", "")
        )
        return response
    else:
        uuids = json.loads(request.COOKIES.get('history'))["products_uuid"]
        history = []
        for uuid in uuids:
            try:
                product = Door.objects.get(uuid= uuid)
                history.append(product)
            except Door.DoesNotExist:
                pass

        return render(request, "pages/index.html", context={'doors': doors, 'cta': cta, 'title': 'Главная', 'history': history })


def detail(request, pk=1):
    door = Door.objects.all()[pk - 1]

    response = render(request, "pages/detail.html", context={'door': door, 'title': door.title})
    if not request.COOKIES.get('history'):
        response.set_cookie(
            "history", json.dumps({"products_uuid": [door.uuid]}).replace(" ", "")
        )
    else:
        uuids = json.loads(request.COOKIES.get('history'))["products_uuid"]
        not_exist = True
        for uuid in uuids:
            if uuid == str(door.uuid):
                not_exist = False
                break
        if not_exist:
            uuids.append(str(door.uuid))
            response.set_cookie(
                'history', json.dumps({"products_uuid": uuids}).replace(" ", "")
            )
    return response


def catalog(request):
    page_number = request.GET.get('page')
    doors = Door.objects.all()
    p = Paginator(doors, 9)
    page = p.get_page(page_number)
    return render(request, 'pages/catalog.html', context={'page': page, 'door_count': len(doors), 'title': 'Каталог'})


def contacts(request):
    return render(request, 'pages/contacts.html', context={'title': 'Контакты'})
