from graphics import *
from button import Button
from random import randrange
from time import sleep

class NumberTurtles:
	"""
	Let the user choose the number of turtles
	"""
	def __init__(self):
		#GUI to choose the number of racers
		self.win = win = GraphWin('Turtles', 200, 200)

		Text(Point(100, 50), 'How many turtles do').draw(win)
		Text(Point(100, 65), 'you want to race?').draw(win)
		Text(Point(100, 80), '(between 2 and 10)').draw(win)
		self.nrTurtles = Entry(Point(100, 110), 2).draw(win)

	def getNumberTurtles(self):
		return int(self.nrTurtles.getText())

	def enterKey(self):
		while True:
			if self.win.getKey() == 'Return':
				self.win.close()
				break
			else:
				pass

class Laps:

	def __init__(self):

		self.win = win = GraphWin('Laps', 200, 200)

		Text(Point(100, 70), 'How many laps do').draw(win)
		Text(Point(100, 85), 'you want to run?').draw(win)

		self.laps = Entry(Point(100, 105), 3).draw(win)

	def getNumberLaps(self):
		return int(self.laps.getText())

	def enterKey(self):
		while True:
			if self.win.getKey() == 'Return':
				self.win.close()
				break
			else:
				pass

class CreatTurtles:

	def __init__(self):
		#GUI to choose the colors
		self.win = win = GraphWin('Colors', 200, 200)

		Text(Point(100, 55), 'Choose the color of').draw(win)
		Text(Point(100, 70), 'of each turtle').draw(win)
		self.color = Entry(Point(100, 100), 7).draw(win)

		self.addButton = Button(win, Point(100, 150), 35, 20, 'Add') #To add turtle
		self.addButton.activate()

	def turtlesPosition(self, nrTurtles, width):
		self.xCoords = [] #Saves the position of each turtle
		#Calculates x coordinates based on the number of turtles chosen to center them and add it to the list
		x = (width / nrTurtles) / 2
		for i in range(nrTurtles):
			self.xCoords.append(x)
			x = x + (width / nrTurtles)


	def generateTurtle(self, nrTurtles, win):
		allTurtles = [] #Saves a list of turtles
		self.all_colors = [] #Saves turtles colors
		for i in range(nrTurtles):
			if self.interact():
				xcoord = self.xCoords[i]
				turtleColor = str(self.color.getText()) #Only work valid colors
				self.all_colors.append(turtleColor)
				turtle = self.makeTurtle(turtleColor, xcoord, win)
			allTurtles.append(turtle)
			self.color.setText('')
		self.win.close() #Closes GUI to choose colors after all turtles colors are set
		return allTurtles

	def list_of_colors(self):
		return self.all_colors

	def makeTurtle(self, color, xcoord, win):
		turtle = []
		body = Rectangle(Point(xcoord - 7, 473), Point(xcoord + 7, 487))
		body.setFill(color)
		paw1 = Rectangle(Point(xcoord - 10, 476), Point(xcoord - 8, 478))
		paw1.setFill(color)
		paw2 = Rectangle(Point(xcoord - 10, 482), Point(xcoord - 8, 484))
		paw2.setFill(color)
		paw3 = Rectangle(Point(xcoord + 10, 476), Point(xcoord + 8, 478))
		paw3.setFill(color)
		paw4 = Rectangle(Point(xcoord + 10, 482), Point(xcoord + 8, 484))
		paw4.setFill(color)
		head = Rectangle(Point(xcoord - 4, 467), Point(xcoord + 4, 472))
		head.setFill(color)
		turtle.append(body)
		turtle.append(paw1)
		turtle.append(paw2)
		turtle.append(paw3)
		turtle.append(paw4)
		turtle.append(head)
		for i in turtle:
			i.draw(win) #Draw the turtle one object at a time
		return turtle

	def interact(self):
		while True:
			click = self.win.getMouse()
			if self.addButton.clicked(click):
				return True

	def undrawTurtles(self, allTurtles, win):
		for turtle in allTurtles:
			for part in turtle:
				part.undraw()

	def redrawTurtles(self, allTurtles, win):
		for turtle in allTurtles:
			ycoord = turtle[0].getCenter().getY()
			dy = 480 - ycoord
			for part in turtle:
				part.move(0, dy)
				part.draw(win)

class MoveTurtles:

	def moveTurtle(self, allTurtles):
		racerSpeed = self.speed(len(allTurtles)) #Fixed speed for each turtle for entire race
		whileLoopCheck = True
		sleep(0.2)
		while whileLoopCheck == True: #Runs until get a winner
			for turtle in allTurtles: #Turtles move one at a time
				dy = racerSpeed[allTurtles.index(turtle)]
				for i in turtle: #Body parts of the turtle move on at a time
					i.move(0, -dy)
			for turtle in allTurtles: #Checks if there is a winner
				if turtle[0].getCenter().getY() <= 34:
					whileLoopCheck = False
			sleep(0.001)

	def speed(self, nrTurtles):
		#The speed is based on how many pixels the turtle will move at a time
		speeds = []
		for i in range(nrTurtles):
			speeds.append(250 / randrange(200,250))
		return speeds

class Quit:
	def __init__(self,win):
		self.quit = Button(win, Point(270,480), 40, 20, 'Quit')
		self.quit.activate()
		
	def interact(self,p):
		while True:
			if self.quit.clicked(p):
				return True
			else:
				return None

	def undraw(self):
		self.quit.deactivate()
		self.quit.undraw()

class Restart:
	def __init__(self,win):
		self.restart = Button(win, Point(215,480), 60, 20, 'Restart')
		self.restart.activate()
		
	def interact(self,p):
		while True:
			if self.restart.clicked(p):
				return True
			else:
				return None

	def undraw(self):
		self.restart.deactivate()
		self.restart.undraw()

class Winner:
	def __init__(self):
		self.list_of_winners = []

	def register_winner(self, allTurtles):
		self.winner = 0
		position = 280
		for turtle in allTurtles: #Compares the positions of all turtles
			if turtle[0].getCenter().getY() < position:
				position = turtle[0].getCenter().getY()
				self.winner = allTurtles.index(turtle)

	def winner_color(self, colors_list):
		return colors_list[self.winner] #Winner of specific lap

	def winners_list(self, winner, laps):
		self.list_of_winners.append(winner) #List of lap winners

	def overall_winner(self, colors_list):
		winner = []
		wins = 0
		for color in colors_list:
			if self.list_of_winners.count(color) > wins:
				wins = self.list_of_winners.count(color)
				winner = [color]
			elif self.list_of_winners.count(color) == wins and color not in winner:
				winner.append(color)
		self.list_of_winners = []
		return winner

class Tie:
	def __init__(self, win):
		self.tiebreaker = Button(win, Point(135,480), 90, 20, 'Tiebreaker')
		self.tiebreaker.activate()

	def interact(self,p):
		while True:
			if self.tiebreaker.clicked(p):
				return True
			else:
				return None

	def undraw(self):
		self.tiebreaker.deactivate()
		self.tiebreaker.undraw()

	def untie(self, colors_list, allTurtles, overall_winner):
		turtles_to_untie = [] #List of tied turtles
		for i in overall_winner:
			index = colors_list.index(i)
			turtles_to_untie.append(allTurtles[index])
		return turtles_to_untie

class Bet:
	def __init__(self):
		self.win = win = GraphWin('Bet', 200, 200)

		Text(Point(100, 70), 'Which turtle do you').draw(win)
		Text(Point(100, 85), 'think will win?').draw(win)
		self.winner_bet = Entry(Point(100, 110), 7).draw(win)

	def getBet(self):
		return self.winner_bet.getText()

	def enterKey(self):
		while True:
			if self.win.getKey() == 'Return':
				self.win.close()
				break
			else:
				pass

	def checkBet(self, overall_winner):
		#Compares the bet to the winner
		if self.winner_bet.getText() == overall_winner:
			print('Your bet was right!!')
		else:
			print(f'Poor bet...try again (your bet: {self.winner_bet.getText()})')