Class Description:
f1_team enables users to create their own barebones Formula 1 team. They can choose their own team name, that of their two drivers, race engineers, team principal, and three sponsors. The class can match the drivers with their race engineers and set where on the car the sponsors will be displayed, allowing users to build their own Formula 1 team with an endless number of possibilities.

Variables: 
num_drivers - Class variable that describes the number of drivers in a team. This number is always the same as per Formula 1 rules, hence it being a class variable.

self._team_name - The name of the Formula 1 team
self._driver1 & self._driver2 - The names of the team's two drivers
self._eng1 & self._eng2 - The names of the team's two race engineers
self._principal - The name of the team's team principal
self._pair1 & self._pair2 - Pairs composing of one driver and one race engineer who work together during races
self.sponsor1, self.sponsor2, & self.sponsor3 - The three sponsors that will be displayed on the team's cars
front_wing - Assigns where the first sponsor will be displayed
chasis - Assigns where the second sponsor will be displayed
rear_wing - Assigns where the third sponsor will be displayed

Methods:
get_team_name() - Returns the name of the team. Takes no arguments.
set_drivers() - Sets the variables self._driver1 & self._driver2 to the two given arguments, making the teams two drivers. Returns None.
get_drivers() - Returns the names of the team's two drivers. Takes no arguments.
set_engineers() - Sets the variables self._eng1 & self._eng2 to the given arguments, making the teams two race engineers. Returns None.
get_engineers() - Returns the names of the team's two race engineers. Takes no arguments.
set_princ() - Sets the variable self._principal to the given argument, making the team's team principal. Returns None.
get_princ() - Returns the name of the team principal. Takes no arguments.
match_drivers() - Puts the drivers and race engineers into pairs, returns the pais as a tuple. Takes no arguments.
set_sponsors() - Sets the varibles self.sponsor1, self.sponsor2, & self.sponsor3 to the given three arguments, making the teams three sponsors. Returns None.
get_sponsors() - Returns the name of the three sponsors. Takes no arguments
sponsor_display() - Selects where the sponsors will be displayed. Returns a string stating which sponsor will be displayed where on the car. Takes no arguments.

Demo Program Description:
The demo program will run the user through the process of making their own Formula 1 team. First, it greets the user with a welcome and introductory message, giving them the lineup of team members they will fill. Then, the program will go through each part of the lineup, taking user inputs at each step and then confirming the lineup at each 'milestone' (when both drivers are given, the pairs of drivers & engineers, etc.). When it comes to sponsors, the program will enter a while loop to confirm that the user properly inputs either 'yes' or 'no' to indicate whether or not they want to add sponsors. Once all parts of the team are given, the program will output a message describing the team lineup and end the program with a good luck message.
Demo Program Instructions:
In order to run the demo program, first ensure that you have an updated version of Python 3 on your computer. Then, simply download the python file 'A_Starkman_10_1.py', open up your computers shell/interpreter, navigate to the directory where you downloaded the file and type in 'python3 A_Starkman_10_1.py' and press enter. The program will guide you from there!