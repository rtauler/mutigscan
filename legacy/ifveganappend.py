def wordcount(filename,listwords):
	inputpath = "/Users/marta/Desktop/Vegan-filter/"+str(listwords)+'.txt'
	inputfile = open (inputpath, "r")
	inputread = inputfile.read()
	inputline = inputread.split(',')
	print (inputline)
	try:
		if inputline == ['']:
			raise ValueError ('nothing to process in ' + filename)
		path = "/Users/marta/Desktop/Vegan-filter/"+filename+'.txt'
		file = open (path, "r")
		read = file.read()
		file.close()
		for inputingredient in inputline:
			inputlower = inputingredient.lower()
			inputclean = inputlower.lstrip()
			print (inputclean)
			count = 0
			line = read.split('\n')
			for item in line:
				line = item.lower()
				if inputclean == line:
					count += 1

			if count >= 1:
				if count == 1:
					print (inputclean, "is already" , count, "time in", filename)
				else:
					print (inputclean, "is already" , count, "times in", filename)
			else:
				print (inputclean, 'was not yet in', filename, 'I will add it now!') 
				file = open (path, "a")
				file.write("\n")
				file.write(inputclean)
	except ValueError as e:
		print (e)
			
# Check and add VEGAN ingredient
wordcount("vegan-ingredients", 'veganinput')

# Check and add AMBIGUOUS ingredient
wordcount("can-be-both", 'ambiguousinput')

# Check and add NON vegan ingredient
wordcount("non-vegan-ingredients", 'nonveganinput')
