from Web.cart.models import CartItem
from Web.products.models import Plate
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from Web.cart.form import PlateAddToCartForm
#todo:Move all methods not in urls to service methods, refactor all hellpers

# Create your views here.
def _cart_id(request):
	if 'cart_id' in request.session:
			request.session['cart_id'] = _generate_cart_id()
	return request.session['cart_id']

import random
def _generate_cart_id():
	cart_id = ''
	characters = 'ABCDEFGHIJKLMNOPQRQSTUVWXYZabcdefghijklm\
	nopqrstuvwxyz1234567890!@#$%^&*()'
	cart_id_length = 50
	for y in range(cart_id_length):
		cart_id += characters[random.randint(0, len(characters)-1)]
	return cart_id

# return all items from the current user's cart
def get_cart_items(request):
	return CartItem.objects.filter(cart_id=_cart_id(request))

# add an item to the cart
def add_to_cart(request):
	postdata = request.POST.copy()
	# get product slug from post data, return blank if empty
	product_id = postdata.get('product_id','')
	# get quantity added, return 1 if empty
	quantity = postdata.get('quantity',1)
	# fetch the product or return a missing page error
	p = get_object_or_404(Plate, id=product_id)
	#get products in cart
	cart_products = get_cart_items(request)
	product_in_cart = False
	# check to see if item is already in cart
	for cart_item in cart_products:
		if cart_item.product.id = p.id:
		# update th(e quantity if found
			cart_item.augment_quantity(quantity)
			product_in_cart = True
	if not product_in_cart:
		# create and save a new cart item
		ci = CartItem()
		ci.product = p
		ci.quantity = quantity
		ci.cart_id = _cart_id(request)
		ci.save()

# returns the total number of items in the user's cart
def cart_distinct_item_count(request):
	return get_cart_items(request).count()


def add_plate_to_cart(request,plate_id):
	postdata=request.POST.copy()
	form=PlateAddToCartForm(postdata)

	if form.is_valid():
		add_to_cart(request)
		if request.session.test_cookie_worked():
			request.session.delete_test_cookie()
		url = urlresolvers.reverse('show_cart')
		return HttpResponseRedirect(url)


def show_cart(request,template):
	return HttpResponseRedirect("/")


