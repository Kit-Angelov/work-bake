from django.shortcuts import render, get_object_or_404, render_to_response, get_list_or_404
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
from .models import Product, Category, Order, OrderElem, Call
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import uuid
from .forms import ProductsSearchForm


def index(request):
    check_uuid(request)
    order = __create_order(request.session['uuid'])
    category_index_list = Category.objects.filter(display=True).order_by('-priority')
    context = dict(categories=category_index_list[:6])
    return render(request, 'cookie/index.html', context=context)


def catalog(request, category_id):
    check_uuid(request)
    category_name = get_object_or_404(Category, id=category_id)
    category_menu = Category.objects.filter(display=True)
    product_list = Product.objects.filter(category=category_id)
    paginator = Paginator(product_list, 9)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = dict(
        products=products,
        category_name=category_name,
        category_menu=category_menu,
    )
    return render(request, 'cookie/catalog.html', context=context)


def product_detail(request, product_id):
    category_menu = Category.objects.filter(display=True)
    if request.session.get('uuid', None) is None:
        request.session['uuid'] = str(uuid.uuid4())
    else:
        print(request.session['uuid'])
    product = get_object_or_404(Product, id=product_id)
    photos = product.photoproduct_set.all()
    context = dict(
        product=product,
        category_menu=category_menu,
        photos=photos,
    )
    return render(request, 'cookie/product.html', context=context)


def basket(request):
    check_uuid(request)
    order = __create_order(request.session['uuid'])

    print(order)
    print(order.orderelem_set.all())
    order_elems = order.orderelem_set.all()
    paginator = Paginator(order_elems, 8)
    page = request.GET.get('page')
    try:
        order_elems = paginator.page(page)
    except PageNotAnInteger:
        order_elems = paginator.page(1)
    except EmptyPage:
        order_elems = paginator.page(paginator.num_pages)
    context = dict(
        order_elems=order_elems
    )
    return render(request, 'cookie/basket.html', context=context)


def basket_closed(request):
    check_uuid(request)
    order = __create_order(request.session['uuid'])
    if request.method == 'POST':
        form = request.POST
        print(form)
        name = form.get('name')
        phone = form.get('phone')
        address = form.get('address')
        order.name = str(name)
        order.phone = str(phone)
        order.address = str(address)
    order_elems = order.orderelem_set.all()
    order.sum = 0.0
    for order_elem in order_elems:
        order.sum += float(order_elem.sum)
    order.save()
    paginator = Paginator(order_elems, 8)
    page = request.GET.get('page')
    try:
        order_elems = paginator.page(page)
    except PageNotAnInteger:
        order_elems = paginator.page(1)
    except EmptyPage:
        order_elems = paginator.page(paginator.num_pages)

    context = {
        'order_elems': order_elems,
        'count_order_elem': len(order_elems),
        'sum': order.sum,
        'address': order.address,
        'phone': order.phone,
        'name': order.name,

    }
    return render(request, 'cookie/basket_closed.html', context=context)


def search(request):
    check_uuid(request)
    form = ProductsSearchForm(request.GET)
    text_query = request.GET.get('q', None)
    product_list = form.search()
    paginator = Paginator(product_list, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'text_query': text_query,
    }
    return render(request, 'cookie/search.html', context=context)

'''
def add_to_basket(request, product_id):
    if request.session.get('uuid', None) is None:
        request.session['uuid'] = str(uuid.uuid4())
    else:
        print(request.session['uuid'])
    try:
        order = Order.objects.get(uuid=request.session['uuid'])
    except Exception:
        order = Order(uuid=request.session['uuid'])
    form = PriceForm(request.Get)
    weight_product = form.
    product = Product.objects.get(id = product_id)
    sum_product = product.price * weight_product
    param_order = [str(sum_product), str(weight_product)]
    order.set_product_list(product_id, param_order)
'''


def __create_order(uuid):
    try:
        order = Order.objects.get(uuid=uuid)
    except:
        order = Order(uuid=uuid)
        order.save()
    return order


def add_to_basket(request):
    context = {}
    check_uuid(request)
    order = __create_order(request.session['uuid'])
    if request.method == 'GET':
        weight = request.GET.get('weight')
        if weight == '':
            weight = 0.0
        product_id = request.GET.get('product_id')
        product = Product.objects.get(id=product_id)
        new_order_elem = OrderElem(product=product, order=order, weight=float(weight))
        new_order_elem.save()
        print(new_order_elem.order.uuid)
    try:
        order = Order.objects.get(uuid=request.session['uuid'])
        order_elems = order.orderelem_set.all()
        context = str(len(order_elems))
    except:
        request.session['uuid'] = str(uuid.uuid4())
        order = Order(uuid=request.session['uuid'])
        context = str(0)
    finally:
        return HttpResponse(context, content_type="text/html")


def delete_order_elem_basket(request, id):
    try:
        order_elem = OrderElem.objects.get(id=id)
        order_elem.delete()
        return basket(request)
    except:
        return basket(request)


def delete_order_elem_basket_closed(request, id):
    try:
        order_elem = OrderElem.objects.get(id=id)
        order_elem.delete()
        return basket_closed(request)
    except:
        return basket_closed(request)


def closed_order(request):
    check_uuid(request)
    order = __create_order(request.session['uuid'])
    order.closed = True
    order.save()
    if check_order(order) is True:
        request.session['uuid'] = None
    return index(request)


def check_order(order):
    res = True
    list_attr = [order.uuid, order.name, order.phone, order.address]
    for a in list_attr:
        if a is not None:
            continue
        else:
            res = False
    return res


def call(request):
    check_uuid(request)
    if request.method == 'GET':
        form = request.GET
        print(form)
        name = form.get('name')
        phone = form.get('phone')
        address = form.get('address')
        call = Call(name=name, phone=phone, address=address)
        call.save()
    return HttpResponse(content='ok', content_type="text/html")


def check_uuid(request):
    if request.session.get('uuid', None) is None:
        request.session['uuid'] = str(uuid.uuid4())
    else:
        print(request.session['uuid'])
