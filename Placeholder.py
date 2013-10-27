#!/usr/bin/env python

#### PLACEHOLDER: Powered by QPGE ============================================================ ####
#### A full adventure based on the novel by the Phoeron, to show off all the features of QPGE. ####
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

QPGE.banner = u"""\033[1;31m
 #### ================================================================================ ####
 \033[1;30m
     dP dP   "8e     eeeee e     eeeee eeee eeee e   e eeeee e     eeeee eeeee eeeee       
  8888888888   "8e   8   8 8     8   8 8  8 8    8   8 8  88 8     8   8 8     8   8       
    dP dP        e8" 8eee8 8e    8eee8 8e   8eee 8eee8 8   8 8e    8e  8 8eee  8eee8e      
 8888888888    e8"   88    88    88  8 88   88   88  8 8   8 88    88  8 88    88   8      
   dP dP     e8"     88    88eee 88  8 88e8 88ee 88  8 8eee8 88eee 88ee8 88eee 88   8 eeeee
 \033[1;31m
 #### ====== (c) 2012--2013 THEPHOERON.COM -- BASED ON THE NOVEL BY THE PHOERON ====== ####
 ##                                                                                      ##
 #### ============= Powered by QPGE v0.4: http://qpge.studio-six-ten.com ============= ####\033[0m"""

QPGE.intro = u"""
 You awake to find yourself floating in mid-air, slowly spinning in position, and for a
 moment, you can't remember where you are, or how you got there -- but you seem to be in
 space.
 
 There is something written on the far wall; with some effort, you move your body over
 itself and glide towards the centre of the room from where you can just make out the
 words."""

QPGE.confirm_bar = u"""\033[1;31m
 #### =========================== Press RETURN to Continue =========================== ####\033[0m"""

#### Uncomment these if you want to change them
# QPGE.enemy_distance = 100
# QPGE.game_time = 0
# QPGE.is_wearing_spacesuit = False
# QPGE.spacesuit_o2_level = 100

#### Uncomment these if you want to activate them
# QPGE.ship_location = "Vega b"
# QPGE.is_quantum_core_activated = False
# QPGE.has_admin_access = False

# QPGE.default_prompt = u"\n[default@prompt]#> "

#### ITEMS =================================================================================== ####

#### Random Object --- Item Template
# random_object_dict = {
# 	'name': 'random_object',
# 	'title': u"Random Object",
# 	'descr': u"""
# The Random Object has no discernible shape or purpose.  It is a mighty strange
# thing to look upon, nevermind the feeling of dark foreboding it gives you as
# you grasp it in your hand.""",
# 	'location': 'default_room',
# }
# QPGE.random_object = Item(**random_object_dict)
# QPGE.list_of_items.append((random_object_dict['name'],random_object_dict['title'],random_object_dict['descr'],random_object_dict['location'],))

#### Micrograv-friendly marker
micrograv_marker_dict = {
	'name': 'micrograv_marker',
	'title': u"Micrograv Marker",
	'descr': u"""
A standard-issue micrograv-friendly marker for manually marking surfaces that do not interact with neural-interfaces.""",
	'location': 'storage_alpha',
}
QPGE.micrograv_marker = Item(**micrograv_marker_dict)
QPGE.list_of_items.append((micrograv_marker_dict['name'],micrograv_marker_dict['title'],micrograv_marker_dict['descr'],micrograv_marker_dict['location'],))

#### Coffee pod
coffee_pod_dict = {
	'name': 'coffee_pod',
	'title': u"Coffee Pod",
	'descr': u"""
 Your average, sawdust and floor-sweeping flavoured brown caffeinated source pouch for use with a micrograv hot-beverage combined single-serving brewer and drinking pouch.  You've suspected for a long time that it doesn't have any real coffee in it at all.""",
	'location': 'storage_beta',
}
QPGE.coffee_pod = Item(**coffee_pod_dict)
QPGE.list_of_items.append((coffee_pod_dict['name'],coffee_pod_dict['title'],coffee_pod_dict['descr'],coffee_pod_dict['location'],))

#### Brewing Pouch
brew_pouch_dict = {
	'name': 'brew_pouch',
	'title': u"Micrograv Brew Pouch",
	'descr': u"""
A standard-issue micrograv hot-beverage single-serving combined brewer and drinking pouch, for use with recylable beverave pods.  You need to attach it to a water source to use it.""",
	'location': 'storage_beta',
}
QPGE.brew_pouch = Item(**brew_pouch_dict)
QPGE.list_of_items.append((brew_pouch_dict['name'],brew_pouch_dict['title'],brew_pouch_dict['descr'],brew_pouch_dict['location'],))

#### Vorkrieg-era Datapad
datapad_dict = {
	'name': 'datapad',
	'title': u"Vorkrieg-era Datapad",
	'descr': u"""
An ancient-looking, but well-preserved electronic artifact from the Pre-War era.  It appears to have a touch-enabled screen, and does not respond to commands from your neuro-interface.""",
	'location': 'sec_o_beta_b',
}
QPGE.datapad = Item(**datapad_dict)
QPGE.list_of_items.append((datapad_dict['name'],datapad_dict['title'],datapad_dict['descr'],datapad_dict['location']))

#### Fuzzbomb
fuzzbomb_dict = {
	'name': 'fuzzbomb',
	'title': u"'Fuzzbomb' WMD",
	'descr': u"""
The menacing bulk of the ultimate weapon terrifies you, despite the somewhat gentle and humorous name.  This bomb was designed to create a singularity and destroy an entire star system.""",
	'location': 'ordo_ars_toroid',
}
QPGE.fuzzbomb = Item(**fuzzbomb_dict)
QPGE.list_of_items.append((fuzzbomb_dict['name'],fuzzbomb_dict['title'],fuzzbomb_dict['descr'],fuzzbomb_dict['location']))

#### CHARACTERS ============================================================================== ####

#### ROOMS =================================================================================== ####

#### Default Room --- Room Template
# default_room_dict = {
# 	'name': 'default_room',
# 	'title': u"Default Room",
# 	'visited': False,
#	'gravity': False,
# 	'descr': u"""
# This is the long description of the Default Room. Blah blah blah.""",
# 	'vdescr': u"""
# This is the short description of the Default Room.""",
# 	'options': u"""
# You can 'wander off', 'kill yourself', or cry for 'help'.""",
# 	'paths': {
# 		'west': (
# 			"west",
# 			("door","s"),
# 			"Another Room",
# 			"another_room",
# 			),
# 		'east': (
# 			"east",
# 			("portal","s"),
# 			"Another Room",
# 			"another_room",
# 			),
# 	},
# 	'actions': {
# 		'help': (
# 			"help",
# 			u"""
# You need to cheat already?  Didn't you see the room's options?""",
# 			"default_room",
# 			),
# 		'kill_yourself': (
# 			"kill yourself",
# 			u"""
# You decide, rather selfishly, to end it all right now instead of quitting out-
# right like a normal person.""",
# 			"death",
# 			),
# 	},
# }
# QPGE.default_room = Room(**default_room_dict)
# QPGE.list_of_rooms.append(default_room_dict['name'])

#### SFS Fulgora ============================================================================= ####

#### Research Bay
research_bay_dict = {
	'name': 'research_bay',
	'title': u"Research Bay",
	'visited': False,
	'gravity': False,
	'descr': u"""
 You are in a long, brightly lit compartment.  The walls are covered in computer terminals and standard-issue, micrograv lab equipment.  A narrow strip of bulkhead in the middle of the compartment appears to be rotating.  A sign says you are in the Research Bay, in the central axis of the SFS Fulgora.  Under the sign is a cartesian plot and a map of the ship.""",
	'vdescr': u"""
 You are in Sec R: Research Bay, in the central axis of the SFS Fulgora.  It is long and brightly lit, and the walls are covered in computer terminals and standard-issue, micrograv lab equipment.  There is a rotating strip of bulkhead in the middle of the room.""",
	'options': u"""
 There is a terminal you can use.  There also seems to be a small hole in the padding along the edge of the rotating section, just large enough to put your hand inside.""",
	'paths': {
		'north': (
			"north",
			("porthole","s"),
			"unlocked",
			u"Junction O alpha/beta",
			"jn_o_alpha_beta",
			),
		'east': (
			"east",
			("porthole","s"),
			"locked",
			u"Junction O zeta/eta",
			"jn_o_zeta_eta",
			),
		'south': (
			"south",
			("porthole","s"),
			"locked",
			u"Junction O theta/iota",
			"jn_o_theta_iota",
			),
		'west': (
			"west",
			("porthole","s"),
			"locked",
			u"Junction O nu/xi",
			"jn_o_nu_xi"
			),
		'above': (
			"above",
			("hatch","es"),
			"unlocked",
			u"Sec F: Flight Deck",
			"flight_deck",
			),
		'below': (
			"below",
			("hatch","es"),
			"locked",
			u"Sec L: Research Lab",
			"research_lab",
			),
		'forward': (
			"forward",
			("hatch","es"),
			"unlocked",
			u"Sec C alpha: Corridor (Central Axis -- Forward)",
			"corridor_alpha",
			),
		'aft': (
			"aft",
			("hatch","es"),
			"unlocked",
			u"Sec C beta: Corridor (Central Axis -- Medical/Engineering)",
			"corridor_beta",
			),
		'port': (
			"port",
			("hatch","es"),
			"locked",
			u"Sec S alpha: Storage (Utilities)",
			"storage_alpha",
			),
		'starboard': (
			"starboard",
			("hatch","es"),
			"locked",
			u"Sec S beta: Storage (Micrograv Galley)",
			"storage_beta",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use","uses"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""
 You decide to use the Research Bay Terminal.""",
			},
		},
		'put': {
			'hand_in_hole': {
				'type': "V-S-O",
				'verb': ("put", "place", "stick"),
				'subj': "hand",
				'dprt': "in",
				'dobj': "hole",
				'rtrn': "death",
				'new_item': None,
				'descr': u"""
 You decide to put your hand in the hole along the rotating bulkhead.""",
			}
		},
	},
}
QPGE.research_bay = Room(**research_bay_dict)
QPGE.list_of_rooms.append(research_bay_dict['name'])

#### Research Bay Terminal
research_bay_terminal_dict = {
	'name': 'research_bay_terminal',
	'title': u"Research Lab",
	'visited': False,
	'gravity': False,
	'descr': u"""
 You are holding a standard SFAF Terminal in your hands.  It is controlled via neuro-interface.""",
	'vdescr': u"""
 You try the SFAF Terminal again.  You know that it is controlled via neuro-interface, but that seems to be all you can remember.""",
	'options': u"""
 The terminal appears to be working, but you can't remember your login and password.""",
	'paths': {
		# 'back': (
		# 	"back",
		# 	("exit","s"),
		#	"unlocked",
		# 	"Research Bay",
		# 	"research_bay",
		# 	),
	},
	'actions': {
		'exit': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("exit","leave","logout"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay",
				'new_item': None,
				'descr': u"""
 You replace the terminal screen in its dock and return your attention to the Research Bay.""",
			},
		},
		'throw': {
			'terminal': {
				'type': "V-S",
				'verb': ("throw","toss","pitch"),
				'subj': "terminal",
				'rtrn': "death",
				'descr': u"""
 Out of frustration, you throw the terminal screen as hard as you can against the wall of the Research Bay, but the sturdy metaglass screen doesn't even chip.

 But the terminal screen ricochets around the Research Bay until you realize it's flying directly for your head.  You can't move away in micrograv fast enough, and the corner of it strikes you square in the temple...""",
			},
		},
	},
}
QPGE.research_bay_terminal = Room(**research_bay_terminal_dict)
QPGE.list_of_rooms.append(research_bay_terminal_dict['name'])

#### Flight Deck
flight_deck_dict = {
	'name': 'flight_deck',
	'title': u"Sec F: Flight Deck",
	'visited': False,
	'gravity': False,
	'descr': u"""
 The red glow of the Flight Deck comforts you, but after quick investigation, you find that the terminals all require logins.  You can't remember yours.  The crescent of a planet is barely visible through the metaglass viewport.""",
	'vdescr': u"""
 You are in Sec F: Flight Deck.  You still can't remember your login for the terminals.  The crescent of a planet is barely visible through the metaglass viewport.""",
	'options': u"""
 Since you can't remember your login info, there appears to be nothing to do here.""",
	'paths': {
		'below': (
			"below",
			("hatch","es"),
			"unlocked",
			"Sec R: Research Bay",
			"research_bay",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.flight_deck = Room(**flight_deck_dict)
QPGE.list_of_rooms.append(flight_deck_dict['name'])

#### Research Lab
research_lab_dict = {
	'name': 'research_lab',
	'title': u"Sec L: Research Lab",
	'visited': False,
	'gravity': False,
	'descr': u"""
 Maj Jeanville's lab smells musty and unused.  Half-eaten remains of a dozen or more meals lay rotten and scattered all over the lab.  The room is dominated by a powerful supercomputer and many large screens, although there is also a wide variety of equipment and samples.""",
	'vdescr': u"""
 You are in 'Sec L: Research Lab,' and it smells musty and neglected.  Half-eaten remains of a dozen or more meals lay rotten and scattered all over the lab.  The room is dominated by a powerful supercomputer and many large screens, but also contains a wide variety of equipment and samples.""",
	'options': u"""
 There is a supercomputer you can use here, but you might want to clean up first.""",
	'paths': {
		'above': (
			"above",
			("hatch","es"),
			"unlocked",
			"Sec R: Research Bay",
			"research_bay",
			),
		'below': (
			"below",
			("hatch","es"),
			"locked",
			"Sec C zeta: Corridor (Counterweight Maintenance)",
			"corridor_zeta",
			),
	},
	'actions': {
		'use': {
			'supercomputer': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use","access"),
				'subj': "supercomputer",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_lab_supercomputer",
				'new_item': None,
				'descr': u"""
 You decide to use Maj Jeanville's supercomputer.""",
			},
		},
	},
}
QPGE.research_lab = Room(**research_lab_dict)
QPGE.list_of_rooms.append(research_lab_dict['name'])

#### Corridor Zeta: Counterweight Maintenance Access
corridor_zeta_dict = {
	'name': 'corridor_zeta',
	'title': u"Sec C zeta: Corridor (Counterweight Maintenance)",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'above': (
			"above",
			("hatch","es"),
			"unlocked",
			"Sec L: Research Lab",
			"research_lab",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use","access"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "counterweight_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.corridor_zeta = Room(**corridor_zeta_dict)
QPGE.list_of_rooms.append(corridor_zeta_dict['name'])

#### Ordo A.R.S. Toroidal Chamber
ordo_ars_toroid_dict = {
	'name': 'ordo_ars_toroid',
	'title': u"Sec Omega: Ordo A.R.S. Toroid",
	'visited': False,
	'gravity': True,
	'descr': u"""
 You are in a strange toroidal chamber that seems to loop around the counterweight maintenance access tunnel.  The eerie blue light and locally-contained gravitational field, combined with the fact that it was so carefully hidden beneath Maj Jeanville's lab, suggests that you aren't supposed to be here.""",
	'vdescr': u"""
 You are in 'Sec Omega: Ordo A.R.S. Toroid,' a chamber hidden as part of the counterweight systems that doesn't appear on any map of the SFS Fulgora.  It's pretty clear that you aren't supposed to be here.""",
	'options': u"""
 There is a terminal here you can use.""",
	'paths': {
		'out': (
			"out",
			("airlock","s"),
			"unlocked",
			"Sec C zeta: Corridor (Counterweight Maintenance)",
			"corridor_zeta",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use","access"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "ordo_ars_terminal",
				'new_item': None,
				'descr': u"""
 You decide to use the Ordo A.R.S. Terminal.""",
			},
		},
	},
}
QPGE.ordo_ars_toroid = Room(**ordo_ars_toroid_dict)
QPGE.list_of_rooms.append(ordo_ars_toroid_dict['name'])

#### Ordo A.R.S. Terminal
ordo_ars_terminal_dict = {
	'name': 'ordo_ars_terminal',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		# 'west': (
		# 	"west",
		# 	("door","s"),
		# 	"unlocked",
		# 	"Another Room",
		# 	"another_room",
		# 	),
	},
	'actions': {
		'exit': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("exit","leave"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "ordo_ars_toroid",
				'new_item': None,
				'descr': u"""
You decide to exit the Ordo A.R.S. Terminal.""",
			},
		},
	},
}
QPGE.ordo_ars_terminal = Room(**ordo_ars_terminal_dict)
QPGE.list_of_rooms.append(ordo_ars_terminal_dict['name'])

#### Corridor Alpha
corridor_alpha_dict = {
	'name': 'corridor_alpha',
	'title': u"Sec C alpha: Corridor (Central Axis -- Forward)",
	'visited': False,
	'gravity': False,
	'descr': u"""
 You are in a long cylindrical passage, so long that you cannot see the end of it.  It simply disappears into darkness beyond your vision.  The walls are covered in panels with protruding soft cushions and handholds to easily correct trajectory or anchor yourself.""",
	'vdescr': u"""
 You are in 'Sec C alpha: Central Axis Forward Corridor.'  The passage is so long that it disappears into darkness beyond your vision.  The walls are covered in panels with protruding soft cushions and handholds to easily correct trajectory or anchor yourself.""",
	'options': u"""
 There's nothing to do here but continue on your way.""",
	'paths': {
		'aft': (
			"aft",
			("hatch","es"),
			"unlocked",
			"Sec R: Research Bay",
			"research_bay",
			),
		'port': (
			"port",
			("airlock","s"),
			"unlocked",
			"Sec C alpha: Airlock",
			"corridor_alpha_airlock",
			),
		'forward': (
			"forward",
			("airlock","s"),
			"unlocked",
			"Sec M beta: Med Bay (Quarantine)",
			"med_bay_beta",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.corridor_alpha = Room(**corridor_alpha_dict)
QPGE.list_of_rooms.append(corridor_alpha_dict['name'])

#### Corridor Alpha Airlock
corridor_alpha_airlock_dict = {
	'name': 'corridor_alpha_airlock',
	'title': u"Sec C alpha: Airlock",
	'visited': False,
	'gravity': False,
	'descr': u"""
 You are in an airlock.  Considering the posted warning about EVAs, you shouldn't leave the ship without a suit.""",
	'vdescr': u"""
 You are in an airlock.  There is a posted warning about EVAs.""",
	'options': u"""
 There is a spacesuit here you can wear.""",
	'paths': {
		'starboard': (
			"starboard",
			("airlock stage","s"),
			"unlocked",
			"Sec C alpha: Corridor (Central Axis -- Forward)",
			"corridor_alpha",
			),
		'port': (
			"port",
			("airlock stage","s"),
			"unlocked",
			"Sec C alpha: Airlock (Outer Hull)",
			"corridor_alpha_airlock_outside"
			),
	},
	'actions': {
		'wear': {
			'spacesuit': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("wear","put"),
				'subj': "spacesuit",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "",
				'new_item': None,
				'descr': u"""
 You decide to wear the spacesuit.  You can now safely leave the ship.""",
			},
		},
	},
}
QPGE.corridor_alpha_airlock = Room(**corridor_alpha_airlock_dict)
QPGE.list_of_rooms.append(corridor_alpha_airlock_dict['name'])

#### Corridor Alpha Airlock (outside ship)
corridor_alpha_airlock_outside_dict = {
	'name': 'corridor_alpha_airlock_outside',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.corridor_alpha_airlock_outside = Room(**corridor_alpha_airlock_outside_dict)
QPGE.list_of_rooms.append(corridor_alpha_airlock_outside_dict['name'])

#### Port-side Storage alpha -- Equipment
storage_alpha_dict = {
	'name': 'storage_alpha',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.storage_alpha = Room(**storage_alpha_dict)
QPGE.list_of_rooms.append(storage_alpha_dict['name'])

#### Starboard Storage beta -- Micrograv Galley
storage_beta_dict = {
	'name': 'storage_beta',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.storage_beta = Room(**storage_beta_dict)
QPGE.list_of_rooms.append(storage_beta_dict['name'])

#### Medical Bay beta
med_bay_beta_dict = {
	'name': 'med_bay_beta',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'above_forward': (
			"above-forward",
			("airlock","s"),
			"unlocked",
			"Sec D: Docking Bay",
			"docking_bay",
			),
		'above_aft': (
			"above-aft",
			("airlock","s"),
			"unlocked",
			"Sec C alpha: Corridor (Central Axis -- Forward)",
			"corridor_alpha",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.med_bay_beta = Room(**med_bay_beta_dict)
QPGE.list_of_rooms.append(med_bay_beta_dict['name'])

#### Docking Bay
docking_bay_dict = {
	'name': 'docking_bay',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""
 You are in the docking bay access corridor.  There are faint hand-smears of blood here.""",
	'vdescr': u"""
 You are in the docking bay access corridor.  There are faint hand-smears of blood here.""",
	'options': u"""
 There's nothing to do here but keep exploring.""",
	'paths': {
		'forward_port': (
			"forward-to-port",
			("airlock","s"),
			"unlocked",
			"Docking Bay: Airlock",
			"docking_bay_airlock",
			),
		'forward_starboard': (
			"forward-to-starboard",
			("hatch","es"),
			"unlocked",
			"Docking Bay: Storage",
			"docking_bay_storage"
			),
		'aft_below': (
			"aft-below",
			("airlock","s"),
			"unlocked",
			"Sec M beta: Med Bay (Quarantine)",
			"med_bay_beta",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.docking_bay = Room(**docking_bay_dict)
QPGE.list_of_rooms.append(docking_bay_dict['name'])

#### Docking Bay Storage
docking_bay_storage_dict = {
	'name': 'docking_bay_storage',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""
 You are in the docking bay storage area.""",
	'vdescr': u"""
 You are in the docking bay storage area.""",
	'options': u"""
 There's nothing to do here.""",
	'paths': {
		'aft': (
			"aft",
			("hatch","es"),
			"unlocked",
			"Sec D: Docking Bay",
			"docking_bay",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.docking_bay_storage = Room(**docking_bay_storage_dict)
QPGE.list_of_rooms.append(docking_bay_storage_dict['name'])

#### Docking Bay Airlock
docking_bay_airlock_dict = {
	'name': 'docking_bay_airlock',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""
 You are in the docking bay airlock.""",
	'vdescr': u"""
 You are in the docking bay airlock.""",
	'options': u"""
 You might want to clean up all the blood.""",
	'paths': {
		'forward': (
			"forward",
			("airlock stage","s"),
			"unlocked",
			"Shuttlecraft One: Airlock",
			"shuttlecraft_one_airlock",
			),
		'aft': (
			"aft",
			("airlock stage","s"),
			"unlocked",
			"Sec D: Docking Bay",
			"docking_bay"
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.docking_bay_airlock = Room(**docking_bay_airlock_dict)
QPGE.list_of_rooms.append(docking_bay_airlock_dict['name'])

#### Shuttlecraft One: Airlock
shuttlecraft_one_airlock_dict = {
	'name': 'shuttlecraft_one_airlock',
	'title': u"Shuttlecraft One: Airlock",
	'visited': False,
	'gravity': False,
	'descr': u"""
 You are in the airlock for Shuttlecraft One.  There is blood everywhere.""",
	'vdescr': u"""
 You are in the airlock for Shuttlecraft One.  There is blood everywhere.""",
	'options': u"""
 You might want to clean up all the blood here.""",
	'paths': {
		'below': (
			"below",
			("airlock stage","s"),
			"unlocked",
			"Docking Bay: Airlock",
			"docking_bay_airlock",
			),
		'forward': (
			"forward",
			("airlock stage","s"),
			"unlocked",
			"Shuttlecraft One: NCM Cabin",
			"shuttlecraft_one_ncm_cabin"
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.shuttlecraft_one_airlock = Room(**shuttlecraft_one_airlock_dict)
QPGE.list_of_rooms.append(shuttlecraft_one_airlock_dict['name'])

#### Shuttlecraft One: NCM's Cabin
shuttlecraft_one_ncm_cabin_dict = {
	'name': 'shuttlecraft_one_ncm_cabin',
	'title': u"Shuttlecraft One: NCM Cabin",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'aft': (
			"aft",
			("airlock","s"),
			"unlocked",
			"Shuttlecraft One: Airlock",
			"shuttlecraft_one_airlock",
			),
		'forward': (
			"forward",
			("door","s"),
			"unlocked",
			"Shuttlecraft One: Officer's Cabin",
			"shuttlecraft_one_officer_cabin",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.shuttlecraft_one_ncm_cabin = Room(**shuttlecraft_one_ncm_cabin_dict)
QPGE.list_of_rooms.append(shuttlecraft_one_ncm_cabin_dict['name'])

#### Shuttlecraft One: Officer's Cabin
shuttlecraft_one_officer_cabin_dict = {
	'name': 'shuttlecraft_one_officer_cabin',
	'title': u"Shuttlecraft One: Officer's Cabin",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'aft': (
			"aft",
			("door","s"),
			"unlocked",
			"Shuttlecraft One: NCM Cabin",
			"shuttlecraft_one_ncm_cabin",
			),
		'forward': (
			"forward",
			("door","s"),
			"unlocked",
			"Shuttlecraft One: Cockpit",
			"shuttlecraft_one_pilot_cabin",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.shuttlecraft_one_officer_cabin = Room(**shuttlecraft_one_officer_cabin_dict)
QPGE.list_of_rooms.append(shuttlecraft_one_officer_cabin_dict['name'])

#### Shuttlecraft One: Pilot's Cabin
shuttlecraft_one_pilot_cabin_dict = {
	'name': 'shuttlecraft_one_pilot_cabin',
	'title': u"Shuttlecraft One: Cockpit",
	'visited': False,
	'gravity': False,
	'descr': u"""
 You are in the cockpit of Shuttlecraft One.  You can see a brilliant, blue and white planet through the viewport.  According to the console, it is called 'Vega b'.""",
	'vdescr': u"""
 You are in the cockpit of Shuttlecraft One.  Vega b is visible through the viewport.""",
	'options': u"""
 There are coordinates on the console for three landing sites on the surface of the planet -- the colony on the north west continent, the north east islands, or the south west continent.  You can pilot the shuttle to any of these locations, although your ship appears to be in geosynchronous orbit over the research base.""",
	'paths': {
		'aft': (
			"aft",
			("door","s"),
			"unlocked",
			"Shuttlecraft One: Officer's Cabin",
			"shuttlecraft_one_officer_cabin",
			),
	},
	'actions': {
		'pilot': {
			'shuttle_to_vega_b_base': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S-O",
				'verb': ("pilot","fly"),
				'subj': "shuttle",
				'dprt': "to",
				'dobj': "base",
				'iprt': None,
				'iobj': None,
				'rtrn': "vega_b_landing_site",
				'new_item': None,
				'descr': u"""
 You decide to pilot the shuttlecraft to the research base on Vega b.""",
			},
		},
	},
}
QPGE.shuttlecraft_one_pilot_cabin = Room(**shuttlecraft_one_pilot_cabin_dict)
QPGE.list_of_rooms.append(shuttlecraft_one_pilot_cabin_dict['name'])

#### Shuttlecraft One: Storage/Engine
shuttlecraft_one_storage_dict = {
	'name': 'shuttlecraft_one_storage',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.shuttlecraft_one_storage = Room(**shuttlecraft_one_storage_dict)
QPGE.list_of_rooms.append(shuttlecraft_one_storage_dict['name'])

#### Corridor Beta
corridor_beta_dict = {
	'name': 'corridor_beta',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.corridor_beta = Room(**corridor_beta_dict)
QPGE.list_of_rooms.append(corridor_beta_dict['name'])

#### Medical Ring alpha: Med Bay
med_ring_alpha_dict = {
	'name': 'med_ring_alpha',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.med_ring_alpha = Room(**med_ring_alpha_dict)
QPGE.list_of_rooms.append(med_ring_alpha_dict['name'])

#### Medical Ring beta: Dr Kaplan's Office
med_ring_beta_dict = {
	'name': 'med_ring_beta',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.med_ring_beta = Room(**med_ring_beta_dict)
QPGE.list_of_rooms.append(med_ring_beta_dict['name'])

#### Medical Ring gamma: Medical Storage
med_ring_gamma_dict = {
	'name': 'med_ring_gamma',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.med_ring_gamma = Room(**med_ring_gamma_dict)
QPGE.list_of_rooms.append(med_ring_gamma_dict['name'])

#### Medical Ring delta: Medical Lab
med_ring_delta_dict = {
	'name': 'med_ring_delta',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.med_ring_delta = Room(**med_ring_delta_dict)
QPGE.list_of_rooms.append(med_ring_delta_dict['name'])

#### Medical Ring delta b: Morgue
med_ring_morgue_dict = {
	'name': 'med_ring_morgue',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.med_ring_morgue = Room(**med_ring_morgue_dict)
QPGE.list_of_rooms.append(med_ring_morgue_dict['name'])

#### Engineering
engineering_dict = {
	'name': 'engineering',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.engineering = Room(**engineering_dict)
QPGE.list_of_rooms.append(engineering_dict['name'])

#### Reactor Bay
reactor_bay_dict = {
	'name': 'reactor_bay',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.reactor_bay = Room(**reactor_bay_dict)
QPGE.list_of_rooms.append(reactor_bay_dict['name'])

#### Nuclear Fuel Storage
nuclear_fuel_storage_dict = {
	'name': 'nuclear_fuel_storage',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.nuclear_fuel_storage = Room(**nuclear_fuel_storage_dict)
QPGE.list_of_rooms.append(nuclear_fuel_storage_dict['name'])

#### Nuclear Waste Storage
nuclear_waste_storage_dict = {
	'name': 'nuclear_waste_storage',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.nuclear_waste_storage = Room(**nuclear_waste_storage_dict)
QPGE.list_of_rooms.append(nuclear_waste_storage_dict['name'])

#### Corridor Gamma
corridor_gamma_dict = {
	'name': 'corridor_gamma',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.corridor_gamma = Room(**corridor_gamma_dict)
QPGE.list_of_rooms.append(corridor_gamma_dict['name'])

#### Server Hub
server_hub_dict = {
	'name': 'server_hub',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.server_hub = Room(**server_hub_dict)
QPGE.list_of_rooms.append(server_hub_dict['name'])

#### Quantum Core
quantum_core_dict = {
	'name': 'quantum_core',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.quantum_core = Room(**quantum_core_dict)
QPGE.list_of_rooms.append(quantum_core_dict['name'])

#### Identity Core
id_core_dict = {
	'name': 'id_core',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.id_core = Room(**id_core_dict)
QPGE.list_of_rooms.append(id_core_dict['name'])

#### Airlock to Nuclear Pulse Propulsion Rocket
nppr_airlock_dict = {
	'name': 'nppr_airlock',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.nppr_airlock = Room(**nppr_airlock_dict)
QPGE.list_of_rooms.append(nppr_airlock_dict['name'])

#### NPPR and Fuel Storage (Outside Ship)
nppr_fuel_storage_dict = {
	'name': '',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.nppr_fuel_storage = Room(**nppr_fuel_storage_dict)
QPGE.list_of_rooms.append(nppr_fuel_storage_dict['name'])

#### SFS FULGORA: HABITATION RING ============================================================ ####

#### Sec O alpha: North Gardens, east side
sec_o_alpha_east_dict = {
	'name': 'sec_o_alpha_east',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_alpha_east = Room(**sec_o_alpha_east_dict)
QPGE.list_of_rooms.append(sec_o_alpha_east_dict['name'])

#### Sec O alpha: North Gardens, monument
sec_o_alpha_monument_dict = {
	'name': 'sec_o_alpha_monument',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_alpha_monument = Room(**sec_o_alpha_monument_dict)
QPGE.list_of_rooms.append(sec_o_alpha_monument_dict['name'])

#### Sec O alpha: North Gardens, west side
sec_o_alpha_west_dict = {
	'name': 'sec_o_alpha_west',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_alpha_west = Room(**sec_o_alpha_west_dict)
QPGE.list_of_rooms.append(sec_o_alpha_west_dict['name'])

#### Junction O alpha/beta
jn_o_alpha_beta_dict = {
	'name': 'jn_o_alpha_beta',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.jn_o_alpha_beta = Room(**jn_o_alpha_beta_dict)
QPGE.list_of_rooms.append(jn_o_alpha_beta_dict['name'])

#### Sec O beta: Jr Officer Quarters (corridor)
sec_o_beta_dict = {
	'name': 'sec_o_beta',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_beta = Room(**sec_o_beta_dict)
QPGE.list_of_rooms.append(sec_o_beta_dict['name'])

#### Sec O beta a: Lt McNair's Quarters (Chief Engineer)
sec_o_beta_a_dict = {
	'name': 'sec_o_beta_a',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_beta_a = Room(**sec_o_beta_a_dict)
QPGE.list_of_rooms.append(sec_o_beta_a_dict['name'])

#### Sec O beta b: Lt Schreiber's Quarters (MRD Programmer/Physicist)
sec_o_beta_b_dict = {
	'name': 'sec_o_beta_b',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_beta_b = Room(**sec_o_beta_b_dict)
QPGE.list_of_rooms.append(sec_o_beta_b_dict['name'])

#### Sec O beta c: Ens Nishimura's Quarters (1st Pilot)
sec_o_beta_c_dict = {
	'name': 'sec_o_beta_c',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_beta_c = Room(**sec_o_beta_c_dict)
QPGE.list_of_rooms.append(sec_o_beta_c_dict['name'])

#### Sec O beta d: Ens Volkova's Quarters (2nd Pilot)
sec_o_beta_d_dict = {
	'name': 'sec_o_beta_d',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_beta_d = Room(**sec_o_beta_d_dict)
QPGE.list_of_rooms.append(sec_o_beta_d_dict['name'])

#### Sec O gamma a: Officer's Mess Hall & Galley (North side)
sec_o_gamma_north_dict = {
	'name': 'sec_o_gamma_north',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_gamma_north = Room(**sec_o_gamma_north_dict)
QPGE.list_of_rooms.append(sec_o_gamma_north_dict['name'])

#### Sec O gamma b: Officer's Rec-Room (South side)
sec_o_gamma_south_dict = {
	'name': 'sec_o_gamma_south',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_gamma_south = Room(**sec_o_gamma_south_dict)
QPGE.list_of_rooms.append(sec_o_gamma_south_dict['name'])

#### Sec O delta: Officer's Head -- Corridor
sec_o_delta_dict = {
	'name': 'sec_o_delta',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_delta = Room(**sec_o_delta_dict)
QPGE.list_of_rooms.append(sec_o_delta_dict['name'])

#### Sec O delta a: Officer's Head -- Showers
sec_o_delta_a_dict = {
	'name': 'sec_o_delta_a',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_delta_a = Room(**sec_o_delta_a_dict)
QPGE.list_of_rooms.append(sec_o_delta_a_dict['name'])

#### Sec O delta b: Officer's Head -- Toilets
sec_o_delta_b_dict = {
	'name': 'sec_o_delta_b',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_delta_b = Room(**sec_o_delta_b_dict)
QPGE.list_of_rooms.append(sec_o_delta_b_dict['name'])

#### Sec O epsilon: Officer's Gym (North Side)
sec_o_epsilon_north_dict = {
	'name': 'sec_o_epsilon_north',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_epsilon_north = Room(**sec_o_epsilon_north_dict)
QPGE.list_of_rooms.append(sec_o_epsilon_north_dict['name'])

#### Sec O epsilon: Officer's Observation deck (South Side)
sec_o_epsilon_south_dict = {
	'name': 'sec_o_epsilon_south',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_epsilon_south = Room(**sec_o_epsilon_south_dict)
QPGE.list_of_rooms.append(sec_o_epsilon_south_dict['name'])

#### Sec O zeta: Captain's Galley, Mess, and Office (Corridor)
sec_o_zeta_dict = {
	'name': 'sec_o_zeta',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_zeta = Room(**sec_o_zeta_dict)
QPGE.list_of_rooms.append(sec_o_zeta_dict['name'])

#### Sec O zeta a: Captain's Galley
sec_o_zeta_a_dict = {
	'name': 'sec_o_zeta_a',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_zeta_a = Room(**sec_o_zeta_a_dict)
QPGE.list_of_rooms.append(sec_o_zeta_a_dict['name'])

#### Sec O zeta b: Captain's Mess
sec_o_zeta_b_dict = {
	'name': 'sec_o_zeta_b',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_zeta_b = Room(**sec_o_zeta_b_dict)
QPGE.list_of_rooms.append(sec_o_zeta_b_dict['name'])

#### Sec O zeta c: Captain's Office hallway
sec_o_zeta_c_dict = {
	'name': 'sec_o_zeta_c',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_zeta_c = Room(**sec_o_zeta_c_dict)
QPGE.list_of_rooms.append(sec_o_zeta_c_dict['name'])

#### Sec O zeta d: Captain's Office
sec_o_zeta_d_dict = {
	'name': 'sec_o_zeta_d',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_zeta_d = Room(**sec_o_zeta_d_dict)
QPGE.list_of_rooms.append(sec_o_zeta_d_dict['name'])

#### Junction O zeta/eta a: Outer Corridor
jn_o_zeta_eta_a_dict = {
	'name': 'jn_o_zeta_eta_a',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.jn_o_zeta_eta_a = Room(**jn_o_zeta_eta_a_dict)
QPGE.list_of_rooms.append(jn_o_zeta_eta_a_dict['name'])

#### Junction O zeta/eta b: Elevator Access
jn_o_zeta_eta_b_dict = {
	'name': 'jn_o_zeta_eta_b',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.jn_o_zeta_eta_b = Room(**jn_o_zeta_eta_b_dict)
QPGE.list_of_rooms.append(jn_o_zeta_eta_b_dict['name'])

#### Sec O eta: Captain's Quarters (Outer Corridor)
sec_o_eta_dict = {
	'name': 'sec_o_eta',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_eta = Room(**sec_o_eta_dict)
QPGE.list_of_rooms.append(sec_o_eta_dict['name'])

#### Sec O eta a: Captain's Quarters
sec_o_eta_a_dict = {
	'name': 'sec_o_eta_a',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_eta_a = Room(**sec_o_eta_a_dict)
QPGE.list_of_rooms.append(sec_o_eta_a_dict['name'])

#### Sec O eta b: Captain's Observation Deck
sec_o_eta_b_dict = {
	'name': 'sec_o_eta_b',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_eta_b = Room(**sec_o_eta_b_dict)
QPGE.list_of_rooms.append(sec_o_eta_b_dict['name'])

#### Sec O theta: Sr Officer's Quarters (Corridor a)
sec_o_theta_a_dict = {
	'name': 'sec_o_theta_a',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_theta_a = Room(**sec_o_theta_a_dict)
QPGE.list_of_rooms.append(sec_o_theta_a_dict['name'])

#### Sec O theta a1: Maj Jeanville's Quarters
sec_o_theta_a1_dict = {
	'name': 'sec_o_theta_a1',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_theta_a1 = Room(**sec_o_theta_a1_dict)
QPGE.list_of_rooms.append(sec_o_theta_a1_dict['name'])

#### Sec O theta: Sr Officer's Quarters (Corridor b)
sec_o_theta_b_dict = {
	'name': 'sec_o_theta_b',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_theta_b = Room(**sec_o_theta_b_dict)
QPGE.list_of_rooms.append(sec_o_theta_b_dict['name'])

#### Sec O theta b1: Dr Kaplan's Quarters
sec_o_theta_b1_dict = {
	'name': 'sec_o_theta_b1',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_theta_b1 = Room(**sec_o_theta_b1_dict)
QPGE.list_of_rooms.append(sec_o_theta_b1_dict['name'])

#### Junction O theta/iota
jn_o_theta_iota_dict = {
	'name': 'jn_o_theta_iota',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.jn_o_theta_iota = Room(**jn_o_theta_iota_dict)
QPGE.list_of_rooms.append(jn_o_theta_iota_dict['name'])

#### Sec O iota: South Gardens (west side)
sec_o_iota_west_dict = {
	'name': 'sec_o_iota_west',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_iota_west = Room(**sec_o_iota_west_dict)
QPGE.list_of_rooms.append(sec_o_iota_west_dict['name'])

#### Sec O iota: South Gardens Monument
sec_o_iota_monument_dict = {
	'name': 'sec_o_iota_monument',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_iota_monument = Room(**sec_o_iota_monument_dict)
QPGE.list_of_rooms.append(sec_o_iota_monument_dict['name'])

#### Sec O iota: South Gardens (east side)
sec_o_iota_east_dict = {
	'name': 'sec_o_iota_east',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_iota_east = Room(**sec_o_iota_east_dict)
QPGE.list_of_rooms.append(sec_o_iota_east_dict['name'])

#### Sec O kappa: Long-term Storage and Reserves (Corridor)
sec_o_kappa_dict = {
	'name': 'sec_o_kappa',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_kappa = Room(**sec_o_kappa_dict)
QPGE.list_of_rooms.append(sec_o_kappa_dict['name'])

#### Sec O lambda: Utilities and Water Recycling (Corridor)
sec_o_lambda_dict = {
	'name': 'sec_o_lambda',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_lambda = Room(**sec_o_lambda_dict)
QPGE.list_of_rooms.append(sec_o_lambda_dict['name'])

#### Sec O mu: Arms Storage (Corridor)
sec_o_mu_dict = {
	'name': 'sec_o_mu',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_mu = Room(**sec_o_mu_dict)
QPGE.list_of_rooms.append(sec_o_mu_dict['name'])

#### Sec O nu: Security Office (Corridor)
sec_o_nu_dict = {
	'name': 'sec_o_nu',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_nu = Room(**sec_o_nu_dict)
QPGE.list_of_rooms.append(sec_o_nu_dict['name'])

#### Junction O nu/xi: Elevator
jn_o_nu_xi_dict = {
	'name': 'jn_o_nu_xi',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.jn_o_nu_xi = Room(**jn_o_nu_xi_dict)
QPGE.list_of_rooms.append(jn_o_nu_xi_dict['name'])

#### Sec O xi: NCM Mess and Rec Room
sec_o_xi_dict = {
	'name': 'sec_o_xi',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_xi = Room(**sec_o_xi_dict)
QPGE.list_of_rooms.append(sec_o_xi_dict['name'])

#### Sec O omicron: NCM Gym & Head
sec_o_omicron_dict = {
	'name': 'sec_o_omicron',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_omicron = Room(**sec_o_omicron_dict)
QPGE.list_of_rooms.append(sec_o_omicron_dict['name'])

#### Sec O pi: NCM Quarters (Corridor)
sec_o_pi_dict = {
	'name': 'sec_o_pi',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_pi = Room(**sec_o_pi_dict)
QPGE.list_of_rooms.append(sec_o_pi_dict['name'])

#### Sec O pi a: NCO Quarters
sec_o_pi_a_dict = {
	'name': 'sec_o_pi_a',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_pi_a = Room(**sec_o_pi_a_dict)
QPGE.list_of_rooms.append(sec_o_pi_a_dict['name'])

#### Sec O pi b: Enlisted Quarters
sec_o_pi_b_dict = {
	'name': 'sec_o_pi_b',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.sec_o_pi_b = Room(**sec_o_pi_b_dict)
QPGE.list_of_rooms.append(sec_o_pi_b_dict['name'])

#### Jn O pi/alpha
jn_o_pi_alpha_dict = {
	'name': 'jn_o_pi_alpha',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.jn_o_pi_alpha = Room(**jn_o_pi_alpha_dict)
QPGE.list_of_rooms.append(jn_o_pi_alpha_dict['name'])

#### VEGA B: SFS FULGORA BASE AND RESEARCH COLONY ============================================ ####

#### Landing Site
vega_b_landing_site_dict = {
	'name': 'vega_b_landing_site',
	'title': u"Vega b: Research Colony Landing Site",
	'visited': False,
	'gravity': True,
	'descr': u"""
 You are standing on the surface of Vega b outside Shuttlecraft One -- the air is heavy and damp, the starlight of Vega is a brilliant blue-white, and the ground is wet and muddy.  Thick grass surrounds the hard baked clay landing pad, and you can see a path that leads into a forest.  You are not certain why, but this place feels like home.""",
	'vdescr': u"""
 You are standing on the surface of Vega b outside Shuttlecraft One.  The path to the Research Colony leads off into a forest.""",
	'options': u"""
 If you don't feel like sticking around here, you can return to your ship in orbit.""",
	'paths': {
		'north': (
			"north",
			("forest path","s"),
			"unlocked",
			"Vega b: Landing Site -- Forest Path",
			"vega_b_landing_path",
			),
	},
	'actions': {
		'return': {
			'to_ship': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("return","pilot","fly"),
				'subj': "ship",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "docking_bay",
				'new_item': None,
				'descr': u"""
 You decide to pilot the shuttlecraft back to the SFS Fulgora.""",
			},
		},
	},
}
QPGE.vega_b_landing_site = Room(**vega_b_landing_site_dict)
QPGE.list_of_rooms.append(vega_b_landing_site_dict['name'])

#### Path from Landing Site to Garden
vega_b_landing_path_dict = {
	'name': 'vega_b_landing_path',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.vega_b_landing_path = Room(**vega_b_landing_path_dict)
QPGE.list_of_rooms.append(vega_b_landing_path_dict['name'])

#### Outer Garden/Forest (Front)
vega_b_outer_garden_dict = {
	'name': 'vega_b_outer_garden',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.vega_b_outer_garden = Room(**vega_b_outer_garden_dict)
QPGE.list_of_rooms.append(vega_b_outer_garden_dict['name'])

#### Inner Garden (Front)
vega_b_inner_garden_dict = {
	'name': 'vega_b_inner_garden',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.vega_b_inner_garden = Room(**vega_b_inner_garden_dict)
QPGE.list_of_rooms.append(vega_b_inner_garden_dict['name'])

#### Grave Site (Front)
vega_b_grave_site_dict = {
	'name': 'vega_b_grave_site',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.vega_b_grave_site = Room(**vega_b_grave_site_dict)
QPGE.list_of_rooms.append(vega_b_grave_site_dict['name'])

#### TransHab Airlock (Outside)
vega_b_transhab_airlock_outside_dict = {
	'name': 'vega_b_transhab_airlock_outside',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.vega_b_transhab_airlock_outside = Room(**vega_b_transhab_airlock_outside_dict)
QPGE.list_of_rooms.append(vega_b_transhab_airlock_outside_dict['name'])

#### TransHab Airlock (Inside)
vega_b_transhab_airlock_dict = {
	'name': 'vega_b_transhab_airlock',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.vega_b_transhab_airlock = Room(**vega_b_transhab_airlock_dict)
QPGE.list_of_rooms.append(vega_b_transhab_airlock_dict['name'])

#### TransHab Rec Room/Mess
vega_b_transhab_recroom_dict = {
	'name': 'vega_b_transhab_recroom',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.vega_b_transhab_recroom = Room(**vega_b_transhab_recroom_dict)
QPGE.list_of_rooms.append(vega_b_transhab_recroom_dict['name'])

#### TransHab Airlock to Captain's Quarters
vega_b_transhab_captains_airlock_dict = {
	'name': 'vega_b_transhab_captains_airlock',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.vega_b_transhab_captains_airlock = Room(**vega_b_transhab_captains_airlock_dict)
QPGE.list_of_rooms.append(vega_b_transhab_captains_airlock_dict['name'])

#### TransHab Captain's Quarters
vega_b_transhab_captains_quarters_dict = {
	'name': 'vega_b_transhab_captains_quarters',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.vega_b_transhab_captains_quarters = Room(**vega_b_transhab_captains_quarters_dict)
QPGE.list_of_rooms.append(vega_b_transhab_captains_quarters_dict['name'])

#### TransHab Airlock to Pressurized Tunnel (Officer Quarters, Greenhouse, Lab)
vega_b_transhab_lab_airlock_dict = {
	'name': 'vega_b_transhab_lab_airlock',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.vega_b_transhab_lab_airlock = Room(**vega_b_transhab_lab_airlock_dict)
QPGE.list_of_rooms.append(vega_b_transhab_lab_airlock_dict['name'])

#### TransHab Airlock to Pressurized Tunnel (NCM Quarters, Maintenance, Sanitation)
vega_b_transhab_ncm_airlock_dict = {
	'name': 'vega_b_transhab_ncm_airlock',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.vega_b_transhab_ncm_airlock = Room(**vega_b_transhab_ncm_airlock_dict)
QPGE.list_of_rooms.append(vega_b_transhab_ncm_airlock_dict['name'])

#### TransHab Officer's Quarters
vega_b_transhab_officer_quarters_dict = {
	'name': 'vega_b_transhab_officer_quarters',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.vega_b_transhab_officer_quarters = Room(**vega_b_transhab_officer_quarters_dict)
QPGE.list_of_rooms.append(vega_b_transhab_officer_quarters_dict['name'])

#### TransHab NCM Quarters
vega_b_transhab_ncm_quarters_dict = {
	'name': 'vega_b_transhab_ncm_quarters',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.vega_b_transhab_ncm_quarters = Room(**vega_b_transhab_ncm_quarters_dict)
QPGE.list_of_rooms.append(vega_b_transhab_ncm_quarters_dict['name'])

#### TransHab Greenhouse
vega_b_transhab_greenhouse_dict = {
	'name': 'vega_b_transhab_greenhouse',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.vega_b_transhab_greenhouse = Room(**vega_b_transhab_greenhouse_dict)
QPGE.list_of_rooms.append(vega_b_transhab_greenhouse_dict['name'])

#### TransHab Lab
vega_b_transhab_lab_dict = {
	'name': 'vega_b_transhab_lab',
	'title': u"",
	'visited': False,
	'gravity': False,
	'descr': u"""""",
	'vdescr': u"""""",
	'options': u"""""",
	'paths': {
		'west': (
			"west",
			("door","s"),
			"unlocked",
			"Another Room",
			"another_room",
			),
	},
	'actions': {
		'use': {
			'terminal': {
				# available types are: V-S, V-S-O, V-S-O-I
				'type': "V-S",
				'verb': ("use"),
				'subj': "terminal",
				'dprt': None,
				'dobj': None,
				'iprt': None,
				'iobj': None,
				'rtrn': "research_bay_terminal",
				'new_item': None,
				'descr': u"""""",
			},
		},
	},
}
QPGE.vega_b_transhab_lab = Room(**vega_b_transhab_lab_dict)
QPGE.list_of_rooms.append(vega_b_transhab_lab_dict['name'])

#### VEGA B: NORTH-WEST CONTINENT ============================================================ ####

#### VEGA B: NORTH-EAST ISLANDS ============================================================== ####

#### VEGA B: SOUTH-WEST CONTINENT ============================================================ ####

#### Extra Rooms
QPGE.victory = Victory()
QPGE.death = Death()
QPGE.quit = Quit()

#### RUN GAME ================================================================================ ####
the_game = Game(QPGE.research_bay)
the_game.play()

#### End of File ============================================================================= ####
