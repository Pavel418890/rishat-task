from typing import Optional

import stripe as stripelib
from django.conf import settings

from . import crud


class Stripe:
    stripelib.api_key = settings.STRIPE_PRIVATE_KEY

    def get_checkout_session(
        self, item_id: int
    ) -> Optional[stripelib.checkout.Session]:
        item = crud.item.get(id_=item_id)
        session = None
        if item:
            session = stripelib.checkout.Session.create(
                success_url="{}/admin/item/item/".format(settings.CLIENT_BASE_URL),
                cancel_url="{}/".format(settings.CLIENT_BASE_URL),
                payment_method_types=["card"],
                mode="payment",
                line_items=[
                    {
                        "name": item.name,
                        "description": item.description,
                        "amount": int(item.price * 100),
                        "currency": "usd",
                        "quantity": 1,
                    }
                ],
            )
        return session


stripe = Stripe()
