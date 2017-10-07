
def log(original_function, logfilename="log.txt"):
	def new_function(*args, **kwargs):
		with open(logfilename, "w") as logfile:
	            logfile.write("Function '%s' called with positional arguments %s and keyword arguments %s.\n" % (original_function.__name__, args, kwargs))
		return original_function(*args, **kwargs)
	return new_function

@log
def addition(x,y):
    return x + y
print(addition(133, 144))

with open("log.txt", "r") as logfile:
    print(logfile.read())
