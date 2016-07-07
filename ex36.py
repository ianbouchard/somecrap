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
		gear.update({"rod":"10wt 9' Redington Predator"})
		gear.update({"reel":"Allen Kraken"})
		if f == "calm":
			gear.update({"line":"WF10F"})
			gear.update({"fly":"Chartreuse gurgler with some flash"})
		else:
			gear.update({"line":"WF10S"})
			gear.update({"fly":"Chartreuse over white clouser"})
	elif w == "salt" and s == "small":
		gear.update({"rod":"8wt 7' 10\" TFO Mangrove"})
		gear.update({"reel":"Lamson Konic II 3.5"})
		if f == "calm":
			gear.update({"line":"WF8F"})
			gear.update({"fly":"tan crab pattern"})
		else:
			gear.update({"line":"WF8I"})
			gear.update({"fly":"blue over white deceiver"})
	elif w == "fresh" and s == "big":
		gear.update({"rod":"7wt 9' Blue Halo glass"})
		gear.update({"reel":"Redington Zero 3"})
		if f == "calm":
			gear.update({"line":"WF7F"})
			gear.update({"fly":"green foam frog popper"})
		else:
			gear.update({"line":"WF6F with a class III sink tip"})
			gear.update({"fly":"size 6 olive wooly bugger"})
	elif w == "fresh" and s == "small":
		gear.update({"rod":"3wt 7' 6\" Redington Butterstick"})
		gear.update({"reel":"Ross Flyrise I"})
		if f == "calm":
			gear.update({"line":"DT3F"})
			gear.update({"fly":"size 12 beige muddler minnow with a gold body"})
		else:
			gear.update({"line":"DT3F"})
			gear.update({"fly":"size 12 Olive and partridge soft hackle"})
	else: 
		print "borked"
	print "You're throwing a %s rod lined up with %s spooled on a %s. And I tied on a %s for ya." % (gear['rod'], gear['line'], gear['reel'], gear['fly'])


water = get_water()
size = get_size()
flow = get_flow()
	
print "Gnarly, let's go crush some %s, %s, %swater!\nHere's the gear I've supplied for you: \n" % (size, flow, water)

outfit(water, size, flow)	

#set chances of success using randrange

print "\nReady? Let's cast"

def cast(g):
	