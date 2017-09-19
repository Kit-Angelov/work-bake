from cookie.models import Order
import uuid


def _counts(request):
    try:
        order = Order.objects.get(uuid=request.session['uuid'])
        order_elems = order.orderelem_set.all()
        return {'count': str(len(order_elems))}
    except:
        return {'count': str(0)}

"""
    except:
        request.session['uuid'] = str(uuid.uuid4())
        order = Order(uuid=request.session['uuid'])
        print('CREATE IN CONTEXT ')
    try:
    """