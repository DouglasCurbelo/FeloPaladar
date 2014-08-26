from products.models import Plate
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


#todo:Move all methods not in urls to service methods, refactor all hellpers

# Create your views here.
# views.py
from cart import Cart


def add_plate_to_cart(request, plate_id, quantity):
    plate=get_object_or_404(Plate,plate_id)
    cart = Cart(request)
    cart.add(product, product.unit_price, quantity)

def remove_plate_from_cart(request, product_id):
    plate=get_object_or_404(Plate,plate_id)
    cart = Cart(request)
    cart.remove(product)

#add tow more products types to cart

def get_cart(request):
    return render_to_response('cart/cart.html', dict(cart=Cart(request)))

