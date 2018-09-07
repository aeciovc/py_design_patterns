from functools import wraps

def serializer(func):
	"""Defines a serializer decorator fo response functions"""

	@wraps(func)

	def decorator():
		#grab the return function mapped to be decorated
		ret = func()

		#Add new behavior
		return {"result":ret}

	return decorator

#Apply decorator
@serializer
def ping():
	""" Ping resource function """
	return "pong"


print(ping())

print(ping.__name__)

print(ping.__doc__)