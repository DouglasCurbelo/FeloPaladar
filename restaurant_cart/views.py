from products.models import Plate
from django.shortcuts import get_object_or_404,render_to_response
from django.http import HttpResponseRedirect
from django.core import urlresolvers
from django.template import RequestContext
from .form import PlateAddToCartForm
#todo:Move all methods not in urls to service methods, refactor all hellpers

# Create your views here.
# views.py
from cart import Cart,ItemDoesNotExist


def add_plate_to_cart(request, plate_id):
	# import pdb; pdb.set_trace()		
	plate_id=int(plate_id)
	plate=get_object_or_404(Plate,pk=int(plate_id))
	if request.method=='POST':
		postdata=request.POST.copy()
		form=PlateAddToCartForm(request,postdata)
		if form.is_valid():
			cart = Cart(request)
			try:
				cart.add_quantity(plate,form.cleaned_data['quantity'])
			except ItemDoesNotExist:
				cart.add(plate, plate.price, form.cleaned_data['quantity'])
			url=urlresolvers.reverse("home")
			# url="/"
			return HttpResponseRedirect(url)

	else:
		form=PlateAddToCartForm(request)
	return render_to_response("cart/add_plate.html"\
			,locals(),context_instance=RequestContext(request))



def remove_plate_from_cart(request, product_id):
    plate=get_object_or_404(Plate,plate_id)
    cart = Cart(request)
    cart.remove(product)

#add tow more products types to cart

def get_cart(request):
    return render_to_response('cart/cart.html', dict(cart=Cart(request)))

