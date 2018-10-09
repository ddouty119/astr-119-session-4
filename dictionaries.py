#define dictionary data structure
#dictionary made up of key:value elements
example_dict = {
	"class"			:	"Astr 119",
	"prof"			:	"Brant",
	"awesomeness"	:	10
}

print(type(example_dict))	#will say dict

#getting a value from a key
course = example_dict["class"]
print(course)

#change a value via a key
example_dict["awesomeness"] += 1		#increase awesomeness

#print the dictionary
print(example_dict)

#print dictionary element by element
for x in example_dict.keys():
	print(x,example_dict[x])
