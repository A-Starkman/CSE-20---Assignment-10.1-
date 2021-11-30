#Adam Starkman
#Asgn 10.1
#Creates a class with at least 1 class variable, 2 data variables, 2 get-set methods, and 2 other methods

class f1_team:
    #sets the class variable 'positions' which describes the positions that need to be filled in order to have a complete team
    positions = ('2 Drivers', '2 Race Engineers', '1 Team Principal', '3 Sponsors (optional)')

    def __init__(self, team_name):
        self._team_name = team_name #sets the name of the team

    def get_team_name(self):
        return self._team_name#sets the argument team_name to a private data variable
    def set_drivers(self, name1, name2):
        self._driver1 = name1
        self._driver2 = name2 #sets the given names to private variables for each driver
    def get_drivers(self):
        return ("The two drivers of " + self._team_name + " are " + self._driver1 + " and " + self._driver2 + ".") #concentates the team and driver names into a string and returns it
    def set_engineers(self, engineer1, engineer2, ):
        self._eng1 = engineer1
        self._eng2 = engineer2 #sets the given names to private variables for each enginee
        
    def get_engineers(self):
        return self._eng1, self._eng2 # returns the name of the two race engineers
    def set_princ(self, principal):        
        self._principal = principal  #sets self._principal to the given argument

    
    def get_princ(self):
        return self._principal #returns the name of the team principal

    def match_drivers(self):
        #creates the driver/engineer pairs
        self._pair1 = self._driver1 + " and " + self._eng1
        self._pair2 = self._driver2 + " and " + self._eng2
        return self._pair1, self._pair2 #returns the pairs as a tuple

    def set_sponsors(self, sponsor1, sponsor2, sponsor3):
        self._sponsor1 = sponsor1
        self._sponsor2 = sponsor2 #sets the given sponsors to private variables
        self._sponsor3 = sponsor3

    def get_sponsors(self):
        return self._sponsor1, self._sponsor2, self._sponsor3 #returns the name of the three sponsors
    
    def sponsor_display(self):
        #assigns where on the car the sponsor will be displayed
        front_wing = self._sponsor1
        chasis = self._sponsor2
        rear_wing = self._sponsor3
        return (front_wing + ", which will be displayed on the front wing of your car, " + chasis + " on the chasis of your car, and " + rear_wing + " on the rear wing,") #concentates a string stating which sponsor will be displayed where on the car

    
def main():
    print("Welcome to the Formula 1 team builder!") #intro/welcome statement
    intro_name = input("Please input the name of your team:\n") #asks the user to input the team name
    team = f1_team(intro_name) #creates a class object with the given name
    print("Alright lets make " + team.get_team_name() + " into a full team! \nHere are the positions you'll need to fill in order to make you own F1 team:\n" + str(team.positions))
    driver_1 = input("Please input the name of your first driver:\n")
    driver_2 = input("Please input the name of your second driver:\n") #asks the user for the names of their two drivers
    team.set_drivers(driver_1, driver_2) #uses set_drivers to assign those drivers to the team
    print("Alright! " + intro_name + " now has its drivers: " + driver_1 + " and " + driver_2 + ".") #confirms with the user that the team now has drivers
    eng_1 = input("Please input the name of your first race engineer:\n")
    eng_2 = input("Please input the name of your second race engineer:\n") #asks the user for the names of their two race engineers
    team.set_engineers(eng_1, eng_2) #uses set_engineers to assign those engineers to the team
    
    print("Alright, now that we have your race engineers, lets match them up with your drivers.") 
    print(team.get_team_name() + " now has the driver/engineer pairs of:\n" + str(team.match_drivers())) #concentates the driver/engineer pairs together and displays them for the user
    while True:
        x = input("Would you like to add sponsors to your team? (answer with 'yes' or 'no') ") #asks if they want to add sponsors
        x = x.lower() #makes x lower case for ease of use
        if x == "yes" or x == "no":
            break
        else:
            print("That was not a valid answer, please input either 'yes' or 'no'.")
    if x == "yes":
        spons_1 = input("Please input your first sponsor:\n")
        spons_2 = input("Please input your second sponsor:\n") #asks the user for their three sponsors
        spons_3 = input("Please input your third sponsor:\n")
        team.set_sponsors(spons_1, spons_2, spons_3) #uses set_sponsors to assign the team the sponsors given by the user
        print(team.sponsor_display()) #uses sponsor_display to tell the user where on the car the sponsors will be displayed
    team_princ = input("And lastly, please input the name of your team principal:\n") #asks the user for the name of their principal
    team.set_princ(team_princ) #uses set_princ to assign the team its principal
    print("\nCongrats! You have now have your won Formula 1 team. \nYour team principal, " + team.get_princ() + ", will over see the driver and engineer pairs: " + str(team.match_drivers()) + " as you take on the competition in the coming year!")  #gives the user the layout/lineup of their team
    if x == "yes": 
        print("Your sponsors: " + team.sponsor_display() + " are ready to support " + team.get_team_name() + "! \nGood luck!") #if the included sponsors, mentions them
    else: #if they didnt include sponsors
        print("Good luck!")
    



if __name__ == "__main__":
    main()
    

    
