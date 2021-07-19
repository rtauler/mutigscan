def wordcount(filename,listwords):
	try:
		file = open (filename, "r")
		read = file.read()
		file.close()
		for word in listwords:
			lower = word.lower()
			count = 0
			line = read.split('\n')
			print (line)
			for item in line:
				line = item.lower()
				if lower == line:
					count += 1

			if count >= 1:
				if count == 1:
					print (lower, "is already" , count, "time in the list!")
				else:
					print (lower, "is already" , count, "times in the list!")
			else:
				print (lower, 'was not yet in the list, I will add it now!') 
				file = open (filename, "a")
				file.write("\n")
				file.write(lower)
	except FileExistsError:
		print ('The file is not there ')
			

wordcount("/Users/marta/Desktop/Vegan-filter/vegan-ingredients.txt", ["apple"])