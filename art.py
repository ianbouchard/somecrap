from sys import argv


# pass a read file to argv. 
script, read_file = argv

line_list = []

with open(read_file) as file:
	next(file)
	for line in file:
		line_list = line.split(',')
		output = open(line_list[0]+".txt", 'w')
		output.write("The %s of the National Football League %s when it comes to football teams. \n" % (line_list[0], line_list[5]))
		output.write("They are located in %s, which %s. \nThe %s, or as they are also called the %s, have %s" % (line_list[2], line_list[3], line_list[0], line_list[1], line_list[6]))
		output.write("as a quarterback. %s %s.\nThe %s play at %s which is actually located in %s. \n" % (line_list[6], line_list[7], line_list[0], line_list[8], line_list[9]))
		output.write("If you get a chance to visit %s for a %s game, don't miss the %s which is the signature food item there. " % (line_list[8], line_list[1], line_list[10]))

		
