from cookie.models import Order


def _counts(request):
    order = Order.objects.get(uuid=request.session['uuid'])
    order_elems = order.orderelem_set.all()
    return {'count': str(len(order_elems))}
