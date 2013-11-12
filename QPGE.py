#### ===================================================================== ####
 ##                                                                         ##
 ##   QUANTUM PYTHON GAME ENGINGE v0.4 alpha [[:with default test game:]]   ##
 ##   by "the Phoeron" Colin J.E. Lupton                                    ##
 ##                                                                         ##
 ##   Copyright (c) 2012--2013, Studio Six-Ten I.D. Inc.                    ##
 ##   See LICENSE for more information.                                     ##
 ##   http://www.studio-six-ten.com/                                        ##
 ##                                                                         ##
#### ===================================================================== ####

# TO-DO:
# Re-write engine to be CHARACTER-BASED instead of LOCATION-BASED.
# Should offer more flexibility for the Heuristics, Pathfinding, and Decision
# Matrix

from random import randint
from operator import *
import sys

banner = u"""
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
|                                                                             |
|    QUANTUM PYTHON GAME ENGINGE v0.4 alpha [[:default game:]]                |
|    by "the Phoeron" Colin J.E. Lupton                                       |
|                                                                             |
|    Copyright (c) 2012--2013, Studio Six-Ten I.D. Inc.                       |
|    See LICENSE for more information                                         |
|    http://www.studio-six-ten.com/                                           |
|                                                                             |
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
"""
intro = u"""
This is a test game to demonstrate the QPGE in action.  If you're seeing this 
message, the instantiation of the Game class and default room went according to
plan.
"""

#### Standard Actions ==================================================== ####

standard_actions = {
	'walk': (
		"walk",
		u"\n You can't walk that way.",
		"",
		),
	'go': (
		"go",
		u"\n You can't go that way.",
		"",
		),
	'put': (
		"put",
		u"\n You can't put that there.",
		"",
		),
	'look': (
		"look",
		u"\n You've already seen all there is to see here.  You should move along and do something worthwhile with your time.",
		"",
		),
	'quit': (
		"quit",
		u"",
		"quit",
		),
}

current_room = ''
inventory = []
list_of_rooms = []
list_of_characters = []
list_of_items = []
# ship_location = "Vega b"
# current_room = "research_bay"
is_wearing_spacesuit = False
spacesuit_o2_level = 100

# is_quantum_core_activated = False
# has_admin_access = False

enemy_distance = 100
game_time = 0

#### Common Elements ===================================================== ####

spacer_left = " " * 21
spacer = " " * 15

section_bar = spacer_left + spacer + "----------"
confirm_bar = u"#### ====================== Press ENTER to Continue ====================== ####"

prompt_info = "Move: %s - ED: %s" % (game_time, enemy_distance)
default_prompt = "\n \033[1;31m,=\033[1;30m[" + prompt_info + "]\033[1;31m" + ("=" * 68) + ".\n `=\033[1;30m#> \033[0m"


#### THE PARENT ITEM CLASS =============================================== ####

class Item(object):
	"""
	The 'Item' parent class.

	Items are anything you can pick up, keep in your inventory, or do something with.
	Some actions require items to perform.
	"""
	def __init__(self, **item_dict):
		super(Item, self).__init__()
		self.item_dict = item_dict

	def main(self):
		# global list_of_items

		item = self.item_dict
		name = item['name']
		title = item['title']
		descr = item['descr']
		location = item['location']

		# list_of_items.append(name)


#### THE CHARACTER CLASSES =============================================== ####

class Character(object):
	"""
	The 'Character' parent class.

	Characters are any player, creature, monster, friend, or foe that appears within the game and can move independently through the game world and act on objects like the player can.
	This class only contains properties and functions shared by all characters in the game.  Players and NPCs descend separately from the Character class.
	"""
	def __init__(self, **character_dict):
		super(Character, self).__init__()
		self.character_dict = character_dict
		self.name = character['name']
		self.descr = character['descr']
		self.location = character['location']
		self.inventory = character['inventory']

	def main(self):
		# global list_of_rooms, current_room

		character = self.character_dict
		name = self.name
		descr = self.descr
		location = self.location
		inventory = self.inventory


class NPC(Character):
	"""
	The 'NPC' (Non-Player Character) Class.
	"""

	def npc_look():
		"""
		NPC Character heuristics will go here
		"""
		# First of all the NPC has to check whether the player is in the room
		# if not, then it looks for clues as to where the player might be

	def npc_decision():
		"""
		NPC Character decision tree will go here
		"""
		# NPC uses heuristics from NPC.npc_look() to decide whether it should
		# wait around to gather more evidence, travel elsewhere based on clues,
		# or if it runs into the Player, attack, leave, etc.

	def npc_travel():
		"""
		NPC Character pathfinding will go here
		"""
		# Extending on NPC.npc_decision(), the logic for moving through rooms
		# goes here

	def npc_interaction():
		"""
		NPC and Player interaction will go here
		"""
		# Depending on the decision from NPC.npc_decision(), a number of
		# possible interactions could occur
		# Interactions can be defined on the NPC character similar to special
		# actions in rooms
		# since interactions can easily be broken down into hostile, neutral,
		# or friendly, this naturally maps to Ising problems, and the characters'
		# mood can influence the decision tree

	def npc(self):
		character = self.character_dict
		name = self.name
		descr = self.descr
		location = self.location
		inventory = self.inventory

		# when NPC.npc() is called, it needs to check where it is and look
		# for evidence of player character (whether room is visited or not
		# by player), try to guess which way the player went, and then update
		# the pathfinding algorithm accordingly
		# All of this should use the D-Wave SAPI, since that's the point of this
		# game engine


class Player(Character):
	"""
	The 'Player' Character Class.
	Multiple Player Characters can be instantiated.
	"""
	# This player class is not currently used by the engine
	# A lot of the logic under Room should be moved here

	def player_look(self):
		pass

	def player_action(self):
		pass

	def player_move(self):
		pass

	def player_interaction(self):
		pass

	def player(self):
		character = self.character_dict
		name = self.name
		descr = self.descr
		location = self.location
		inventory = self.inventory
		

#### THE PARENT ROOM CLASS =============================================== ####

class Room(object):
	"""The Base Room Class"""
	def __init__(self, **room_dict):
		super(Room, self).__init__()
		self.room_dict = room_dict

	def main(self):
		global current_room, list_of_items, inventory

		room = self.room_dict
		room_name = room['name']
		room_descr = room['descr']
		room_vdescr = room['vdescr']
		room_opt = room['options']
		paths = room['paths']
		actions = room['actions']
		is_room_visited = room['visited']
		try:
			if room['gravity'] == True:
				gravity = room['gravity']
			elif room['gravity'] == False:
				gravity = room['gravity']
			else:
				pass
		except KeyError:
			room['gravity'] = True
			gravity = room['gravity']

		# list_of_rooms.append(room_name)

		items_str = u""
		paths_str = u""
		local_items_list = []
		for item,title,descr,location in list_of_items:
			if location == room_name:
				local_items_list.append((item,title,descr,))

		# Somewhere in the below code, a check is needed for NPC characters
		# It makes sense if the usual room desription is overshadowed by the
		# presence of an NPC
		if current_room != room_name:
			current_room = room_name

			if is_room_visited == False:
				Say.parser(room_descr)
				room['visited'] = True
			else:
				Say.parser(room_vdescr)

			if gravity == False:
				Say.parser(u"\n There is no gravity here.")
			elif gravity == True:
				Say.parser(u"\n This room has gravity.")
			else:
				pass

			Say.parser(room_opt)

			paths_count = 0
			paths_dump = []
			for p in paths:
				paths_count += 1
				paths_dump.append((str(paths[p][0]),str(paths[p][1][0]),str(paths[p][1][1]),))
				# paths_str += p + ", "

			path_dict = {}
			for (i,j,k,) in paths_dump:
				pd_len = len(paths_dump)
				try:
					if path_dict[str(j)]:
						path_dict[str(j)].append(str(i))
					else:
						pass
				except KeyError:
					path_dict[str(j)] = [(str(j),str(k))]
					path_dict[str(j)].append(str(i))
				
			paths_key_count = 0
			for key in path_dict:
				paths_key_count += 1
				if len(path_dict[key]) == 2 and paths_key_count == 1:
					paths_str += "is "
				elif len(path_dict[key]) >= 3 and paths_key_count == 1:
					paths_str += "are "
				else:
					pass
				if len(path_dict[key]) == 2:
					paths_str += "a " + path_dict[key][0][0] + " leading " + path_dict[key][1]
				elif len(path_dict[key]) >= 3:
					paths_str += path_dict[key][0][0] + path_dict[key][0][1] + " leading "
					for value in path_dict[key]:
						ind = path_dict[key].index(value)
						if ind == 0:
							pass
						elif ind == len(path_dict[key]) - 1:
							paths_str += "and " + path_dict[key][ind] + ""
						elif (ind >= 2 and ind < len(path_dict[key]) - 1) or (ind == 1 and len(path_dict[key]) >= 2):
							paths_str += path_dict[key][ind] + ", "
						elif ind == 1:
							paths_str += path_dict[key][ind] + " "
						else:
							pass
				else:
					pass
				if len(path_dict) >= 2 and paths_key_count == len(path_dict) - 1:
					paths_str += ", and "
				elif len(path_dict) >= 2 and paths_key_count < len(path_dict) - 1:
					paths_str += ", "
				else:
					paths_str += ""
					
					# if paths_count == 1:
					# 	paths_str += i + " "
					# elif paths_count == 2 and paths_dump.index(i) == 0:
					# 	paths_str += i + " "
					# elif paths_dump.index(i) == pd_len - 1:
					# 	paths_str += "and " + i + " "
					# elif paths_dump.index(i) < pd_len - 1:
					# 	paths_str += i + ", "
					# else:
					# 	pass

			if paths_str != u"":
				# print u"\n There " + paths_str + " from here."
				the_paths_str = u"\n There " + paths_str + u" from here."
				Say.parser(the_paths_str)
			elif paths_str == u"":
				# print u"\n There seems to be no way out of this room..."
				pass
			else:
				print u"\n Something went wrong with path paragraph generation.\n DEBUG INFO: 'paths_str' == " + paths_str + " ; 'paths_dump' == " + str(paths_dump) + " ; 'paths_count' == " + str(paths_count) + " ; 'len(paths_dump)' == " + str(len(paths_dump)) + " ; "

			for i,j,k in local_items_list:
				if len(local_items_list) >= 2 and local_items_list.index((i,j,k)) == len(local_items_list) - 1:
					items_str += "and " + j + " "
				elif local_items_list.index((i,j,k)) < len(local_items_list) - 1:
					items_str += j + ", "
				else:
					items_str += j + " "

			if len(local_items_list) >= 1:
				the_items_str = "\n There is a " + items_str + "here."
				Say.parser(the_items_str)
			# elif len(local_items_list) == 1:
			# 	print "\n There is a " + items_str + "here."
			else:
				pass

		command = raw_input(default_prompt)
		for i,j,k in inventory:
			command = command.replace(j, i)
		for i,j,k in local_items_list:
			command = command.replace(j, i)

		cmd_tokens = command.split(" ")

		#### Debug line; uncomment to echo parsed command back to terminal.
		# print "You entered the command: " + command + " and it was parsed as: " + str(cmd_tokens)
		cmd_dump = []
		for token in cmd_tokens:
			# particles = ['an', 'a', 'the', 'your', 'my', 'in', 'to', 'at']
			if token == 'an' or token == 'a' or token == 'the':
				pass
			elif token == 'your' or token == 'yours' or token == 'my' or token == 'mine':
				pass
			# elif token == 'in' or token == 'on' or token == 'to' or token == 'at':
			# 	pass
			# elif token == 'onto' or token == 'into' or token == 'inside' or token == 'under':
			# 	pass
			else:
				cmd_dump.append(token)

		is_action_successful = False

		while is_action_successful is False:
			# Check command for actions on objects first
			if cmd_dump[0] == 'look' and len(cmd_dump) >= 2:
				for i,j,k in inventory:
					if cmd_dump[1] == i or cmd_dump[1] == j:
						Say.parser(k)
						is_action_successful = True
						return eval(current_room)
				for i,j,k in local_items_list:
					if cmd_dump[1] == i or cmd_dump[1] == j:
						Say.parser(k)
						is_action_successful = True
						return eval(current_room)
					else:
						pass
				look_error_str = u"\n You don't see that here."
				Say.parser(look_error_str)
				return eval(current_room)
			elif (cmd_dump[0] == 'take' or cmd_dump[0] == 'pickup') and len(cmd_dump) >= 2:
				for item,title,descr in local_items_list:
					if cmd_dump[1] == item or cmd_dump[1] == title:
						take_str = u"\n You take the " + title + "."
						Say.parser(take_str)
						inventory.append((item,title,descr))
						# local_items_list[:] = [(x,y,z) for x,y,z in local_items_list if tuple((item,title,descr))]
						list_of_items[:] = [(w,x,y,z,) for w,x,y,z in list_of_items if not eq((w,x,y,z),(item,title,descr,location,))]
						is_action_successful = True
						return eval(current_room)
					else:
						pass
				take_error_str = u"\n That item doesn't appear to be here."
				Say.parser(take_error_str)
				return eval(current_room)
			elif cmd_dump[0] == 'drop' and len(cmd_dump) >= 2:
				for i,j,k in inventory:
					if cmd_dump[1] == i or cmd_dump[1] == j:
						drop_str = u"\n You drop the " + j + "."
						Say.parser(drop_str)
						list_of_items.append((i,j,k,current_room))
						# local_items_list.append((i,j,k))
						inventory[:] = [(x,y,z,) for x,y,z in inventory if not eq((x,y,z,),(i,j,k,))]
						is_action_successful = True
						return eval(current_room)
					else:
						pass
				drop_error_str = u"\n You don't have that item."
				Say.parser(drop_error_str)
				return eval(current_room)
			elif cmd_dump[0] == 'inventory':
				inv_str = u"\n You are carrying "
				if len(inventory) == 0:
					inv_str += "nothing."
				for i,j,k in inventory:
					if inventory.index((i,j,k)) == 0 and len(inventory) > 1:
						j_str = "a " + j + ", "
						inv_str += j_str
					elif inventory.index((i,j,k)) == len(inventory) - 1 and len(inventory) > 1:
						j_str = "and a " + j + "."
						inv_str += j_str
					elif inventory.index((i,j,k)) < len(inventory) - 1 and len(inventory) > 1:
						j_str = "a " + j + ", "
						inv_str += j_str
					else:
						j_str = "a " + j + "."
						inv_str += j_str

				Say.parser(inv_str)
				is_action_successful = True
				return eval(current_room)
			# Now check for rooms you can travel to
			elif (cmd_dump[0] == 'go' or cmd_dump[0] == 'travel' or cmd_dump[0] == 'walk') and len(cmd_dump) >= 2:
				if gravity == False and cmd_dump[0] == 'walk':
					grav_str = u"\n You can't walk in microgravity..."
					Say.parser(grav_str)
					is_action_successful = True
					return eval(current_room)
				else:
					pass
				for p in paths:
					if cmd_dump[1] == paths[p][0] and paths[p][2] == "locked":
						go_str = u"\n You can't %s that way -- the %s appears to be locked." % (cmd_dump[0], paths[p][1][0])
						Say.parser(go_str)
						is_action_successful = True
						return eval(current_room)
					elif cmd_dump[1] == paths[p][0] and paths[p][2] == "unlocked":
						go_str = u"\n You %s %s through the %s to %s." % (cmd_dump[0], paths[p][0], paths[p][1][0], paths[p][3])
						Say.parser(go_str)
						is_action_successful = True
						return eval(paths[p][4])
					else:
						pass
				go_error_str = u"\n You can't %s that way." % cmd_dump[0]
				Say.parser(go_error_str)
				return eval(current_room)
			else:
				# NEW! -- Check Action Dict for Advanced Actions and Run
				for action in actions:
					for act in actions[action]:
						the_act = actions[action][act]
						act_type = the_act['type']
						act_verb = the_act['verb']
						act_descr = the_act['descr']
						act_rtrn = the_act['rtrn']
						for v in act_verb:
							# print v
							if cmd_dump[0] == v:
								if len(cmd_dump) == 2 and act_type == "V-S":
									if cmd_dump[1] == the_act['subj']:
										Say.parser(act_descr)
										is_action_successful = True
										if act_rtrn != "":
											return eval(act_rtrn)
										else:
											return eval(current_room)
									else:
										pass
									action_error_str = "There was an error with your V-S command: \'" + str(cmd_dump) + "\'"
									Say.parser(action_error_str)
									return eval(current_room)
								elif len(cmd_dump) == 4 and act_type == "V-S-O":
									if cmd_dump[1] == the_act['subj'] and cmd_dump[2] == the_act['dprt'] and cmd_dump[3] == the_act['dobj']:
										if the_act['new_item'] != None:
											new_item = the_act['new_item']
											for i,j,k in inventory:
												if i == the_act['subj']:
													inventory[:] = [(x,y,z,) for x,y,z in inventory if not eq((x,y,z,),(i,j,k,))]
												if i == the_act['dobj']:
													inventory[:] = [(x,y,z,) for x,y,z in inventory if not eq((x,y,z,),(i,j,k,))]
											inventory.append((new_item['item'],new_item['title'],new_item['descr']))
										else:
											pass
										Say.parser(act_descr)
										is_action_successful = True
										if act_rtrn != "":
											return eval(act_rtrn)
										else:
											return eval(current_room)
									else:
										pass
									action_error_str = "There was an error with your V-S-O command: \'" + str(cmd_dump) + "\'"
									Say.parser(action_error_str)
									return eval(current_room)
								elif len(cmd_dump) == 6 and act_type == "V-S-O-I":
									if cmd_dump[1] == the_act['subj'] and\
									   cmd_dump[2] == the_act['dprt'] and\
									   cmd_dump[3] == the_act['dobj'] and\
									   cmd_dump[4] == the_act['iprt'] and\
									   cmd_dump[5] == the_act['iobj']:
										if the_act['new_item'] != None:
											new_item = the_act['new_item']
											for i,j,k in inventory:
												if i == the_act['subj']:
													inventory[:] = [(x,y,z,) for x,y,z in inventory if not eq((x,y,z,),(i,j,k,))]
												if i == the_act['dobj']:
													inventory[:] = [(x,y,z,) for x,y,z in inventory if not eq((x,y,z,),(i,j,k,))]
												if i == the_act['iobj']:
													inventory[:] = [(x,y,z,) for x,y,z in inventory if not eq((x,y,z,),(i,j,k,))]
											inventory.append((new_item['item'],new_item['title'],new_item['descr']))
										else:
											pass
										Say.parser(act_descr)
										is_action_successful = True
										if act_rtrn != "":
											return eval(act_rtrn)
										else:
											return eval(current_room)
									action_error_str = "There was an error with your V-S-O-I command: \'" + str(cmd_dump) + "\'"
									Say.parser(action_error_str)
									return eval(current_room)
								else:
									pass
							else:
								pass
								# print u"\n I can't seem to find that verb in the action dictionary..."
								# return eval(current_room)
				# Check Action Dict for Command and Run
				# for action in actions:
				# 	if command == actions[action][0]:
				# 		print actions[action][1]
				# 		is_action_successful = True
				# 		return eval(actions[action][2])
				# 	else:
				# 		pass
				# If Command Not in Action Dict, Try Standard Actions
				for action in standard_actions:
					if cmd_tokens[0] == standard_actions[action][0]:
						Say.parser(standard_actions[action][1])
						is_action_successful = True
						if standard_actions[action][2] != "":
							return eval(standard_actions[action][2])
						else:
							return eval(current_room)
					else:
						pass
				# If All Else Fails, Complain and Return to Room
				action_str = u"\n That is not an option."
				Say.parser(action_str)
				return eval(current_room)


class Victory(Room):
	"""
	The 'Victory' Room.  Inherits from parent Room class.
	Should only be called from actions which are meant to lead to the succesful completion of the game.
	"""

	def __init__(self):
		self.quips = [
			u"Victory is... yours!",
			u"What do you know? I didn't see that coming.",
			u"Wow, you actually beat me... you actually, actually beat me...",
		]

	def main(self):
		victory_str = u"\n " + self.quips[randint(0, len(self.quips)-1)]
		victory_str2 = u"\n In other words, you've won!  Give yourself a big pat on the back, thanks for playing."
		Say.parser(victory_str)
		Say.parser(victory_str2)
		sys.exit(0)


class Death(Room):
	"""
	The 'Death' Room.  Inherits from parent Room Class.
	Prints a random funny message/quote after the terminal action is complete.
	Should be customized to allow restarting game without exiting.
	"""

	def __init__(self):
		self.quips = [
			u"As the saying goes, \"GAME OVER!\"",
			u"\"The failure is all your own.\"",
			u"\"Life is but a walking shadow...\"",
			u"\"You leave this world with naught but regret.\"",
			u"\"Did you leave the kettle on?\"",
			u"\"Tomorrow would be better if there would be a tomorrow for you.\"",
		]

	def main(self):
		death_str = u"\n " + self.quips[randint(0, len(self.quips)-1)]
		death_str2 = u"\n In other words, you're dead.  Thanks for playing."
		Say.parser(death_str)
		Say.parser(death_str2)
		sys.exit(1)


class Quit(Room):
	"""
	The 'Quit' Room.  Inherits from parent Room Class.
	Displays a single message thanking the user for playing.  Could be extended to display a random funny quote like the Death Room, only positive instead of scolding?
	Should be customized to perform any clean wrap-up functions, saving game, etc.
	"""
	def __init__(self):
		self.quips = [
			u"You were a mighty opponent.  No really, I'm not being cheeky.",
			u"What's the matter? You run out of time, little girl?",
			u"I don't think you meant to do that.  Now you'll have to start over from the... beginning!!! Mwahahahaaaaaa!",
			u"Seriously?!",
			u"You're a real numpty.  Just sayin\'.",
		]

	def main(self):
		quit_str = " " + self.quips[randint(0, len(self.quips)-1)]
		quit_str2 = u"\n Thanks for playing."
		Say.parser(quit_str)
		Say.parser(quit_str2)
		sys.exit(0)


#### MAIN INTERFACE AND GAME LOOP CLASSES ================================ ####

class Map(object):
	"""
	Game Map Generator class.

	Takes the global list_of_rooms and generates a node--connection graph for the AI.
	"""

	def __init__(self, rooms=list_of_rooms):
		self.list_of_rooms = rooms

	def main(self):
		list_of_rooms = self.list_of_rooms

		for room in list_of_rooms:
			room_name = eval(room)
			the_room = getattr(room_name, "main")
			paths = the_room.paths

			for path in paths:
				the_path = paths[path]
				path_dir = the_path[0]
				path_typ = the_path[1]
				path_lck = the_path[2]
				path_dsc = the_path[3]
				path_dst = the_path[4]


class Say(object):
	"""
	Text processor class.

	Takes input string, formats it according to screen and interface properties, and sends it to
	the appropriate view.
	"""

	# def __init__(self, input_string):
	# 	self.input_string = input_string

	def parser(self, input_string):
		# input_string = self.input_string
		par_width = 92

		word_list = input_string.split(" ")
		new_par = u""
		new_par_lines = []
		new_line = u""
		for word in word_list:
			if word == "\n" or word == "\n\n":
				# new_line += u"\n"
				new_par_lines.append(new_line)
				new_line = u""
			elif (len(new_line) + len(word)) <= par_width and word_list.index(word) < len(word_list) - 1:
				new_line += word + " "
			elif word_list.index(word) == len(word_list) - 1:
				new_line += word
				new_par_lines.append(new_line)
				new_line = u""
			elif (len(new_line) + len(word)) > par_width:
				new_par_lines.append(new_line)
				new_line = word + " "
			else:
				new_line += word + ""
				new_par_lines.append(new_line)

		for line in new_par_lines:
			if new_par_lines.index(line) < len(new_par_lines) - 1:
				new_par += line + "\n "
			else:
				new_par += line

		print new_par
		# print " DEBUG: word_list = \'" + str(word_list) + "\'"
		# print " DEBUG: new_par_lines = \'" + str(new_par_lines) + "\'"
		# print " DEBUG: len(new_line) = \'" + str(len(new_line)) + "\'"


class Game(object):
	"""
	The primary game loop class.
	
	init: Accepts an instantiated room variable as a string, and allows for an alternate 'start
	      function' to be specified instead of 'main', so that sub-rooms can be defined in a child
	      class of 'Room'.
	play: Prints Game Banner and Intro on launch, loads 'start room', then runs the game in the
	      while loop.
	"""

	def __init__(self, room_class, start_function='main'):
		self.room_class = room_class
		self.start_function = start_function


	def play(self):
		print banner
		print intro

		action = raw_input(confirm_bar)

		# room_str = u""
		# for room in list_of_rooms:
		# 	if room == None:
		# 		room_str += "."
		# 	else:
		# 		room_str += room + ", "
		# room_str.replace(", .", ".")

		# print "List of Rooms: " + room_str
		# print "List of Items: " + str(list_of_items)
		# print "List of Characters: " + str(list_of_characters)

		next_room_class = self.room_class
		next_room_name = self.start_function

		# NPC characters will have to be told to make their move here,
		# and update their location before the player enters the room, so 
		# they don't accidentally pass each other (which would be a bug)
		while True:
			room = getattr(next_room_class, next_room_name)
			next_room_class = room()

			global game_time, enemy_distance, prompt_info, default_prompt
			game_time += 1
			enemy_distance -= 1
			prompt_info = "Move: %s - ED: %s" % (game_time, enemy_distance)
			default_prompt = "\n \033[1;31m,=\033[1;30m[" + prompt_info + "]\033[1;31m" + ("=" * 68) + ".\n `=\033[1;30m#> \033[0m"
			

Say = Say()
# default_room = Room(**default_room_dict)
# another_room = Room(**another_room_dict)
# death = Death()
# quit = Quit()
# the_game = Game(default_room)
# the_game.play()

#### End of File ========================================================= ####
