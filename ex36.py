from random import randint
from random import randrange

gear = {}

def get_water():
	print "Let's go fly fishing. What type of water do you want to fish? Type: salt or fresh"
	water = raw_input('>> ')
	if water == "salt" or water == "fresh":
		return water
	else:
		water = get_water()
		return water
	

def get_size():
	print "Do you want to fish big or small %swater? Type big or small" % water
	size = raw_input('>> ')
	if size == "big" or size == "small":
		return size
	else:
		size = get_size()
		return size

def get_flow():
	print "What type of %s %swater would you like to fish? Type calm or moving" % (size, water)
	flow = raw_input('>> ')
	if flow == "calm" or flow == "moving":
		return flow
	else:
		flow = get_flow()
		return flow


def outfit(w, s, f):
	if w == "salt" and s == "big":
		gear.update({"rod":"10wt 9' Redington Predator", "reel":"Allen Kraken"})
		if f == "calm":
			gear.update({"line":"WF10F", "fly":"Chartreuse gurgler with some flash", "fish":"Juvenile Tarpon"})
		else:
			gear.update({"line":"WF10S", "fly":"Chartreuse over white clouser", "fish":"Monster Striper"})
	elif w == "salt" and s == "small":
		gear.update({"rod":"8wt 7' 10\" TFO Mangrove", "reel":"Lamson Konic II 3.5"})
		if f == "calm":
			gear.update({"line":"WF8F", "fly":"pink crazy charlie", "fish":"spooky bonefish"})
		else:
			gear.update({"line":"WF8I", "fly":"blue over white deceiver with some crystal flash", "fish":"Hungry Striper"})
	elif w == "fresh" and s == "big":
		gear.update({"rod":"7wt 9' Blue Halo glass", "reel":"Redington Zero 3"})
		if f == "calm":
			gear.update({"line":"WF7F", "fly":"green foam frog popper", "fish":"Beautiful Peacock Bass"})
		else:
			gear.update({"line":"WF7F with a class III sink tip", "fly":"size 8 olive woolly bugger", "fish":"big buttery brown trout"})
	elif w == "fresh" and s == "small":
		gear.update({"rod":"3wt 7' 6\" Redington Butterstick", "reel":"Ross Flyrise I"})
		if f == "calm":
			gear.update({"line":"DT3F", "fly":"size 12 beige muddler minnow with a gold body", "fish":"angry blue gill"})
		else:
			gear.update({"line":"DT3F", "fly":"size 12 Olive and partridge soft hackle", "fish":"fiesty little brookie"})
	else: 
		print "borked"
	print "You're throwing a %s rod lined up with %s spooled on a %s. \nAnd I tied on a %s for ya." % (gear['rod'], gear['line'], gear['reel'], gear['fly'])


water = get_water()
size = get_size()
flow = get_flow()
	
print "Gnarly, let's go crush some %s, %s, %swater!\nHere's the gear I've supplied for you: \n" % (size, flow, water)

outfit(water, size, flow)	

# create function to cast
# set chances of success using randint or randrange


chance = {
	0:"you caught a %s" % gear['fish'],
	1:"got a bite, but couldn't set the hook",
	2:"shitty cast",
	3:"you lined it!",
	4:"he broke you off!",
	5:"snagged",
	6:"the wind really picked up",
	7:"That was a monster! he broke your %s" % gear['rod']
	}

def cast(c):
	i = randint(0,7)
	result = c[i]
	print result
	if result == c[0]:
		print "gnarly! you win"
	elif result == c[7]:
		print "That sucks, gotta head back in :("
	else:
		print "Hit enter to cast again"
		raw_input('>>')
		cast(chance)

print "\nReady to fish? Hit enter to make your first cast"
raw_input('>>')
cast(chance)
