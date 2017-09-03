from django.shortcuts import render, get_object_or_404, render_to_response, get_list_or_404
from django.template import RequestContext
from django.http import HttpResponse
from .models import Product, Category, Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import uuid
from .forms import ProductsSearchForm


def index(request):
    if request.session.get('uuid', None) is None:
        request.session['uuid'] = str(uuid.uuid4())
    else:
        print(request.session['uuid'])
    category_index_list = Category.objects.filter(display=True).order_by('-priority')
    context = dict(categories=category_index_list[:6])
    return render(request, 'cookie/index.html', context=context)


def catalog(request, category_id):
    if request.session.get('uuid', None) is None:
        request.session['uuid'] = str(uuid.uuid4())
    else:
        print(request.session['uuid'])
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
    )
    return render(request, 'cookie/catalog.html', context=context)


def product_detail(request, product_id):
    if request.session.get('uuid', None) is None:
        request.session['uuid'] = str(uuid.uuid4())
    else:
        print(request.session['uuid'])
    product = get_object_or_404(Product, id=product_id)
    context = dict(product=product)
    return render(request, 'cookie/product.html', context=context)


def basket(request):
    if request.session.get('uuid', None) is None:
        request.session['uuid'] = str(uuid.uuid4())
    else:
        print(request.session['uuid'])
    return render(request, 'cookie/basket.html')


def search(request):
    if request.session.get('uuid', None) is None:
        request.session['uuid'] = str(uuid.uuid4())
    else:
        print(request.session['uuid'])
    form = ProductsSearchForm(request.GET)
    products = form.search()
    return render_to_response('cookie/search.html', {'products': products})

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