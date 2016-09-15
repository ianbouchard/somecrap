from sys import argv
from random import randrange

# script, write_file = argv
p = 1

teams = [
	'kb',
	'ib',
	'gus',
	'bergsy',
	'Brandon',
	'Phil',
	'walks',
	'vu',
	'dane',
	'squeegz',
	'wulf',
	'McP'
	]
	
# output = open(write_file, 'a')
print "Here is your pretend football draft order:\n"

while len(teams) > 0:
	t = teams[randrange(0, (len(teams)))]
	print "pick number %d goes to: %s \n" % (p, t)
	p += 1
	teams.remove(t)
	
print "Happy drafting nerds!"