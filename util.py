# this file is just copied from another project
from time import strftime

def p(prefix, text): # nice print function
	t = getTime()
	print("[" + t + "][" + prefix + "] " + text)

def pp(prefix, text, line_end=''): # nice print function
	t = getTime()
	print("[" + t + "][" + prefix + "] " + text, end=line_end)

def getTime(format="%d.%m.%Y %H:%M:%S"):
	try:
		return strftime(format)
	except Exception:
		return getTime("%d.%m.%Y %H:%M:%S")