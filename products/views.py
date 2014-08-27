# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
import services



def product_list(request):
	"""
 	Return the lsit of all plates restaurant 
 	To considerate add pagination to the software
	"""			
	success,plates=services.get_activated_plates()	
	if success:
		return render_to_response('restaurant_menu.html',locals()
			,context_instance=RequestContext(request))
	else:
		pass #show a custom message error





