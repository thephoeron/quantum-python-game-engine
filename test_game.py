#!/usr/bin/env python

#### QPGE Default Game ======================================================================= ####
#### ========================================================================================= ####

#### IMPORTS ================================================================================= ####
#### We import the QPGE library twice, first the entire library, and then all the objects from ####
#### the library, so that we can push new objects to the engine's namespace, override objects  ####
#### already defined in the game engine, and still allow ourselves to refer to every object in ####
#### the engine directly.  It saves a lot of typing, especially as your games grow into full-  ####
#### size adventures.                                                                          ####
#### ========================================================================================= ####

import QPGE
from QPGE import *

#### GAME GLOBALS ============================================================================ ####

# Set the welcome banner
QPGE.banner = u"""
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
|                                                                             |
|    QUANTUM PYTHON GAME ENGINGE v0.4 alpha [[: the default game :]]          |
|    by "the Phoeron" Colin J.E. Lupton                                       |
|                                                                             |
|    Copyright (c) 2012--2013, Studio Six-Ten I.D. Inc.                       |
|    See LICENSE for more information.                                        |
|    http://www.studio-six-ten.com/                                           |
|                                                                             |
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+"""

# Set the welcome text
QPGE.intro = u"""
This is just a small test game to demonstrate the QPGE in action.  If you are
seeing this message, the instantiation of the Game class and default room went
according to plan.

Now it's time to write your own game.  As you can see already, if you've taken
a moment to review the source code, it couldn't be easier!
"""

# If you want to change the default prompt, you can do so here
# QPGE.default_prompt = u"\n[default@prompt]#> "

#### ITEMS =================================================================================== ####

# Describe the in-game items here
random_object_dict = {
	'name': 'random_object',
	'title': u"Random Object",
	'descr': u"""
The Random Object has no discernible shape or purpose.  It is a mighty strange
thing to look upon, nevermind the feeling of dark foreboding it gives you as
you grasp it in your hand.""",
	'location': 'default_room',
}
QPGE.random_object = Item(**random_object_dict)
QPGE.list_of_items.append((random_object_dict['name'],random_object_dict['title'],random_object_dict['descr'],random_object_dict['location'],))

#### CHARACTERS ============================================================================== ####

# Describe your PCs and NPCs here.  Since no multiplayer environment has been defined, only one
# Player Character is necessary

#### ROOMS =================================================================================== ####

# Describe the rooms, their exit paths, and available custom actions here

#### 'default_room'
default_room_dict = {
	'name': 'default_room',
	'title': u"A Default Room",
	'visited': False,
	'descr': u"""
This is the long description of the Default Room. Blah blah blah.""",
	'vdescr': u"""
This is the short description of the Default Room.""",
	'options': u"""
There is a hole you can put your hand inside...""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"locked",
			"Another Room",
			"another_room",
			),
		'east': (
			"east",
			("portal","s"),
			"locked",
			"Another Room",
			"another_room",
			),
		'north': (
			"north",
			("door","s"),
			"locked",
			"Another Room",
			"another_room",
			),
		'south': (
			"south",
			("wormhole","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'kill': {
			'yourself': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("kill","terminate"),
				'subj': "yourself",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "death",
				'new_item': None,
				'descr': u"""
You decide, rather selfishly, to end it all right now instead of quitting out-
right like a normal person.""",
			},
		},
		'put': {
			'hand_in_hole': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S-O",
				'verb': ("put","place","stick"),
				'subj': "hand",
				'dprt': "in",
				'dobj': "hole",
				'iprt': None,
				'iobj': None,
				'rtrn': "",
				'new_item': {
					'item': "golden_nugget",
					'title': "Golden Nugget",
					'descr': u"\n The golden nugget is shiny and pretty, but otherwise apparently useless.",
				},
				'descr': u"""
 You put your hand in the hole and find a golden nugget!""",
			},
		},
	},
}
QPGE.default_room = Room(**default_room_dict)
QPGE.list_of_rooms.append(default_room_dict['name'])

#### 'another_room'
another_room_dict = {
	'name': 'another_room',
	'title': u"Another Default Room",
	'visited': False,
	'descr': u"""
This is the long description of Another Default Room.  It should be somewhat
slightly different than the Default Room.""",
	'vdescr': u"""
This is the short description of Another Default Room.""",
	'options': u"""
You can 'go back' to the Default Room, or ask for 'help'.""",
	'paths': {
		'east': (
			"east",
			("door","s"),
			"unlocked",
			"Default Room",
			"default_room",
			),
	},
	'actions': {
		'kill': {
			'yourself': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("kill"),
				'subj': "yourself",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "death",
				'new_item': None,
				'descr': u"""
You decide, rather selfishly, to end it all right now instead of quitting out-
right like a normal person.""",
			},
		},
		'nail': {
			'nugget_to_wall_with_hammer': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S-O-I",
				'verb': ("nail","numpty"),
				'subj': "golden_nugget",
				'dprt': "to",
				'dobj': "wall",
				'iprt': "with",
				'iobj': "hammer",
				'rtrn': "",
				'new_item': None,
				'descr': u"""
You decide, rather randomly, to nail your golden nugget to the wall with a hammer.""",
			},
		},
	},
}
QPGE.another_room = Room(**another_room_dict)
QPGE.list_of_rooms.append(another_room_dict['name'])

#### Extra Rooms
QPGE.death = Death()
QPGE.quit = Quit()

#### RUN GAME ================================================================================ ####
the_game = Game(QPGE.default_room)
the_game.play()

#### End of File ============================================================================= ####
