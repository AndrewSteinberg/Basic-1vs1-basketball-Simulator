#used imports
import pandas as pd
import csv
import random as rnd

#CSV Reading
file = open('1v1.csv')

data = pd.read_csv('1v1.csv')

#Player definer
Player1number = int(input('What number is assigned to player 1? '))

Player2number = int(input('What number is assigned to player 2? '))


#Cell Finder/CSV Stat Reader
def read_cell(x, y):
    with open('1v1.csv', 'r') as f:
        reader = csv.reader(f)
        y_count = 0
        for n in reader:
            if y_count == y:
                cell = n[x]
                return cell
            y_count += 1      

#Name Finder
Player1name = (read_cell(0, Player1number))
Player2name = (read_cell(0, Player2number))

#Stat finders
#Inside Shots Score
Player1insideshotskill = int((read_cell(1, Player1number)))
Player2insideshotskill = int((read_cell(1, Player2number)))
#Jumpshot Score
Player1jumpshotskill = int((read_cell(2, Player1number)))
Player2jumpshotskill = int((read_cell(2, Player2number)))
#Outside/3point Shot Score
Player1outsideshotskill = int((read_cell(4, Player1number)))
Player2outsideshotskill  = int((read_cell(4, Player2number)))
#Post Defense Score
Player1PostDefense = int((read_cell(8, Player1number)))
Player2PostDefense = int((read_cell(8, Player2number)))
#Perimeter Defense Score
Player1perimeterdefense = int((read_cell(9, Player1number)))
Player2perimeterdefense = int((read_cell(9, Player2number)))
#Midrange Defense Score
Player1midrangedefense = round((Player1perimeterdefense + Player1PostDefense)/2)
Player2midrangedefense = round((Player2perimeterdefense + Player1PostDefense)/2)
#Fouling Score
Player1Fouling = int((read_cell(12, Player1number)))
Player2Fouling = int((read_cell(12, Player2number)))
#Freethrow Score
Player1Freethrow = int((read_cell(3, Player1number)))
Player2Freethrow = int((read_cell(3, Player2number)))
#Ball Handling Score
Player1Handles = int((read_cell(5, Player1number)))
Player2Handles = int((read_cell(5, Player2number)))
#Steal Score
Player1Stealing = int((read_cell(10, Player1number)))
Player2Stealing = int((read_cell(10, Player2number)))
#Block Score
Player1Blocking = int((read_cell(11, Player1number)))
Player2Blocking = int((read_cell(11, Player2number)))
#PhysicalScores
Player1quickness = int((read_cell(13, Player1number)))
Player2quickness = int((read_cell(13, Player2number)))
Player1strength = int((read_cell(14, Player1number)))
Player2strength = int((read_cell(14, Player2number)))
Player1jumping = int((read_cell(15, Player1number)))
Player2jumping = int((read_cell(15, Player2number)))

#Game Start
print (Player1name + ' challenges ' + Player2name + ' to a game of one vs. one.')
#Player 1's Score without Free Throws
Player1ShotScore = 0
#Player 2's Score without Free Throws
Player2ShotScore = 0
#Tracker of if game is over
GAMEEND = 0
#Freethrow Tracker for both players
Player1FreeThrowscore = 0
Player2FreeThrowscore = 0

#This Fuction checks if a foul occured and then rolls to see if the player was caught
#It Also rolls Free throws if necassary
def FreethrowFoulchecker():
    global Player1FreeThrowscore
    #Checks for the Proc and Skill Check before calling the foul
    if Player1foulproc == 1 and rnd.randint(1,Player2Fouling) < rnd.randint(1,100):
        print (f'{Player2name} fouls {Player1name} on the shot')
        #Skill Check for Freethrows but only if the game was not won on the shot
        FreethrowChecker = Player1ShotScore + Player1FreeThrowscore 
        if FreethrowChecker < 21:
            if rnd.randint(1,Player1Freethrow) > (rnd.randint(1,70)):
                #Player 1 Free Throw Tracker gains plus 1 everytime a Freethrow is made
                Player1FreeThrowscore = Player1FreeThrowscore + 1
                print (Player1name + ' makes the freethrow.')
            else:
                print (Player1name + ' misses the freethrow.')
        else:
            print (f'As {Player1name} won the game on the shot they opt not to shoot the freethrow.')
            
#FreeThrow Checker for 2nd player
def FreethrowFoulchecker2():
    global Player2FreeThrowscore
    #Checks for the Proc and Skill Check before calling the foul
    if Player2foulproc == 1 and rnd.randint(1,Player1Fouling) < rnd.randint(1,100):
        #Skill Check for Freethrows but only if the game was not won on the shot
        print (f'{Player1name} fouls {Player2name} on the shot')
        FreethrowChecker2 = Player2ShotScore + Player2FreeThrowscore 
        if FreethrowChecker2 < 21:
            if rnd.randint(1,Player2Freethrow) > (rnd.randint(1,70)):
                #Player 1 Free Throw Tracker gains plus 1 everytime a Freethrow is made
                Player2FreeThrowscore = Player2FreeThrowscore + 1
                print (Player2name + ' makes the freethrow.')
            else:
                print (Player2name + ' misses the freethrow.') 
        else:
            print (f'As {Player2name} won the game on the shot they opt not to shoot the freethrow.')

#Checks if a block opportunity occurs and if the player successfully blocks the shot attempt         
def BlockChecker1():
    global BlockYes
    if Player1blockproc == 1 and rnd.randint(1,Player2Blocking) > rnd.randint(1,40):
        BlockYes = 1

def BlockChecker2():
    global BlockYes2
    if Player2blockproc == 1 and rnd.randint(1,Player1Blocking) > rnd.randint(1,40):
        BlockYes2 = 1


#Game Loop
while GAMEEND == 0:
    #Player 1 action decider
    action = rnd.randint(1,3)
    BlockYes = 0
    BlockYes2 = 0
    #Players are rewarded for athleticism through random events, if the player is quicker stronger, or jumps higher
    #then the opposition they gain a 5 bonus to their rolls for that possesion
    Statboostevent1 = rnd.randint(1,3)
    Statboostevent2 = rnd.randint(1,3)
    Player1Statboost = 0
    Player2Statboost = 0
    if Statboostevent1 == 1:
        if rnd.randint(1,Player1quickness) > rnd.randint(1,Player2quickness):
            Player1statboost = 5
        else:
            Player2Statboost = 5
    if Statboostevent1 == 2:
        if rnd.randint(1,Player1strength) > rnd.randint(1,Player2strength):
            Player1statboost = 5
        else:
            Player2Statboost = 5
    if Statboostevent1 == 3:
        if rnd.randint(1,Player1jumping) > rnd.randint(1,Player2jumping):
            Player1statboost = 5
        else:
            Player2Statboost = 5
    #Foul Randomizer and skill decider
    Player1foulproc = rnd.randint(1,3)
    Player2foulproc = rnd.randint(1,3)
    Player1stealproc = rnd.randint(1,4)
    Player2stealproc = rnd.randint(1,4)
    Player1blockproc = rnd.randint(1,4)
    Player2blockproc = rnd.randint(1,4)
    #While loop is active each possesion starts with this line
    print (Player1name + ' gets the ball.')
    #This if statement checks if a Steal Proc was activated and then will also skill check to see if the steal occurs
    #If it does then the possession ends and player 2 starts their turn, otherwise it continues as normal
    if Player2stealproc == 1 and rnd.randint(1,Player2Stealing) > rnd.randint(1,Player1Handles):
        print (Player2name + ' steals the ball and ends the possession.')
        print (' ')
    else:
        #player 1 inside shot, The action randomiser picks either Inside, midrange, or 3-pointer
        if action == 1:
            #This Print will create a flavor text of the shot attempt
            print (Player1name + ' ' + read_cell(17,rnd.randint(1,5)) + ' ' + Player2name + ' ' + read_cell(18,rnd.randint(1,5)))
            Shotattempt = rnd.randint(1,Player1insideshotskill + Player1Statboost)
            Defensiveeffort = rnd.randint(1,Player2PostDefense + Player2Statboost)
            #Checks for a block and ensure shot is not taken if block occurs
            Player1Blocking = Player1Blocking + 10
            BlockChecker1()
            Player1Blocking = Player1Blocking - 10
            if BlockYes == 0 :
                if Shotattempt < Defensiveeffort:
                    #Print will create Flavor text of miss
                    print (Player1name + read_cell(19,rnd.randint(1,5)))
                    #Runs Foul/Freethrow Checker
                    FreethrowFoulchecker()
                else:
                    #Print will create Flavor text of make
                    print (Player1name + read_cell(20,rnd.randint(1,5)))
                    #Player1ShotScore adds the player's previous score
                    Player1ShotScore = Player1ShotScore + 2
                    #Runs Foul/Freethrow Checker
                    FreethrowFoulchecker()
            else:
                print (f'{Player2name} blocks the shot attempt by {Player1name}')
    
            
        #player 1 Midrange Shot
        if action == 2:
            #Print will create flavor text for a midrange shot
            print (Player1name + read_cell(21,rnd.randint(1,6)) + " While " + Player2name + read_cell(22,rnd.randint(1,5)))
            Shotattempt = rnd.randint(1,Player1jumpshotskill + Player1Statboost)
            Defensiveeffort = rnd.randint(1,Player2midrangedefense + Player2Statboost)
            #Checks for a block and ensure shot is not taken if block occurs
            BlockChecker1()
            if BlockYes == 0 :
                if Shotattempt < Defensiveeffort:
                    #Print will create flavor text for a miss
                    print (Player1name + read_cell(23,rnd.randint(1,5)))
                    #Runs Foul/Freethrow Checker
                    FreethrowFoulchecker()
                else:
                    #Print will create flavor text for a make
                    print (Player1name + read_cell(24,rnd.randint(1,5)))
                    #Player1ShotScore adds the previous players score
                    Player1ShotScore = Player1ShotScore + 2
                    #Runs Foul/Freethrow Checker
                    FreethrowFoulchecker()
            else:
                print (f'{Player2name} blocks the shot attempt by {Player1name}')
             
        #Player 1 3 point Shot
        if action == 3:
            #Print will create flavor text for an outside shot
            print (Player1name + read_cell(25,rnd.randint(1,5)) + " while " + Player2name + read_cell(26,rnd.randint(1,5)))
            Shotattempt = rnd.randint(1,Player1outsideshotskill + Player1Statboost)
            Defensiveeffort = rnd.randint(1,Player2perimeterdefense + Player2Statboost)
            #Checks for a block and ensure shot is not taken if block occurs
            Player1Blocking = Player1Blocking - 10
            BlockChecker1()
            Player1Blocking = Player1Blocking + 10
            if BlockYes == 0 :
                if Shotattempt < Defensiveeffort:
                    #Print will create flavor text for a miss
                    print (Player1name + read_cell(27,rnd.randint(1,5)))
                    #Runs Foul/Freethrow Checker
                    FreethrowFoulchecker()
                else:
                    #Print will create flavor text for a make
                    print (Player1name + read_cell(28,rnd.randint(1,5)))
                    #Player1ShotScore adds the previous players score
                    Player1ShotScore = Player1ShotScore + 3
                    #Runs Foul/Freethrow Checker
                    FreethrowFoulchecker()
            else:
                print (f'{Player2name} blocks the shot attempt by {Player1name}')
            
        #Prints out game score at end of possesion     
        Player1TotalScore = Player1ShotScore + Player1FreeThrowscore
        Player2TotalScore = Player2ShotScore + Player2FreeThrowscore
        print (Player1name + ' ' + str(Player1TotalScore) + '-' + str(Player2TotalScore) + ' ' + Player2name)
        print ('')
        #If Player 1 gets a winning score GAMEEND is set to one which will lead to the loop closing
        if Player1TotalScore >= 21 and (Player1TotalScore - Player2TotalScore) >= 2:
            GAMEEND = 1
    

    #Ends Game when P1 gets 21, without this Player 2 will play an extra possession if they lose
    GTRACKER = 3 + GAMEEND
    GMEND = 1 + GAMEEND + GAMEEND + GAMEEND
    #Player 2 Action Decider, GMEN and GTRACKER are 1 and 3 unless player 1 wins, in which case they become 4 and 4
    #This makes sure that the action taken is 4, which ends the game and does not allow an extra attempt
    action2 = rnd.randint(GMEND,GTRACKER)
    #Players are rewarded for athleticism through random events, if the player is quicker stronger, or jumps higher
    #then the opposition they gain a 5 bonus to their rolls for that possesion
    Statboostevent1 = rnd.randint(1,3)
    Statboostevent2 = rnd.randint(1,3)
    Player1Statboost = 0
    Player2Statboost = 0
    if Statboostevent1 == 1:
        if rnd.randint(1,Player1quickness) > rnd.randint(1,Player2quickness):
            Player1statboost = 5
        else:
            Player2Statboost = 5
    if Statboostevent1 == 2:
        if rnd.randint(1,Player1strength) > rnd.randint(1,Player2strength):
            Player1statboost = 5
        else:
            Player2Statboost = 5
    if Statboostevent1 == 3:
        if rnd.randint(1,Player1jumping) > rnd.randint(1,Player2jumping):
            Player1statboost = 5
        else:
            Player2Statboost = 5
    #This if statment makes sure that the possession does not occur if Player one has ended the game
    if action2 != 4:
        print (Player2name + ' gets the ball.')
    #Player 2 Steal Checker
    if Player1stealproc == 1 and rnd.randint(1,Player1Stealing) > rnd.randint(1,Player2Handles) and action2 != 4:
        print (Player1name + ' steals the ball and ends the possesion.')
        print (' ')
    else:
        #Player 2 Inside Shot
        if action2 == 1:
            #Print will create flavor text for an inside shot attempt
            print (Player2name + ' ' + read_cell(17,rnd.randint(1,5)) + ' ' + Player1name + ' ' + read_cell(18,rnd.randint(1,5)))
            Shotattempt = rnd.randint(1,Player2insideshotskill + Player1Statboost)
            Defensiveeffort = rnd.randint(1,Player1PostDefense + Player2Statboost)
            #Checks for a block and ensure shot is not taken if block occurs block stat is effeted by area shot is taken
            Player2Blocking = Player2Blocking + 10
            BlockChecker2()
            Player1Blocking = Player1Blocking - 10
            if BlockYes2 == 0 :
                #Print will create flavor text if shot is missed
                if Shotattempt < Defensiveeffort:
                    print (Player2name + read_cell(19,rnd.randint(1,5)))
                    #Runs Foul/Freethrow Checker
                    FreethrowFoulchecker2()
                else:
                    #Print will create flavor text if shot is made
                    print (Player2name + read_cell(20,rnd.randint(1,5)))
                    #adds 2 to shot score if shot is made
                    Player2ShotScore = Player2ShotScore + 2
                    #Runs Foul/Freethrow Checker
                    FreethrowFoulchecker2()
            else:
                print (f'{Player1name} blocks the shot attempt by {Player2name}')
            
            
        #Player 2 Midrange Shot
        if action2 == 2:
            #Print creates flavor text for a midrange shot atempt
            print (Player2name + read_cell(21,rnd.randint(1,6)) + " While " + Player1name + read_cell(22,rnd.randint(1,5)))
            Shotattempt = rnd.randint(1,Player2jumpshotskill + Player1Statboost)
            Defensiveeffort = rnd.randint(1,Player1midrangedefense + Player2Statboost)
            BlockChecker2()
            if BlockYes2 == 0:
                if Shotattempt < Defensiveeffort:
                    #Print creates flavor text for a missed midrange shot
                    print (Player2name + read_cell(23,rnd.randint(1,5)))
                    #Runs Foul/Freethrow Checker
                    FreethrowFoulchecker2()
                else:
                    #Print creates flavor text for a made midrange shot
                    print (Player2name + read_cell(24,rnd.randint(1,5)))
                    #adds 2 to shot score if shot is made
                    Player2ShotScore = Player2ShotScore + 2
                    #Runs Foul/Freethrow Checker
                    FreethrowFoulchecker2()
            else:
                print (f'{Player1name} blocks the shot attempt by {Player2name}')
            
        #Player 2 3 point shot
        if action2 == 3:
            #print will create flavor text for an attempted outside/3point shot
            print (Player2name + read_cell(25,rnd.randint(1,5)) + " while " + Player1name + read_cell(26,rnd.randint(1,5)))
            Shotattempt = rnd.randint(1,Player2outsideshotskill + Player1Statboost)
            Defensiveeffort = rnd.randint(1,Player1perimeterdefense + Player2Statboost)
            Player2Blocking = Player2Blocking - 10
            BlockChecker2()
            Player1Blocking = Player1Blocking + 10
            if BlockYes2 == 0:
                if Shotattempt < Defensiveeffort:
                    #print will create flavor text for missed outside/3point shot
                    print (Player2name + read_cell(27,rnd.randint(1,5)))
                    #Runs Foul/Freethrow Checker
                    FreethrowFoulchecker2()
                else:
                    #print will create flavor text for made outside/3point shot
                    print (Player2name + read_cell(28,rnd.randint(1,5)))
                    #adds 3 to shot score if shot is made
                    Player2ShotScore = Player2ShotScore + 3
                    #Runs Foul/Freethrow Checker
                    FreethrowFoulchecker2()
            else:
                print (f'{Player1name} blocks the shot attempt by {Player2name}')
                
        if action2 != 4:
            #will print out the score at end of player 2 posession, will not do so if Player 1 has won the game
            Player1TotalScore = Player1ShotScore + Player1FreeThrowscore
            Player2TotalScore = Player2ShotScore + Player2FreeThrowscore
            print (Player1name + ' ' + str(Player1TotalScore) + '-' + str(Player2TotalScore) + ' ' + Player2name)
            print (' ')
            if Player2TotalScore >= 21 and (Player2TotalScore - Player1TotalScore) >= 2:
                GAMEEND = 1

# If player 1 wins
if Player1TotalScore >= 21 and (Player1TotalScore - Player2TotalScore) >= 2:
    print (Player1name + ' has won the 1 Vs. 1')

# If player 2 wins
if Player2TotalScore >= 21 and (Player2TotalScore - Player1TotalScore) >= 2:
    print ('')
    print (Player2name + ' has won the 1 Vs. 1')

