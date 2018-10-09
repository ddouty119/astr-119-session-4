#python exceptions allow you to deal with  unexpected results

try:
	print(a)		#this will throw an exception because a is not defined
except:
	print("a is not defined!")
	
#there are specific errors to hep with cases
try: 
	print(a)		#will trow an exception
except NameError:
	print("a is still not defined!")	
except:
	print("Something else went wrong")
	
#this will break program since a is not defined
print(a)