print("Welcome to Trucking Simulator.")
print("Your aim is to deliver your soya to Carrs Billington from John Beaty Transport")
roundabout = input('You come to a roundabout, do you "right" or "straight"? ')
if roundabout == "right":
    motorway = input('You come to the motorway, do you go "north" or "south"? ')
    if motorway == "north":
        junction = input('Do you take junction "43" or "44"? ')
        if junction == "44":
            trafficlights = input('Do you turn right at the first traffic light "1" or the second traffic lights "2"? ')
            if trafficlights == "2":
                print("You successfully delivered your load!")
            else:
                print("Game Over, you went to Greggs instead.")
        else:
            print("Game Over, You went into the middle of Carlisle and crashed into Nando's.")
    else:
        print("Game Over, you drove down to London you idiot.")
else:
    print("Game Over, You crashed into Arragons.")
