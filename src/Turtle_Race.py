"""
This program consists of a turtle race.
The user can choose the number of turtles to race and the color of each turtle.

Author: Miguel Sapage
"""

from classes import *
from graphics import *

def run_lap(allTurtles, colors_list, number_laps, turtles, win, winner): #Makes each lap run
	#Takes care of the movement of the turtles
	movment = MoveTurtles()
	movment.moveTurtle(allTurtles)

	sleep(1)

	winner.register_winner(allTurtles)
	winner_color = winner.winner_color(colors_list)
	winner.winners_list(winner_color, number_laps)

	turtles.undrawTurtles(allTurtles, win)

	return winner_color

def main():
	
	#Number of turtles chosen by user
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

	#Draws turtles on the window (colors chosen by user)
	turtles = CreatTurtles()
	turtles.turtlesPosition(number_turtles, win.getWidth())	
	allTurtles = turtles.generateTurtle(number_turtles, win)

	#The user can bet on a turtle
	bet = Bet()
	bet.enterKey()
	winner_bet = bet.getBet()

	winner = Winner()
	print('-' * 30)
	
	for i in range(number_laps):
		if i > 0:
			turtles.redrawTurtles(allTurtles, win)

		winner_color = run_lap(allTurtles, turtles.list_of_colors(), number_laps, turtles, win, winner)

		print(f'Lap {i + 1} winner: {winner_color}')

	overall_winner = winner.overall_winner(turtles.list_of_colors())
	#Decides if it's a tie or there's a single winner
	if len(overall_winner) > 1:
		print("It's a tie between", *overall_winner)
	else:
		print('The overall winner is', *overall_winner)
		
	quit_button = Quit(win)
	restart_button = Restart(win)

	if len(overall_winner) > 1:
		tiebreaker_button = Tie(win)
		turtles_to_untie = tiebreaker_button.untie(turtles.list_of_colors(), allTurtles, overall_winner)
	else:
		bet.checkBet(*overall_winner)
		print('-' * 30)

	
	while True:
		click = win.getMouse()
		if quit_button.interact(click):
			break
		elif restart_button.interact(click):
			win.close()
			main()
			break
		elif tiebreaker_button.interact(click):
			quit_button.undraw()
			restart_button.undraw()
			tiebreaker_button.undraw()

			turtles.redrawTurtles(turtles_to_untie, win)

			winner = Winner()

			winner_color = run_lap(turtles_to_untie, overall_winner, 1, turtles, win, winner) #It will run only 1 lap

			print('The overall winner is', winner_color)

			bet.checkBet(winner_color)
			print('-' * 30)

			quit_button = Quit(win)
			restart_button = Restart(win)

	win.close()

main()