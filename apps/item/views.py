from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from . import crud, services


def get_item_view(request: HttpRequest, item_id: int) -> HttpResponse:
    item = crud.item.get(id_=item_id)
    if not item:
        raise Http404("Item doesn't exists")
    return render(request, "index.html", context={"item": item})


def create_stripe_session(request: HttpRequest, item_id: int) -> HttpResponse:
    session = services.stripe.get_checkout_session(item_id=item_id)
    if not session:
        raise Http404("You cannot buy an item that not exists")
    return JsonResponse(data={"id": session.id})
