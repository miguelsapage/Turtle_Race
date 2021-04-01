"""
This program consists of a turtle race.
The user can choose the number of turtles to race and the color of each turtle.

Author: Miguel Sapage
"""

from classes import *
from graphics import *

def main():
	
	#Number of turtles choosen by user
	nturtles = NumberTurtles()
	
	nturtles.enterKey()
	number_turtles = nturtles.getNumberTurtles()

	#Number of laps
	laps = Laps()
	laps.enterKey()
	number_laps = laps.getNumberLaps()

	#GUI to see the race
	win = GraphWin('Race', 300, 500)
	Line(Point(0,20), Point(300,20)).draw(win)

	#Draws turtles on the window (colors choosen by user)
	turtles = CreatTurtles()
	turtles.turtlesPosition(number_turtles, win.getWidth())	
	allTurtles = turtles.generateTurtle(number_turtles, win)

	#Takes care of the movemment of the turtles
	movment = MoveTurtles()
	movment.moveTurtle(allTurtles)

	sleep(1)

	winner = Winner()
	winner.register_winner(allTurtles)
	winner_color = winner.winner_color(turtles.list_of_colors())
	print('-' * 30)
	print('Lap 1 winner:', winner_color)
	winner.winners_list(winner_color, number_laps)

	turtles.undrawTurtles(allTurtles, win)

	for i in range(number_laps - 1):
		turtles.redrawTurtles(allTurtles, win)

		movment = MoveTurtles()
		movment.moveTurtle(allTurtles)

		sleep(1)

		winner.register_winner(allTurtles)
		winner_color = winner.winner_color(turtles.list_of_colors())
		print('Lap', i + 2, 'winner:', winner_color)
		winner.winners_list(winner_color, number_laps)

		turtles.undrawTurtles(allTurtles, win)

	overall_winner = winner.overall_winner(turtles.list_of_colors())
	if len(overall_winner) > 1:
		print("It's a tie between", *overall_winner)
	else:
		print('The overall winner is', *overall_winner)
	print('-' * 30)

	quit_button = Quit(win)
	restart_button = Restart(win)
	while True:
		click = win.getMouse()
		if quit_button.interact(click):
			break
		elif restart_button.interact(click):
			win.close()
			main()
			break
		else:
			pass

	win.close()

main()