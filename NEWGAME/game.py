# small network game that has differnt blobs
# moving around the screen

import contextlib
with contextlib.redirect_stdout(None):
    import pygame
from client import Network
import random
import os
pygame.font.init()

# Constants
PLAYER_RADIUS = 10
START_VEL = 9
BALL_RADIUS = 10

W, H = 1600, 830

NAME_FONT = pygame.font.SysFont("comicsans", 20)
TIME_FONT = pygame.font.SysFont("comicsans", 30)
SCORE_FONT = pygame.font.SysFont("comicsans", 26)

COLORS = [(255,0,0), (255, 128, 0), (255,255,0), (128,255,0),(0,255,0),(0,255,128),(0,255,255),
		  (0, 128, 255), (0,0,255), (0,0,255), (128,0,255),(255,0,255),
		  (255,0,128),(128,128,128), (0,0,0)]

# Dynamic Variables
players = {}
balls = []

screen=pygame.display.set_mode((300,300))

# FUNCTIONS
def convert_time(t):
	"""
	converts a time given in seconds to a time in
	minutes

	:param t: int
	:return: string
	"""
	if type(t) == str:
		return t

	if int(t) < 60:
		return str(t) + "s"
	else:
		minutes = str(t // 60)
		seconds = str(t % 60)

		if int(seconds) < 10:
			seconds = "0" + seconds

		return minutes + ":" + seconds


def redraw_window(players, balls, game_time, score):
	"""
	draws each frame
	:return: None
	"""


	first = pygame.draw.rect(screen, (255, 255, 255), (0, 0, 100, 100))
	second = pygame.draw.rect(screen, (255, 255, 255), (100, 0, 100, 100))
	third = pygame.draw.rect(screen, (255, 255, 255), (200, 0, 100, 100))
	fourth = pygame.draw.rect(screen, (255, 255, 255), (0, 100, 100, 100))
	fifth = pygame.draw.rect(screen, (255, 255, 255), (100, 100, 100, 100))
	sixth = pygame.draw.rect(screen, (255, 255, 255), (200, 100, 100, 100))
	seventh = pygame.draw.rect(screen, (255, 255, 255), (0, 200, 100, 100))
	eighth = pygame.draw.rect(screen, (255, 255, 255), (100, 200, 100, 100))
	nineth = pygame.draw.rect(screen, (255, 255, 255), (200, 200, 100, 100))
	pygame.draw.line(screen, (255, 0, 100), (100, 300), (100, 0))
	pygame.draw.line(screen, (255, 0, 100), (200, 300), (200, 0))
	pygame.draw.line(screen, (255, 0, 100), (0, 100), (300, 100))


def main(name):
	"""
	function for running the game,
	includes the main loop of the game

	:param players: a list of dicts represting a player
	:return: None
	"""
	global players

	# start by connecting to the network
	server = Network()
	current_id = server.connect(name)
	balls, players, game_time = server.send("get")

	# setup the clock, limit to 30fps
	clock = pygame.time.Clock()

	run = True
	while run:
		clock.tick(30) # 30 fps max
		player = players[current_id]
		vel = START_VEL - round(player["score"]/14)
		if vel <= 1:
			vel = 1

		# get key presses
		keys = pygame.key.get_pressed()

		data = ""
		# movement based on key presses
		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			if player["x"] - vel - PLAYER_RADIUS - player["score"] >= 0:
				player["x"] = player["x"] - vel

		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			if player["x"] + vel + PLAYER_RADIUS + player["score"] <= W:
				player["x"] = player["x"] + vel

		if keys[pygame.K_UP] or keys[pygame.K_w]:
			if player["y"] - vel - PLAYER_RADIUS - player["score"] >= 0:
				player["y"] = player["y"] - vel

		if keys[pygame.K_DOWN] or keys[pygame.K_s]:
			if player["y"] + vel + PLAYER_RADIUS + player["score"] <= H:
				player["y"] = player["y"] + vel

		data = "move " + str(player["x"]) + " " + str(player["y"])

		# send data to server and recieve back all players information
		balls, players, game_time = server.send(data)

		for event in pygame.event.get():
			# if user hits red x button close window
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN:
				# if user hits a escape key close program
				if event.key == pygame.K_ESCAPE:
					run = False


		# redraw window then update the frame
		redraw_window(players, balls, game_time, player["score"])
		pygame.display.update()

	server.disconnect()
	pygame.quit()
	quit()


# get users name
while True:
 	name = input("Please enter your name: ")
 	if  0 < len(name) < 20:
 		break
 	else:
 		print("Error, this name is not allowed (must be between 1 and 19 characters [inclusive])")

# make window start in top left hand corner
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 30)

# setup pygame window
WIN = pygame.display.set_mode((W, H))
pygame.display.set_caption("Blobs")

# start game
main(name)