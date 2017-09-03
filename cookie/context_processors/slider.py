from cookie.models import Product


def _hits(request):
    hits = Product.objects.filter(hit=True).order_by('-date_upload')
    return {'hits': hits}
