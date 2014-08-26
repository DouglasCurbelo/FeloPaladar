from .models import Plate


def get_activated_plates():
	"""
	Return the list of all activated places
	"""
	return True,Plate.objects.get_actives_plates()
