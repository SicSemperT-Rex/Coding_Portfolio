#IMPORTS
import tkinter, time, sys, os
import random

#MISC VARIABLES
missionFail = "Mission One: Failure"
missionSuccess = "Mission One: Complete"


#ALL FUNCTIONS
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(txt)
    
def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(txt)
    value = input()
    return value
    
def youSuck():
    clearScreen()
    typingPrint(missionFail)
    time.sleep(1.50)
    redo = input("\nWould you like to start again at the last checkpoint? Enter 1 for yes, or 2 for no: ")
    return int(redo)
    
def reloadLast():
    clearScreen()
    typingPrint("Starting from last checkpoint in three...")
    time.sleep(1.0)
    typingPrint("\nTwo...\n")
    time.sleep(1.0)
    typingPrint("\nOne.\n")
    time.sleep(1.0)
    clearScreen()
    time.sleep(1.50)

def clearScreen():
    os.system("clear")

speed = 2

while int(speed) == 2:
    speedpref = input("How fast would you like the text to print? Enter a number between 1 and 5, with 1 being the slowest:   ")
    if int(speedpref) == 1:
        txt = 0.10
    if int(speedpref) == 2:
        txt = 0.08
    if int(speedpref) == 3:
        txt = 0.06
    if int(speedpref) == 4:
        txt = 0.04
    if int(speedpref) == 5:
        txt = 0.02



    speed = typingInput( "Is this the text speed you want? Enter 1 for yes, or 2 for no:   " )
    if int(speed) == 1:
        break



#OPENING MENU
print( "Welcome, space marine!" )
Name1 = input( "Please type in your first name:   " )
Name2 = input( "Please type in your last name:   ")

clearScreen()
time.sleep(1.50)

#OPENING EXPOSITION - COMPLETED
typingPrint( "The year is 1965.")
time.sleep(1.50)
typingPrint( "\nThe Third Reich has long since been defeated on Earth; however, thanks to the advancement of V2 rocket technology, the war for space is only beginning." )
time.sleep(1.50)
typingPrint( " Since 1947, Unified Space Command and Soviet Space Command have been locked in a deadly war against the Weltraumwaffe.")
time.sleep(1.50)
typingPrint( " Great battleships fight for superiority among the stars, manned by brave astronauts and space marines.")
time.sleep(1.50)
clearScreen()
typingPrint( "The USPCS Farragut is one such ship, and you, Sergeant " + Name2 + ", are one such space marine." )
time.sleep(1.50)
clearScreen()

saalwachterEnd = 0
typingPrint( "MISSION ONE: THE SAALWACHTER\n" )
time.sleep(1.50)
typingPrint( "\nSITUATION:\n" )
time.sleep(1.50)
typingPrint( "\nThe KWRS Saalwachter is the first of a new generation of Astro-Aryan starship, much faster than older class cruisers. \nThe Saalwachter is currently on patrol near Mars. You and your squad have been tasked with boarding and capturing it to give the engineers aboard the Farragut the chance to study it.")
time.sleep(1.50)
clearScreen()
time.sleep(3.0)
typingPrint( "You are floating in the hatch between the cockpit and the main compartment in a boarding shuttle, holding onto the handrails on either side to keep yourself stationary. You can barely fit in the doorway in your space suit and exoskeleton. You watch through the cockpit window as the Saalwachter comes into view. The new cruiser is small, sleek. An impressive feat of engineering, even for the Astro-Aryans. So far, it seems that the ship's highly sophisticated radar has not detected you, yet.\n" )
time.sleep(1.50)
typingPrint( "\nIn front of you, the shuttle pilot and your good friend, Kiwi, is slowly easing the ship forward, his face a mask of concentration. Behind you, the six members of your squad are strapped into their jump seats.\n" )
time.sleep(1.50)
typingPrint( "\n'We're about five minutes out, " + Name1 + ",' Kiwi says. 'According to G2, you have two main entry points: the aft bulkhead, near engineering, or the forward bulkhead, near the bridge and the wireless room. Which one are you breaching?'\n")
time.sleep(1.50)
pickBulkhead = input( "\nWhich bulkhead will you breach? Type 1 for aft, or 2 for forward:   \n" )
if int(pickBulkhead) == 1:
    choiceBulk = "Aft"
    clearScreen()
    typingPrint( "'Aft', you say. 'We'll disable the engines before we get to the bridge so they can't run.'\n")
    time.sleep(1.50)
else:
    choiceBulk = "Forward"
    clearScreen()
    typingPrint( "'Forward', you say. 'The faster we cut communications, the better.'\n")

typingPrint( "\n'" + choiceBulk + " it is,' Kiwi says. 'Now, get out of my cockpit and get ready to drop. Cabin's going dark in 30 seconds.'\n")
time.sleep(1.50)
typingPrint( "\nYou turn and push yourself back into the main compartment of the shuttle, where your squad is waiting.\n")
time.sleep(1.50)
typingPrint( "\n'Helmets on, suits pressurized,' you command. '30 seconds to dark approach; five minutes to drop.'\n")
time.sleep(1.50)
typingPrint( "\n'Aye, sir,' your squad echoes in unison.\n" )
time.sleep(1.50)
clearScreen()
typingPrint( "\nYou drift back to your seat, right next to the door, where your things are located. You put on your helmet and sling your plasma rifle in front of you. With the press of a few buttons, the hiss of air fills your suit, and it pressurizes around you. \n")
time.sleep(1.50)
typingPrint( "\nYou hear Kiwi's voice over your helmet's intercom system: 'Beginning dark approach in three...'\n")
time.sleep(1.00)
typingPrint( "\n'Two...'\n")
time.sleep(1.00)
typingPrint( "\n'One.'\n")
time.sleep(1.00)
typingPrint( "\nThe lights in the cabin go dim, save for a bright red light by the door, where you'll be jumping from.")
time.sleep(1.50)
clearScreen()


#MAIN GAME - CHECKPOINT 1
checkpoint = 1
while checkpoint == 1:
    typingPrint( "The minutes tick by like hours. You hear the thunks and whine of the shuttles mooring lines as Kiwi launches them towards the Saalwachter and secures your ship to the cruiser. Finally, though, the red light turns green. It's time for the jump.\n")
    time.sleep(1.50)
    typingPrint( "\nYou stand up from your seat. 'On your feet!' You call into your helmet's radio.\n")
    time.sleep(1.50)
    typingPrint( "\nThe squad all get to their feet.\n")
    time.sleep(1.50)
    typingPrint("\n'Standby for open door,' Kiwi says over the radio.\n")
    time.sleep(1.50)
    typingPrint("\nYou hear the whine of gears as the door next to you opens into empty space. The shuttle is still about 100 yards from the Saalwachter. It's a long jump, but it isn't impossible.\n")
    time.sleep(1.50)
    pickFirst = input( "\nDo you jump first and lead the way, or do you jump second to make sure everyone makes it off the shuttle? Enter 1 for first, 2 for second:   \n") 
    
    #THIS GOES TO CHECKPOINT 2.1
    if int(pickFirst) == 1:
        clearScreen()
        typingPrint( "One of the mooring lines is coming from the door frame. You hook both of the retractable safety lines on your belt to this line and shove yourself out of the ship, heading directly for the Saalwachter. You've always been first in the fight, and this mission isn't any different.\n")
        time.sleep(1.50)
        typingPrint( "\nFor about a minute, you float weightlessly through the vast emptiness of space. It's an experience that is both exhilirating and terrifying. Finally, you hit the other ship with a soft thunk. You've landed close to one of the maintenance rails, about 10 yards from the " + choiceBulk + " hatch. You unclip from the mooring line with one safety line, then clip into the maintenance rail. You repeat the process with the second safety line.\n")
        time.sleep(1.50)
        typingPrint( "\n'Next marine: you're clear for jump,' you say into your radio as you look up at the shuttle. A few moments later, you see another marine begin their jump on the line.\n")
        time.sleep(1.50)
        pickWatchJ = input( "\nDo you watch your men complete the jump, or do you watch the " + choiceBulk + " hatch? Enter 1 to watch the jump, or 2 to watch the hatch:   ")
        if int(pickWatchJ) == 1:
            clearScreen()
            typingPrint( "You continue to watch the ship as, one by one, your men drift from the shuttle. One every ten seconds, on your mark.\n" )
            time.sleep(1.50)
            typingPrint( "\nAs the first marine to jump gets within ten feet, you notice him unsling his plasma rifle.\n" )
            time.sleep(1.50)
            typingPrint( "\nA bright burst of plasma darts past you from behind, barely missing your head. Cursing, you spin around to see a Weltraumwaffen marine poking his head out of the aft hatch. He's taking aim at you, again. You have no cover.\n" )
            time.sleep(1.50)
            pickFight = input( "\nDo you unsling your rifle and shoot back, or do you duck? Enter 1 to shoot back, or 2 to duck:   " )
            if int(pickFight) == 1:
                getShot = random.randint(1, 2)
                if getShot == 1:
                    clearScreen()
                    typingPrint( "You're a quick draw. While the enemy marine adjusts his aim, you're able to level your own plasma rifle at him and fire.\n" )
                    time.sleep(1.50)
                    typingPrint( "\nUnlike the enemy marine, your aim is true: the beam hits him in the chest, and he begins to drift away, motionless.\n" )
                    time.sleep(1.50)
                    checkpoint = 2.1

                else:
                    clearScreen()
                    typingPrint( "The marine begins to adjust his aim to fire again. Panicked, you fumble for your own rifle." )
                    time.sleep(1.50)
                    typingPrint( "\nThe marine fires a second time. You see the beam go straight for your chest. You hear a pop as your suit decompresses, then all goes black.\n")
                    time.sleep(1.50)
                    plzRedo = youSuck()
                    if plzRedo == 1:
                        reloadLast()
                    else:
                        sys.exit()

            else:
                clearScreen()
                typingPrint( "You grab your safety line and yank, pulling you close to the ship as the Nazi fires another shot.\n" )
                time.sleep(1.50)
                typingPrint( "\nThe Nazi fires, missing you and missing your men.\n" )
                time.sleep(1.50)
                typingPrint( "\nBefore you can get your own rifle to shoot back, one of your men shoots, hitting the astronaut and killing him. You watch as his body floats away into empty space.\n" )
                time.sleep(1.50)
                checkpoint = 2.1

        else:
            clearScreen()
            typingPrint( "You don't know if the crew of the Saalwachter noticed the drop ship hooking up with them, or if they felt you landing. You figure, however, that if they did, they would be more likely to come out of that hatch in front of you than any other. You post up with your rifle aimed at the hatch, ready for anyone who might try and come up from the hatch.\n" )
            time.sleep(1.50)
            typingPrint( "\n'I'll provide overwatch,' you say into your radio. 'Next person to land: the rest of the team will jump on your mark.'\n" )
            time.sleep(1.50)
            typingPrint( "\n'Aye, sir.' Barlowe's voice crackles over the radio.\n" )
            time.sleep(1.50)
            typingPrint( "\nFrom there, you hear Barlowe give call outs to the rest of the team, telling when the next person should jump.\n" )
            time.sleep(1.50)
            typingPrint( "\nAs Barlowe calls out to the last person to jump, you watch the hatch begin to open.\n" )
            time.sleep(1.50)
            typingPrint( "\nYou take aim, waiting until you can see the head of the Weltraumwaffe astronaut.\n" )
            time.sleep(1.50)
            sgtMiss = random.randint(1, 3)
            if sgtMiss == 1:
                clearScreen()
                typingPrint( "Your shot goes a little wide, barely missing the Marine.\n" )
                getShot = random.randint(1, 3)
                if getShot == 1:
                    typingPrint("\nYou panic. You begin to adjust your aim, but before you can. the Marine fires. You watch as the plasma bolt heads directly into your chest.\n" )
                    time.sleep(1.50)
                    typingPrint("\nYou hear a pop as your suit decompresses, and all goes black.\n")
                    time.sleep(1.50)
                    plzRedo = youSuck()
                    if plzRedo == 1:
                        reloadLast()
                    else:
                        sys.exit()

                else:
                    typingPrint("\nYou quickly readjust your aim as the Marine scrambles for his weapon.\n")
                    time.sleep(1.50)
                    typingPrint("\nThis time, your aim is true: you hit the Marine before he's able to get a shot off. His body begins to float out to empty space.")
                    time.sleep(1.50)
                    checkpoint = 2.1   

            else:
                clearScreen()
                typingPrint( "Your aim is true: before the Marine knows what's happening, he's dead, his body floating away from the ship and into the vast emptiness of space.")
                time.sleep(1.50)
                checkpoint = 2.1

#GOES TO CHECKPOINT 2.2
    else:
        clearScreen()
        typingPrint( "You stand to the side of the door. 'First marine: hook up and jump!' you order in your headset.\n" )
        time.sleep(1.50)
        typingPrint( "\nThe first marine in line hooks both retractable safety lines from his belt onto the mooring line by the door. Once he's secure, he jumps through the door and towards the Saalwachter.\n")
        time.sleep(1.50)
        typingPrint( "\nYou watch him as he descends. Your heart is racing as you do, waiting to hear that he got to the bottom safely.\n" )
        time.sleep(1.50)
        typingPrint( "\nFinally, you hear his voice over the radio: 'Jumper landed.'\n" )
        time.sleep(1.50)
        typingPrint( "\nYou send the rest of the men down the line, one every ten seconds. You are the last to jump, hooking your safety lines onto the mooring line and pushing off into the abyss.\n" )
        time.sleep(1.50)
        clearScreen()
        typingPrint( "A few seconds later, you suddenly see a plasma blast rocket away dart from the hatch, narrowly missing the first marine to land. 'Contact! Contact! Contact!' you hear the shouts over the radio.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou see a second plasma blast. This one comes from comes from your men. You watch as it hits the Weltraumwaffen marine, and as his body floats away from the ship. You don't see any more coming from up the port, but where there's one, there's more.\n")
        time.sleep(1.50)
        clearScreen()
        typingPrint( "You call out over the radio: 'What the hell just happened?'\n" )
        time.sleep(1.50)
        typingPrint( "\n'Contact,' you hear. 'We don't see any more of them coming up, so far.'\n" )
        time.sleep(1.50)
        checkpoint = 2.2

    if checkpoint != 1:
        break



#CHECKPOINT 2.1 - ENTER THE SHIP, YOU JUMPED FIRST
while checkpoint == 2.1:
    typingPrint( "\nSo far, there are no alarms, and nobody else is coming up the hatch. Still: where there's one, there's likely more.\n" )
    time.sleep(1.50)
    pickWait = input( "\nDo you wait for the rest of your squad to descend the hatch, or do you push forward with the marine who's already landed? Enter 1 for wait, or 2 for go.   ")
    if int(pickWait) == 1:
        clearScreen()
        typingPrint( "'Contact! Contact! Contact!' You keep your rifle aimed at the hatch as the rest of the marines finish their descent.\n" )
        time.sleep(1.50)
        typingPrint( "\nNobody else ascends the hatch while the rest of your men get to the ship. It seems that that was the only marine there.\n" )
        time.sleep(1.50)
        typingPrint( "\nOnce every marine is on board the shuttle, you cautiously approach the hatch. You see that the hatch leads to a second, larger one: an airlock. You and your men descend into the airlock.\n" )
        time.sleep(1.50)
        typingPrint( "\nOne of your men gets to work. He breaks into a control panel and begins fiddling with buttons. Not minutes after you and your men had entered the hatch, the hatch above them is closing, and the hatch below you is descending, an elevator into the ship.\n" )
        time.sleep(1.50)
        descent = 1
        checkpoint = 3.1
        
    else:
        clearScreen()
        typingPrint( "'Contact! Contact! Contact!' You keep your rifle aimed at the hatch as you approach. 'Barlowe: you're with me. The rest of you: follow once everyone has landed.'\n")
        time.sleep(1.50)
        typingPrint( "\n'Right behind you, sergeant,' Barlowe's voice comes over the radio.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou look down into the hatch. You see that the hatch leads to a second, larger one: an airlock. You descend into the airlock, with Barlowe following close behind.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou look around the airlock, searching for any buttons or levers to close the airlock and allow you to enter the rest of the ship. 'Do you see any controls?' you ask Barlowe.\n" )
        time.sleep(1.50)
        typingPrint( "\nBefore Barlowe can say anything, the hatch snaps shuts above your heads, sealing you off from the rest of your team.\n" )
        time.sleep(1.50)
        clearScreen()
        typingPrint( "You feel a pit in your stomach. 'Did you touch anything?'\n" )
        time.sleep(1.50)
        typingPrint( "\n'No,' Barlowe said. 'You didn't either, did you?'\n" )
        time.sleep(1.50)
        typingPrint( "\nYou hear the hiss of air filling the airlock. Once it's pressurized, you feel a jolt, and the two of you start descending. You see that you're going down into the engine room, and you can see three Weltraumwaffe marines with guns drawn, ready to shoot the two of you.\n" )
        time.sleep(1.50)
        typingPrint( "\n'You have a plan, right?' Barlowe asks.\n")
        time.sleep(1.50)
        pickShoot = input( "\nDo you try and shoot the marines, or do you surrender and see if you can talk your way out of this? Enter 1 for shoot, or 2 for surrender:   " )
        if int(pickShoot) == 1:
            clearScreen()
            typingPrint( "You know it isn't your finest idea, but you can't stand the thought of surrendering to Nazis. You draw your weapon and take aim.\n" )
            time.sleep(1.50)
            marine1 = random.randint(1, 3)
            marine2 = random.randint(1, 3)
            marine3 = random.randint(1, 3)
            if marine1 == 1 or marine2 == 2 or marine3 == 3:
                typingPrint( "\nBefore you're able to fire off a shot, one of the Marines fires off a shot with his plasma rifle. The bolt hits you square in the chest.\n" )
                time.sleep(1.50)
                typingPrint( "\nYou hear Barlowe shouting your name, see more shots, and everything fades to black." )
                time.sleep(1.50)
                plzRedo = youSuck()
                if plzRedo == 1:
                    reloadLast()
                else:
                    sys.exit()

            else:
                typingPrint( "\nThe marines shoot at you, and you shoot back. Luckily for you, you're a much better shot than any of them: you're able to shoot all three of them before they shoot you.\n" )
                time.sleep(1.50)
                typingPrint( "\nFrankly, you're shocked. You didn't have opinions on the existence of God, before, but now, you're starting to wonder.\n" )
                time.sleep(1.50)
                typingPrint( "\n'Nice shooting,' Barlowe comments behind you.\n" )
                time.sleep(1.50)
                typingPrint( "\nFor a moment, all you can do is nod.\n" )
                time.sleep(1.50)
                typingPrint( "\n'Open the airlock and get the rest of the team down here,' you order.\n")
                time.sleep(1.50)
                typingPrint( "\n'Aye, sir.' Barlowe begins to fiddle with the airlock controls.")
                descent = 2
                checkpoint = 3.1

        else:
            clearScreen()
            typingPrint( "You only really see one choice. God, though, is it a terrible one.\n" )
            time.sleep(1.50)
            typingPrint( "\n'You aren't going to like it,' you tell Barlowe quietly. 'Follow my lead.'\n" )
            time.sleep(1.50)
            typingPrint( "\n'Aye, sir.'\n" )
            time.sleep(1.50)
            typingPrint( "\nAgainst your better instincts, you drop your weapon and hold your hands up in surrender.\n" )
            time.sleep(1.50)
            typingPrint( "\n'God: I hope you know what you're doing,' you hear Barlowe say.\n" )
            time.sleep(1.50)
            typingPrint( "\nSo do I, you think to yourself." )
            time.sleep(1.50)
            Barlowe = 1
            checkpoint = 3.2

    if checkpoint != 2.1:
        break




#CHECKPOINT 2 - YOU JUMPED LAST
while checkpoint == 2.2:
    pickGo = input( "\nDo you order your men to start going down the hatch, or do you order them to wait until everyone has descended? Enter 1 to order them to go down, or 2 to order them to wait:   " )
    if int(pickGo) == 1:
        clearScreen()
        typingPrint( "\n'Take whatever men you have and go down the hatch,' you order. 'We need to take care of anyone else who might come down that hatch, and we need to take care of them fast.'\n" )
        time.sleep(1.50)
        typingPrint( "\n'Aye sir,' the marine says. 'Going into the hatch.'\n" )
        time.sleep(1.50)
        typingPrint( "\nThe radio cuts, and you see the men already on the ship going into a nearby service hatch.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou land on the ship not long after your team has descended. You're the only one out on the ship's hull, that you can see. The hatch they went down is feet away from you.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou key up the radio, again, heading for the hatch. It's closed - it would seem that they've already descended, and are past the airlock. 'Team one: do you have airlock control?'\n" )
        time.sleep(1.50)
        typingPrint( "\n'We do,' someone confirms. 'Get into the airlock, and we'll bring you into the ship.'\n" )
        time.sleep(1.50)
        clearScreen()
        marinesShoot = random.randint(1, 2)
        if marinesShoot == 1:
            typingPrint( "You approach the hatch and begin to open it.\n" )
            time.sleep(1.50)
            typingPrint( "\nBefore you can get it open, there's a bright flash of plasma that barely misses you.\n" )
            time.sleep(1.50)
            typingPrint( "\nYou turn, swearing under your breath. There's three Weltraumwaffen marines coming towards you on the hull.\n" )
            time.sleep(1.50)
            pickSurrender = input( "\nDo you surrender, or do you shoot back? Enter 1 for surrender, or 2 for shoot back:   " )
            if int(pickSurrender) == 1:
                clearScreen()
                typingPrint( "The odds in this fight aren't exactly in your favor. Even if you manage to shoot one, one of the other two will likely shoot you. Your odds of surviving this won't be the best if you get captured, but they'll still be better than if they were to shoot a hole through your suit.\n" )
                time.sleep(1.50)
                typingPrint( "\nYou key up your radio as you put your hands up. 'Team: slight problem.'" )
                Barlowe = 0
                checkpoint = 3.2
            else:
                clearScreen()
                typingPrint( "You know it isn't your finest idea, but you can't stand the thought of surrendering to Nazis. You draw your weapon and take aim.\n" )
                time.sleep(1.50)
                marine1 = random.randint(1, 3)
                marine2 = random.randint(1, 3)
                marine3 = random.randint(1, 3)
                if marine1 == 1 or marine2 == 2 or marine3 == 3:
                    typingPrint( "\nBefore you're able to fire off a shot, one of the Marines fires off a shot with his plasma rifle. The bolt hits you square in the chest.\n" )
                    time.sleep(1.50)
                    typingPrint( "\nThe last thing you hear is the air rushing out of your suit." )
                    time.sleep(1.50)
                    plzRedo = youSuck()
                    if plzRedo == 1:
                        reloadLast()
                    else:
                        sys.exit()

                else:
                    typingPrint( "\nThe marines shoot at you, and you shoot back. Luckily for you, you're a much better shot than any of them: you're able to shoot all three of them before they shoot you.\n" )
                    time.sleep(1.50)
                    typingPrint( "\nFrankly, you're shocked. You didn't have opinions on the existence of God, before, but now, you're starting to wonder.\n" )
                    time.sleep(1.50)                        
                    typingPrint( "\nYou get back to the hatch and rush to open it up. You key up the radio as you do: 'This ship is starting to crawl with marines - let's get this done. Fast!'\n" )
                    time.sleep(1.50)
                    typingPrint( "\nOnce the hatch is open, you descend into the airlock, and wait for your team to lower you into the ship." )
                    time.sleep(1.50)
                    descent = 1
                    checkpoint = 3.1    

        else:
            typingPrint( "You approach the hatch and begin to open it.\n" )
            time.sleep(1.50)
            typingPrint( "\nYou just about have it open when you feel something hit you in the back. Suddenly, your entire exoskeleton goes rigid. You can't move.\n" )
            time.sleep(1.50)
            typingPrint( "\nYou can't move your head to look, but you can see them out of the corner of your eye: a group of Weltraumwaffe marines heading towards you, and two steel cables leading from your back to the group. You recognize it: it's a taser, used to disable the exoskeletons used by Unified Space Command Marines.\n" )
            time.sleep(1.50)
            typingPrint( "\nYou swear under your breath. This isn't good.\n" )
            Barlowe = 0
            checkpoint = 3.2

    else:
        clearScreen()
        typingPrint( "'Hold until we get down there,' you say. 'We'll all head down together.'" )
        time.sleep(1.50)
        clearScreen()
        typingPrint( "\nOnce every marine is on board the shuttle, you cautiously approach the hatch. You see that the hatch leads to a second, larger one: an airlock. You and your men descend into the airlock.\n" )
        time.sleep(1.50)
        typingPrint( "One of your men gets to work. He breaks into a control panel and begins fiddling with buttons. Not minutes after you and your men had entered the hatch, the hatch above them is closing, and the hatch below you is descending, an elevator into the ship.\n" )
        descent = 1
        checkpoint = 3.1

    if checkpoint != 2.2:
        break



#CHECKPOINT 3.1 - FREEBIRD
while checkpoint == 3.1:
    if int(pickBulkhead) == 1:
        if descent == 1:
            clearScreen()
            typingPrint( "You are surrounded by a myriad of machinery once you descend into the artifical gravity." )
        else:
            clearScreen()
            typingPrint( "You look around the room as Barlowe opens the airlock and allows the rest of the team in.")    
        typingPrint("It appears that the hatch has dropped you directly into the engine room. Nobody else is in the immediate vicinity.\n" )
        time.sleep(1.50)
        typingPrint( "\n'Keep your eyes peeled,' you instruct your men. The command is unnecessary - all of them are at the ready, prepared for an attack. You and your men need to move quickly to secure the engine room.\n" )
        time.sleep(1.50)
        pickSplit = input( "\nDoes your team split up to secure the engine room, or do you all stick together? Enter 1 for split up, or 2 for stick together:   " )
        if int(pickSplit) == 1:
            clearScreen()
            typingPrint( "You need to work quickly - you have no idea how much time you have to take this ship. Dividing and conquering seems to be the best option\n" )
            time.sleep(1.50)
            typingPrint( "'We'll split up,' you say. 'Team one: you'll go left. Team two: you'll go right. Secure this area, and look for the engine controls. Radio in when you find them. Clear?'\n" )
            time.sleep(1.50)
            typingPrint( "\nNone of the men voice questions, or objections.\n")
            time.sleep(1.50)
            pickT1 = input( "\nWill you go with team one, or team two? Enter 1 for team one, or 2 for team two:   ")
            if int(pickT1) == 1:
                team = "team one"
            else:
                team = "team two"
            clearScreen()
            typingPrint( "\n'I'll go with " + team + "' you say. 'Keep your wits about you. If you find anything, or run into any trouble, call it over the radio.'\n" )
            time.sleep(1.50)
            typingPrint( "\nWith that, your squad splits. You and " + team + " head to the right, while the others go to the left." )
            time.sleep(1.50)
            checkpoint = 4.1

        else:
            clearScreen()
            typingPrint( "You need to work quickly - you have no idea how much time you have to take this ship. Focusing your efforts - and all of your men - on disabling the ship seems like the best course of action.\n" )
            time.sleep(1.50)
            typingPrint( "\n'Stick close,' you order your men. 'Barlowe: how well did you study the engine room map?'\n")
            time.sleep(1.50)
            typingPrint( "\n'I know it like the back of my hand,' Barlowe says.\n" )
            time.sleep(1.50)
            typingPrint( "\n'You're on point, then,' you say. 'We need to get to the engine controls and disable them.'\n" )
            time.sleep(1.50)
            typingPrint( "\n'Aye, sir,' Barlowe says. He gets in front of everyone, and begins to lead the group through the engine room.\n" )
            time.sleep(1.50)
            checkpoint = 4.1

    else:
        clearScreen()
        typingPrint( "Your feet slowly descend with the elevator as you descend into the artificial gravity. You find yourself in a long room. Along each wall, you see a row of lockers with nameplates on them. It seems that the forward hatch has dropped you into an equipment locker.\n" )
        time.sleep(1.50)
        typingPrint( "\nYour men post up. All of your men, but Barlowe, your point man. Instead, he pulls up a map of the ship.\n")
        time.sleep(1.50)
        typingPrint( "\n'We're close to the bridge,' he says, pointing to your location. 'We're also close to comms. And, unfortunately, a guard station.'\n" )
        time.sleep(1.50)
        typingPrint( "\nYou curse under your breath. That's not what you want to hear.\n" )
        time.sleep(1.50)
        typingPrint( "\n'What do you want to do next?' Barlowe asks.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou consider it for a few moments. You can split up your team, take out their communications and their Marines at the same time, but that potentially exposes your men more than necessary. Or, you can keep your squad together and overwhelm one section of the ship, but possibly give them more time to respond.\n" )
        time.sleep(1.50)
        pickSplit = input("\nDo you want to split your squad up, or will you move together? Enter 1 for split up, or 2 to stick together:   ")
        checkpoint = 4.2

    if checkpoint != 3.1:
        break



#CHECKPOINT 3.2 - JAILBIRD
while checkpoint == 3.2:
    clearScreen()
    typingPrint( "Not long after, you find yourself in the Saalwachter's brig, stripped of your weapons, exoskeleton, and space suit. ")
    if Barlowe == 0:
        typingPrint( "You haven't heard anything about your men, but you also haven't seen anyone else come into the brig. ")
    else:
        typingPrint( "You know that Barlowe is in the cell next to yours, but otherwise, you haven't heard anything about the rest of your men. You also haven't seen anyone else come into the brig. ") 
    typingPrint( "Red warning lights have been flashing outside your cell since you arrived - based on those two signs, you're pretty sure they're just fine. It's not an ideal situation, but knowing the stories about what the Nazis did during the ground war, you know you could be much worse off.\n" )
    time.sleep(1.50)
    typingPrint( "\nYou hear the brig door open. A few seconds later, the door to your cell opens. On the other side, you see an older, well-dressed man. A captain, according to the dark gray uniform. There are two marines on either side of him with plasma rifles, ready to shoot.\n" )
    time.sleep(1.50)
    pickStand = input( "\n'Do you stand out of respect for an officer, or do you stay sitting? Enter 1 for stand, or 2 for sit:   " )
    if int(pickStand) == 1:
        clearScreen()
        typingPrint( "You stand up. A little respect goes a long way, and that little respect might mean life or death to your men. " )
        if Barlowe == 1:
            typingPrint( "Particularly Barlowe.\n" )
        time.sleep(1.50)
        typingPrint( "\n'Captain,' you say.\n" )
        time.sleep(1.50)
        typingPrint( "\nThe captain gives a curt nod. 'Captain Ehrling, to be precise. And to whom do I owe the pleasure?" )
        time.sleep(1.50)
    else:
        clearScreen()
        typingPrint( "With any other officer, for any other military, you would probably stand out of respect. This is a Nazi officer, though. He doesn't deserve your respect.\n" )
        time.sleep(1.50)
        typingPrint( "\nOne of the Marines moves towards you, as if to pull you to your feet, but he stops when the Captain holds his hand up.\n" )
        time.sleep(1.50)
        typingPrint( "\n'My name is Captain Ehrling, and I'm the commander of this ship,' he says. 'And who might you be?'\n")
        time.sleep(1.50)
    pickTough = input( "\nDo you play tough? Do you cooperate? Do you stay silent? Enter 1 to play tough, 2 to cooperate, or 3 to stay silent:   " )
    if int(pickTough) == 1:
        clearScreen()
        typingPrint( "'That's need-to-know,' you say." )
        time.sleep(1.50)
        typingPrint( "\nCaptain Ehrling gives you a long, hard stare.\n" )
        time.sleep(1.50)
    if int(pickTough) == 2:
        clearScreen()
        typingPrint( "'My name is Sergeant " + Name2 + ", USPCS Farragut,' you say.\n" )
        time.sleep(1.50)
    else:
        clearScreen()
        typingPrint( "You don't answer.\n" )
        time.sleep(1.50)
    if int(pickTough) == 1 or int(pickTough) == 3:
        captAct = random.randint(1,2)
        if captAct == 1 and int(pickStand) == 1:
            typingPrint( "\nCaptain Ehrling gives a nod to one of the Marines. That Marine hits you in the stomach with the butt of his rifle, hard.\n" )
            time.sleep(1.50)
            typingPrint( "\nYou gasp as the air gets knocked out of your lungs. You fall to one knee, arms wrapped around your stomach.\n" )
            brokeRib = random.randint(1,5)
            if brokeRib == 1:
                typingPrint( "You think he might have just broken a rib." )
                time.sleep(1.50)
        typingPrint( "\n'I might have more respect, if I were you,' Captain Ehrling says. Any hint of warmth he might have had has now vanished." )
        if Barlowe == 1:
            typingPrint( "'If not for your sake, then for the sake of your man in the next cell.'\n" )
            time.sleep(1.50)
            typingPrint( "\nYou have to fight to keep from looking away from the captain and at the wall separating you from Barlowe. You can accept the fact that they'll likely do something horrible to you, and you know that Barlowe can, as well. Still: you need to consider what they'll do to him with everything you say or do.\n")
    else:
        typingPrint( "\n'The Farragut,' Ehrling echoes. 'My ship seems like a humble target for Unified Space Command's flagship.'")
        time.sleep(1.50)
        typingPrint( "\nYou clench your fists at your side. Why is he bothering with this?")  
    time.sleep(1.50)
    clearScreen()
    typingPrint( "'What do you want?' you ask.\n" )
    time.sleep(1.50)
    typingPrint( "\n'I want you to either surrender your men, or get them off this ship,' Captain Ehrling says.\n" )
    time.sleep(1.50)
    typingPrint( "\n'And if I refuse?' you ask.\n" )
    time.sleep(1.50)
    if Barlowe == 0:
        typingPrint( "\nCaptain Ehrling nods to one of the Marines.\n" )
        time.sleep(1.50)
        typingPrint( "\nIn response, the Marine points the rifle directly at you. The implication is clear.\n" )
        time.sleep(1.50)
    if Barlowe == 1:
        typingPrint( "\n'Then I throw your man out the nearest airlock.' Captain Ehrling's voice is blunt. 'And you'll be next.'\n" )
        time.sleep(1.50)
    typingPrint( "\nYou see two options available to you: cooperate and try to pull one over on the captain, or refuse and hope he's bluffing.\n" )
    time.sleep(1.50)
    pickCallBluff = input( "\nDo you cooperate, or do you call his bluff? Enter 1 for surrender, or 2 to call his bluff:   ")
    if int(pickCallBluff) == 1:
        clearScreen()
        typingPrint( "The success of the mission is one of your top priorities. You don't doubt that the Nazis would kill you and your men. You only see one way for your team to succeed. As much as it pains you to think about.\n" )
        time.sleep(1.50)
        typingPrint( "\n'Alright,' you say. 'I'll do it.'\n")
        time.sleep(1.50)
        typingPrint( "\nThe captain nods. You see the hint of a smile on his face.\n" )
        time.sleep(1.50)
        typingPrint( "\nHe says something to the marines on either side of him. In response, one of them approaches you and handcuffs your hands behind your back.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou get a sinking feeling in your stomach. 'Where are you taking me?'\n" )
        time.sleep(1.50)
        typingPrint( "\n'The bridge,' the captain says. 'You can't give orders to your men from here.'")
        time.sleep(1.50)
        clearScreen()
        checkpoint = 4.3

    else:
        clearScreen()
        typingPrint( "You know what your answer needs to be.\n" )
        time.sleep(1.50)
        typingPrint( "\n'I won't surrender my men,' you say.")
        time.sleep(1.50)
        typingPrint( "\nThe look on Ehrling's face sours. He doesn't say anything for a few seconds.\n" )
        time.sleep(1.50)
        if Barlowe == 0:
            typingPrint( "\n'Throw him out the airlock,' he says." )
            time.sleep(1.50)
        if Barlowe == 1:
            typingPrint( "\n'Throw both of them out the airlock,' he says. ")
        checkpoint = 4.3
    if checkpoint != 3.2:
        break



#CHECKPOINT 4.1 - ENGINE ROOM
while checkpoint == 4.1:
    problem = 0
    typingPrint( "\nYou and the other members of your team move quickly through the engine room. You meet little resistance. This fact might have been concerning to you, had you not paid attention to the brief you received before the mission. The cruiser wasn't any smaller than the other ships of the Weltraumwaffe's fleet, but most of the controls of this ship were automated. At least, by G2's estimation, they were. Allied scientists theorized they could crew this entire ship with only twenty men. You don't hear any calls of contact over the radio, either - it would seem that the engine room is truly as sparsely manned as the powers-that-be estimated.\n" )
    time.sleep(1.50)
    typingPrint( "\nAfter searching the engine room, you come upon what you'd hoped you'd find: a computer terminal. Judging by the vast amount of machinery behind it, you're confident that this is the engine control panel you'd hoped to find.\n" )
    time.sleep(1.50)
    typingPrint( "\nThere's only one problem: it's currently manned. The Weltraumwaffe engineer has his back to you as he types controls into the terminal. The sound of the engines seems to have disguised your approach, for now. Still: you'll need to get him off the computer if you want to access it.\n" )
    time.sleep(1.50)
    pickIncap = input( "\nDo you sneak up behind him and knock him out, or do you see if he'll surrender? Enter 1 for knock him out, or 2 for get him to surrender:   \n")
    if int(pickIncap) == 1:
        clearScreen()
        typingPrint( "You know you need to keep things quiet. If you startle the engineer, he might trip some sort of alarm. You slowly approach him from behind, hoping he doesn't decide to turn around.\n")
        engineerSees = random.randint(1, 2)
        if engineerSees == 1:
            typingPrint( "\nHe doesn't seem to notice your aproach.\n" )
            pickChokehold = input( "\nDo you put him in a chokehold and pull him away from the controls, or do you use the butt of your plasma rifle? Enter 1 for chokehold, or 2 for the butt of your plasma rifle:   ")
            if int(pickChokehold) == 1:
                clearScreen()
                typingPrint( "You slowly sling your rifle, again. Before he can notice your approach, you wrap one arm around his neck and cover his mouth with your other hand. He struggles against you, but you're able to pull him away from the controls.\n" )
            else:
                clearScreen()
                typingPrint( "You ready your rifle. You don't want too much of a struggle - the faster he's unconscious, the better.\n" )
                time.sleep(1.50)
                typingPrint( "\nYou raise your rifle and hit him on the back of his head, hard.\n" )
                time.sleep(1.50)
                fallDown = random.randint(1, 3)
                if fallDown <= 2:
                    typingPrint( "\nThe engineer crumbles to the ground.\n" )
                if fallDown == 3:
                    typingPrint( "\nThe engineer crumbles to the ground. Before he does, however, he hits the the computer.")
                    alarmGoes = 2
                    checkpoint = 5.1

            time.sleep(1.50)
            typingPrint( "\nOne of your men, Simons, gets onto the computer and begins to type faster than you'd ever seen, before.\n" )
            time.sleep(1.50)
            typingPrint( "\nStill: it feels like he's working at a snail's pace. 'Any time, now!'\n" )
            time.sleep(1.50)
            typingPrint( "\nSimon doesn't look over at you. 'I just... need to find the right controls..." )
            time.sleep(1.50)
            clearScreen()
            alarmGoes = random.randint(1, 2)
            checkpoint = 5.1

        else:
            typingPrint( "\nBefore you can grab him, however, he turns around and sees you.\n" )
            time.sleep(1.50)
            typingPrint( "\nYou have to act quickly. If he alerts the ship, your crew could be in for a fight.\n" )
            time.sleep(1.50)
            engineerFight = input( "\nDo you try and grapple him, or do you threaten him with your rifle? Enter 1 for grapple, or 2 for threaten him with your rifle:   ")
            clearScreen()
            if int(engineerFight) == 1:
                typingPrint( "Without a moment's delay, you rush forward and grab the engineer." )
                time.sleep(1.50)
                winGrapple = random.randint(1, 3)
                if winGrapple <= 2:
                    typingPrint( "\nYou've managed to get the jump on the engineer. You're able to get him into a headlock and pull him away from the computer, allowing one of your men, Simons, to get onto the console and begin typing at a rapid click.\n" )
                    time.sleep(1.50)
                    typingPrint( "\nStill: it feels like he's working at a snail's pace as you fight to keep the engineer subdued long enough to choke him out. 'Any time, now!'\n" )
                    time.sleep(1.50)
                    typingPrint( "\nSimon doesn't look over at you. 'I just... need to find the right controls..." )
                    time.sleep(1.50)
                    clearScreen()
                    alarmGoes = random.randint(1, 2)
                    checkpoint = 5.1

                if winGrapple == 3:
                    typingPrint( "\nYou were expecting the engineer to be easy to subdue, but he's a better grappler than you might've expected. The two of you struggle for a few seconds before he manages to slip away and slam a button on the keyboard." )
                    time.sleep(1.50)
                    clearScreen()
                    problem = 1
                    alarmGoes = 2
                    checkpoint = 5.1

            else:
                typingPrint( "You hold up your rifle, pointing it directly at the Engineer's chest.\n" )
                time.sleep(1.50)

    else:
        clearScreen()
        typingPrint( "You slowly approach him. Once you're within arms length of him, you lift the rifle and press the barrel to the back of his head.\n"  )
        time.sleep(1.50)
    typingPrint ( "\n'Hands off the keyboard!' you yell over the sound of the engines. 'Step away from the computer!'\n " )
    engineerActs = random.randint(1, 4)
    if engineerActs == 1:
        typingPrint( "\nEngineer complies, slowly putting his hands in the air. His hands are shaking.\n" )
    if engineerActs == 2:
        typingPrint( "\nFor a few seconds, he does nothing. Just stands there. His hands are on the keyboard.\n" )
        time.sleep(1.50)
        typingPrint( "\nThen, he smashes a button on the keyboard.\n" )
        time.sleep(1.50)
        clearScreen()
        problem = 1
        alarmGoes = 2
        checkpoint = 5.1

    if engineerActs == 3 and int(pickIncap) == 2:
        typingPrint( "\nWithout warning, he shoves back, knocking you backwards.\n")
        time.sleep(1.50)
        typingPrint( "\nYou stumble backwards. Before you can grab him, again, the engineer smashes a button on the keyboard." )
        time.sleep(1.50)
        clearScreen()
        problem = 1
        alarmGoes = 2
        checkpoint = 5.1

    else:
        typingPrint( "\nWithout warning, the engineer lunges for you and your weapon.\n" )
        time.sleep(1.50)
        winGrapple = random.randint(1, 3)
        if winGrapple == 1:
            typingPrint( "\nThe engineer is fast, but you're faster. The two of you struggle, but in the end, you're able to put him in a chokehold with your rifle and pull him away from the computer, allowing one of your men, Simons, to hop onto the computer, where he begins typing at an incredible clip.\n")
            time.sleep(1.50)
            typingPrint( "\nStill: it feels like he's working at a snail's pace as you fight to keep the engineer subdued long enough to choke him out. 'Any time, now!'\n" )
            time.sleep(1.50)
            typingPrint( "\nSimon doesn't look over at you. 'I just... need to find the right controls..." )
            time.sleep(1.50)
            clearScreen()
            alarmGoes = random.randint(1, 2)
            checkpoint = 5.1
            
        else:
            typingPrint( "\nThe engineer catches you off guard. The two of you begin to struggle, but it isn't long before he manages to get your rifle out of your hands and takes aim directly at you.\n" )
            time.sleep(1.50)
            typingPrint( "\nYou expect him to shoot you, but instead, while holding the rifle up with one hand, smashes a button on the keyboard.\n" )
            time.sleep(1.50)
            problem = 1
            alarmGoes = 2
            checkpoint = 5.1


    if checkpoint != 4.1:
        break
    


#CHECKPOINT 4.2 - AFT
while checkpoint == 4.2:
    if int(pickSplit) == 1:
        clearScreen()
        typingPrint( "'We'll split up, focus our efforts on eliminating their comms and that guard station,' you say. 'Once we have those under control, we'll be able to get the bridge - and the rest of the ship - under control.'\n" )
        time.sleep(1.50)
    else:
        clearScreen() 
        typingPrint( "'We'll stick together,' you say. 'We'll have an easier time putting down any resistance they might mount that way.'\n" )
        time.sleep(1.50)
        typingPrint( "\n'Where do you want to focus our efforts?' Barlowe asks.\n" )
        time.sleep(1.50)
    pickTeam = input( "\nWill you go to the guard station, or will you go to the communications room? Enter 1 for guard station, or 2 for communications room:   " )
    if int(pickTeam) == 1:
        team = "guard station"
        other = "communications room"
    if int(pickTeam) == 2:
        team = "communications room"
        other = "guard station"
    if int(pickSplit) == 1:
        typingPrint( "'Team one and myself will go to the " + team + ",' you say. 'Team two will go to the " + other + ". Any questions?'\n" )
        time.sleep(1.50)
    else:
        typingPrint( "'We'll focus on the " + team + "', you say. 'Once we have that secure, we can focus on the " + other + ". Any other questions?'\n" )
        time.sleep(1.50)
    typingPrint( "\nEveryone stays quiet.\n" )
    time.sleep(1.50)
    typingPrint( "\nYou nod. 'Let's hustle, then. Good luck, gentlemen.\n" )
    clearScreen()
    if int(pickTeam) == 1:
        typingPrint( "The guard room is close to the storage locker you entered the ship from. You lead them through the quiet corridors of the ship, until you see the right bulkhead door in front of you. The door is closed - from where you are, it appears to be locked.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou signal your team to stop.")
        if int(pickSplit) == 1:
            typingPrint("One of them points his rifle down the way you came. The other - Barlowe - points his rifle towards the bulkhead door.\n" )
        else:
            typingPrint( "Half of the men point their rifles down the way you came. The other half take aim at the bulkhead door. Barlowe, however, stays standing next to you.\n" )
        time.sleep(1.50)
        typingPrint( "\n'How do you want to do this?' Barlowe asks.\n" )
        time.sleep(1.50)
        typingPrint( "\nNormally, you might watch the door and wait until a guard change, use the open door and few seconds of lower security to your advantage. You know you're on a time crunch, however - that limits your options.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou can think of two things to do that will work with your limited time: you can try to breach the door, or you can try to get them to open it on their own.\n" )
        time.sleep(1.50)
        pickBreach = input( "\nDo you breach the door, or do you try to get the guards on the other side to open it for you? Enter 1 for breach, or 2 to trick the guards:   " )
        if int(pickBreach) == 1:
            clearScreen()
            typingPrint( "You don't know how long you have before the Saalwachter's crew catches on to what you're doing - breaching seems like the best thing you can do.\n" )
            time.sleep(1.50)
            typingPrint( "\n'Do you have any breaching charges left?' you ask Barlowe.\n" )
            time.sleep(1.50)
            typingPrint( "\nBarlowe gives a nod.\n" )
            time.sleep(1.50)
            typingPrint( "\n'How long do you need to set them on that door?'\n" )
            time.sleep(1.50)
            typingPrint( "\n'Not long,' Barlowe says. 'I can have it done in a few minutes; I'll just need someone to cover me.\n" )
            time.sleep(1.50)
            if int(pickTeam) == 1:
                typingPrint( "\nYou nod and give the orders to the team: 'Move up to the door: we're covering Barlowe.'\n" )
                time.sleep(1.50)
            else:
                typingPrint( "\nYou nod and give the orders to the squad: 'We're moving to the door. Singh: you and me are covering Barlowe. The rest of you: watch the hallway and prepare to breach.'\n" )
                time.sleep(1.50)

            clearScreen()
            typingPrint( "You and your team line up to breach the " + team + ".'" )
            time.sleep(1.50)
            if int(pickTeam) == 1:
                checkpoint = 5.2
            if int(pickTeam) == 2:
                checkpoint = 5.3

        else:
            clearScreen()
            typingPrint( "You're worried that using explosives will not only expose whoever is planting them, but could severely damage the ship, potentially putting you and your men in danger. Getting them to open the door of their own valition seems like the best course of action.\n" )
            time.sleep(1.50)
            typingPrint( "\nYou look over your men. 'Cohen: you speak German, don't you?'\n" )
            time.sleep(1.50)
            typingPrint( "\nCohen looks up from his position guarding the rear. 'Aye, sir.'\n" )
            time.sleep(1.50)
            typingPrint( "\n'You're with me,' you say. " )
            if int(pickSplit) == 2:
                typingPrint( "'The rest of you: get ready to storm the bulkhead.'\n" )
            time.sleep(1.50)

            clearScreen()
            typingPrint( "You, Barlowe, and Cohen take up a position by the door. Cohen is standing in front of the bulkhead door. Barlowe is standing to the side, taking aim at whoever will end up opening the bulkhead door.\n" )
            time.sleep(1.50)
            typingPrint( "\nCohen looks to you. 'What do you want me to say?'\n" )
            time.sleep(1.50)
            typingPrint( "\n'Whatever you think will get them to open that door,' you say.\n" )
            time.sleep(1.50)
            typingPrint( "\nCohen considers his words for a few seconds, then knocks on the door, speaking in what to your ears sounds like perfect German. You just hope that it's passable to the Germans.\n" )
            if int(pickTeam) == 1:
                checkpoint = 5.2
            if int(pickTeam) == 2:
                checkpoint = 5.3
        
    if checkpoint != 4.2:
        break




#CHECKPOINT 4.3 - RESCUE, IN PROGRESS
while checkpoint == 4.3:
    clearScreen()
    if int(pickCallBluff) == 1:
        typingPrint( "You, the guards, and the captain walk through the ship to the bridge without incident. They leave the handcuffs off of you, this time, but it's still clear to you that the guards don't trust you: one of them keeps his plasma pistol jammed into your back. You do your best to keep your cool, but you're nervous. You know that you have to come up with a plan, and you have to come up with a plan fast. Most of your ideas, however, feel like the end with you getting shot.\n" )
        time.sleep(1.50)
        if Barlowe == 1:
            typingPrint( "\nEven with the gun pointed in your back, and even with the stress of trying to find a way to get yourself out of this situation, a lot of your concerns lay with one person, notably missing from your group.\n" )
            time.sleep(1.50)
            typingPrint( "\n'Where's my man?' you ask.\n" )
            time.sleep(1.50)
            typingPrint( "\n'Mister Barlowe, you mean?' Captain Ehrling asks. 'He will be staying behind. Assurance that you won't try something uncouth.'\n" )
            time.sleep(1.50)
            typingPrint( "\nYou clench your fists at your sides. 'How do I know that he's even alive, still? Or that you won't just throw him out the airlock, anyway?'\n" )
            time.sleep(1.50)
            typingPrint( "\n'You'll just have to have a little faith.'\n" )
            time.sleep(1.50)
            typingPrint( "\nThat's not the answer you wanted to hear, but for the moment, you don't know that you have another choice. For the moment, you'll just have to hope that you're right in your belief that Barlowe is more valuable to them alive than dead. And you're fairly certain that Ehrling knows that.\n" )
            time.sleep(1.50)
            clearScreen()
        typingPrint( "\nThe bridge is surprisingly small, considering the size of the ship - just a captain's chair and a handful of technicians at computers.\n" )
        time.sleep(1.50)
        typingPrint( "\nOne of the guards shouts commands in German as your group walks into the bridge. The technicians immediately stand up at attention, facing the captain as he enters the bridge.\n" )
        time.sleep(1.50)
        typingPrint( "\nEhrling gives another command as he takes his seat. Everyone else in the bridge follows suit.\n" )
        time.sleep(1.50)
        typingPrint( "\nEhrling says something to the guards. They bring you to the captain's chair, where you see an intercom mic.\n" )
        time.sleep(1.50)
        typingPrint( "\nEhrling hands you the intercom mic. 'Go ahead, Sergeant. Address your team.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou hesitate before taking the mic. You see a couple options ahead of you. One: try to covertly convey information to your team that will help them accomplish the mission. Two: flat-out defy Ehrling's instructions, and hope they don't kill you. ")
        if Barlowe == 1:
            typingPrint( "Or Barlowe." )
        time.sleep(1.50)
        pickCovert = input( "\nDo you try and covertly give your team information over the ship's intercom, or do you defy Ehrling? Enter 1 to give covert instructions, or 2 to defy Ehrling:   ")

        clearScreen()
        typingPrint( "\nYou take a deep breath before pressing the push-to-talk button on the side of the mic. 'This is Sergeant " + Name2 + ", addressing my men on this ship. If you can hear me, find an intercom mic.\n" )
        time.sleep(1.50)
        typingPrint( "\nThe ship stays silent for a few seconds. Long enough that you're worried that they might not have heard you, or might not be able to get to a mic.\n" )
        time.sleep(1.50)
        typingPrint( "\nFinally, though, you hear a familiar voice over the intercom: 'Sergeant " + Name2 + ", go ahead.'\n" )
        time.sleep(1.50)
        typingPrint( "\nYou shoot a glance at Ehrling before you speak next. You pray that this ends well for you and your men." )
        time.sleep(1.50)
        clearScreen()
        if int(pickCovert) == 1:
            pass
        else:
            pass

    else:
        typingPrint( "The guards lead you through the ship, while Ehrling goes back to the bridge. You have three on you: two holding you by either forearm, and one with a plasma pistol aimed at your back. Your hands are cuffed behind your back. " )
        if Barlowe == 1:
            typingPrint( "Barlowe, you know, is somewhere behind you, with more guards on him. Between the two of you, it seems like most of the marines on that ship are likely on guard duty with the two of you." )
        typingPrint( "Overall, escape seems unlikely, and you know that you likely don't have much time to come to terms with that fact.\n" )
        time.sleep(1.50)
        teamAmbush = random.randint(1, 2)
        if teamAmbush == 1:
            pass
        else:
            pass

    if checkpoint != 4.3:
        break



#CHECKPOINT 5.1 - ENGINE ROOM COMPUTER, IN PROGRESS
while checkpoint == 5.1:
    if alarmGoes == 1:
        typingPrint( "\nThe whine of the engine slowly dies down.\n" )
        time.sleep(1.50)
        typingPrint( "\n'Engines are down,' Simons says. 'Whatever you need, I've got it.'\n" )
        time.sleep(1.50)
        typingPrint( "\nThe engineer falls limp in your arms, unconscious.\n" )
        time.sleep(1.50)
        typingPrint( "\n'Fine work,' you say as you slowly lower the engineer to the ground.\n" )
        time.sleep(1.50)
        pickSend = input( "\nDo you send the other team to clear the rest of the ship, or do you call the bridge and get them to surrender? Enter 1 to send the other team, or 2 to call the bridge:   " )
        if int(pickSend) == 1:
            clearScreen()
            typingPrint( "Even if you do have control of the ship from the engine room, you and your men are still outnumbered. You need to take the bridge quickly, and you need to maintain control of the engine room.\n" )
            time.sleep(1.50)
            if int(pickSplit) == 1:
                typingPrint( "\nYou call out over the radio: 'Team two leader: do you copy?'\n" )
                time.sleep(1.50)
                typingPrint( "\nA few moments later, you hear another voice over the intercom: 'Good copy, Sergeant " + Name2 + ".'\n" )
                time.sleep(1.50)
                typingPrint( "\n'We've taken control of the ship's computer,' you say. 'You and your team need to take the bridge. We'll support you from here as much as we can.'\n" )
                time.sleep(1.50)
                typingPrint( "\n'Aye, sir,' the team leader says. 'Moving towards the bridge now.'\n" )
                time.sleep(1.50)
                typingPrint( "\nMore static crackles in your headset, then all falls silent." )
                time.sleep(1.50)
                clearScreen()
            else:
                pass
            typingPrint( "You look to Simons at the controls. 'What can you access to help them?'\n" )
            time.sleep(1.50)
            typingPrint( "\n'I have access to the whole ship,' Simons says. 'Lights, life support systems, the works. What do you want to do?'" )
            time.sleep(1.50)
            typingPrint( "\nYou consider that for a few moments. You can think of a few systems that could help them if you cut them: life support systems, and the electrical, in particular. Cutting life support would cause the ship's crew to pass out, assuming nobody in the bridge noticed. If they did, they could send a distress signal to a larger ship. If you turn off the electrical, you might be able to cut off their communications, but it might not do much to slow down the crew, themselves. Either way, you'll risk the crew coming to investigate why the engines have stopped.\n" )
            time.sleep(1.50)
            pickLSSys = input( "\nDo you cut off the life support, or do you cut off the electronics? Enter 1 for life support, or 2 for electronics:    " )
            if int(pickLSSys) == 1:
                clearScreen()
                typingPrint( "'Cut off life support,' you say. 'Will you be able to see any distress signals this ship tries to send?'\n" )
                time.sleep(1.50)
                typingPrint( "\n'Yes, sir,' Simons says as he types into the terminal. 'I'll do what I can to block outgoing transmissions.'\n" )
                time.sleep(1.50)
                typingPrint( "\nYou give a nod, then speak into your suit's radio: 'Team two: life support systems are going dark. That should send them scrambling long enough for you to take the bridge.'\n" )
                time.sleep(1.50)
                typingPrint( "\n'Roger, sir,' the voice crackles in your headset.\n" )
                time.sleep(1.50)
                typingPrint( "\nMoments later, you hear the ship around you grow just that much quieter as the air stops circulating. You see something flashing on the terminal in front of Simons - a warning about the life support system, no doubt.\n" )
                time.sleep(1.50)
                typingPrint( "\n'Can anyone on the bridge see that?' You ask.\n" )
                time.sleep(1.50)
                firstSpeak = 2
                bridgeActs = random.randint(1, 2)
                checkpoint = 6.1

            else:
                clearScreen()
                typingPrint( "'Can you cut the electricity everywhere but in here?' You ask.\n" )
                time.sleep(1.50)
                typingPrint( "\n'That shouldn't be too hard,' Simons says as he types.\n" )
                time.sleep(1.50)
                typingPrint( "\nYou call up the other team on the radio: 'Team two: the ship's about to go dark.'\n" )
                time.sleep(1.50)
                typingPrint( "\n'Roger.'\n")
                time.sleep(1.50)
                typingPrint( "\nRight as he says it, the lights flicker, but stay on. 'Lights are off everywhere but here, sergeant,' Simons says." )
        else:
            clearScreen()
            typingPrint( "The most important thing for you to do is hold the engine room - keeping your men in the engine room with you is the best decision you can make.\n" )
            time.sleep(1.50)
            typingPrint( "\nYou see an intercom mic next to the terminal. 'Simons: can you patch me to the bridge?' You ask.\n" )
            time.sleep(1.50)
            typingPrint( "\n'Of course.'\n" )
            time.sleep(1.50)
            typingPrint( "\n'Do it,' you say as you pick up the intercom mic.\n" )
            time.sleep(1.50)
            typingPrint( "\nSimons types, then looks up at you. 'Go ahead.'\n" )
            time.sleep(1.50)
            firstSpeak = 1
            checkpoint = 6.1
    if alarmGoes == 2 and problem == 0:
        clearScreen()
        typingPrint( "An alarm begins to sound.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou curse, looking to Simons. 'What the hell did you do?!'\n" )
        time.sleep(1.50)
        typingPrint( "\n'I... think they changed their computer security on this class ship,' Simons says. 'As it turns out: brute force attacks set off the ship's security alarms.'\n" )
        time.sleep(1.50)
        typingPrint( "\nYou rack your brain for ideas. You can destroy the computer and go on the offensive, or you can go on the defensive and hold the engine room.\n" )
        time.sleep(1.50)
    if alarmGoes == 2 and problem == 1:
        clearScreen()

    if checkpoint != 5.1:
        break



#CHECKPOINT 5.2 - GUARD ROOM, IN PROGRESS
#TBD AFTER AFT CHECKPOINT
while checkpoint == 5.2:
    pass
    if checkpoint != 5.2:
        break



#CHECKPOINT 5.3 - COMMUNICATIONS ROOM
#TBD AFTER AFT CHECKPOINT
while checkpoint == 5.3:
    pass
    if checkpoint != 5.3:
        break


#CHECKPOINT 6.1 - NEGOTIATIONS W/ THE CAPTAIN, IN PROGRESS
while checkpoint == 6.1:
    if firstSpeak == 2:
        if bridgeActs == 2:
            typingPrint( "\nSimons begins frantically typing before he answers you. 'They can see it, sir. Someone on the bridge is trying to get everything back online.'\n")
            time.sleep(1.50)
        typingPrint( "\nBefore Simons can answer, you hear a voice boom over the ship's intercom: 'Herr Steiner: Ich mochte einen Statusbericht. Warum sind die Motoren ausgeschaltet Was is mit dem Lebenserhaltungssystem passiert?'\n" )
        time.sleep(1.50)
        typingPrint( "\n'I think that would be the captain, sir,' Simons says.\n" )
        time.sleep(1.50)
        pickTalk = input( "\nDo you say something back to the ship's captain, or do you remain silent? Enter 1 for say something, or 2 to stay silent:   ")
        if int(pickTalk) == 2:                                  
            clearScreen()
            typingPrint( "You see an intercom mic next to the terminal. You pick it up and start speaking into it.")
            time.sleep(1.50)
    typingPrint( "\n'Good afternoon, captain.'\n" )
    time.sleep(1.50)
    typingPrint( "\nThe ship stays silent for a few moments. 'To whom am I speaking?' the captain's English is heavily accented, but comprehensible. Certainly better than your German.\n" )
    time.sleep(1.50)
    typingPrint( "\nYou see two ways to handle this conversation: you can give diplomacy a try, or you can try to intimidate him into surrendering the ship.\n" )
    time.sleep(1.50)
    pickDiplomacy = input( "\nDo you pick diplomacy, or intimidation? Enter 1 for diplomacy, or 2 for intimidation:   ")
    if int(pickDiplomacy) == 1:
        clearScreen()
        typingPrint( "\n'My name is Sergeant " + Name1 + " " + Name2 + ", Unified Space Command,' you respond.\n" )
        time.sleep(1.50)
        typingPrint( "\n'Where is Herr Steiner?' the captain asks.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou glance over your shoulder at the engineer. He's still unconscious, with one of your men guarding him. 'Herr Steiner is alive.'\n" )
        time.sleep(1.50)
        typingPrint( "\nThere is a long pause before the captain speaks again. 'What do you want, Sergeant " + Name2 + "?'\n" )
        time.sleep(1.50)
        captSignal = random.randint(1, 2)
        if captSignal == 1:
            clearScreen()
            typingPrint( "'The bridge is attempting to signal another ship,' Simons says quietly. 'KWRS Walkure based on the signature. I'll do my best to block it.'\n" )
            time.sleep(1.50)
            typingPrint( "\nYou feel a pit grow in your stomach. The KWRS Walkure is a massive battleship, the closest thing the Weltraumwaffe has to a ship comparable to the Farragut. If that ship shows up, you're all dead.\n" )
            time.sleep(1.50)
            typingPrint( "\nYou turn to one of the other men. 'Call the drop ship - tell them to radio the Farragut.'\n" )
            time.sleep(1.50)
            typingPrint ( "\nYou hear him call up to the drop ship as you key up the intercom: ")
        typingPrint("'I want you to surrender this ship to me and my men.'\n" )
        time.sleep(1.50)
        typingPrint( "\n'And what happens to my men if I do?' the captain asks.\n" )
        time.sleep(1.50)
        typingPrint( "\n'None of you will be harmed, so long as you cooperate,' you say. 'If you refuse, " )
        if captSignal == 1:
            typingPrint( "and if you continue attempting to call for another ship, ")
        typingPrint("all of the life support systems will stay off.'\n" )
        time.sleep(1.50)
        typingPrint( "\nSilence persists for a few moments as the captain considers what you've said. You can hear your heart beating in your chest as you wait for him to make his decision." )
        captSurrender = random.randint(1, 3)
        checkpoint = 7.1

    else:
        clearScreen()
    if checkpoint != 6.1:
        break



#CHECKPOINT 7.1 - ENGINE ROOM ENDGAME, IN PROGRESS
while checkpoint == 7.1:
    if captSurrender == 1:
        clearScreen()
        typingPrint( "Simons speaks up from next to you. 'Sir: the signal dropped. The Walkure has no idea we're here.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou stand up a little straighter, more confident. 'I'll need an answer, Captain.'\n" )
        time.sleep(1.50)
        typingPrint( "\nA few more seconds of silence. Then, a sigh comes over the radio. 'I have your word my men won't be harmed?'\n" )
        time.sleep(1.50)
        typingPrint( "\n'You do,' you say.\n" )
        time.sleep(1.50)
        typingPrint( "\nA few more seconds of silence. 'Turn the life support back on, and the ship is yours.'\n" )
        time.sleep(1.50)                                                          
        clearScreen()
        typingPrint( "You're ecstatic, but you keep yourself cool and collected. 'A team of my men is on their way to you. Their leader will accept your surrender.'\n" )
        time.sleep(1.50)
        typingPrint( "\nYou hang up the intercom mic. 'Fine work, Sergeant " + Name2 + ",' Simons says from his spot at the terminal.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou change channels on your own radio to the one the drop ship is on and call up: 'Drop ship, this is Sergeant " + Name2 + ". Come in, drop ship. Over.'\n" )
        time.sleep(1.50)
        typingPrint( "\nThere's a few seconds of silence before Kiwi's voice comes in over the radio: 'This is drop ship.'\n" )
        time.sleep(1.50)
        typingPrint( "\n'Tell the Farragut we've captured the ship and we're ready for pickup.'\n" )
        time.sleep(1.50)
        checkpoint = 0

    elif captSurrender == 2:
        clearScreen()
        typingPrint( "Simons speaks up from next to you. 'Sir: the signal dropped. The Walkure has no idea we're here.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou stand up a little straighter, more confident. 'I'll need an answer, Captain.'\n" )
        time.sleep(1.50)
        typingPrint( "\nThere's a few more seconds of silence before the captain speaks: 'I have my orders, sergeant, just as you do. That includes not surrendering my ship or my men. I'm sure you understand.'\n" )
        time.sleep(1.50)
        typingPrint( "\nYou nod. You'd expected as much: the Nazis at large weren't known for being open to surrender. Especially not the Weltraumwaffen.\n" )
        time.sleep(1.50)
        typingPrint( "\n'We'll be in touch.' You hang up the intercom mic.\n" )
        time.sleep(1.50)
        clearScreen()

    else:
        clearScreen()
        typingPrint( "Suddenly, Simons stops typing. His face grows pale.\n" )
        time.sleep(1.50)
        typingPrint( "\n'What's wrong?' You ask.\n" )
        time.sleep(1.50)
        typingPrint( "\n'...The signal got through. I-I don't know how, but... I'm sorry.'\n" )
        time.sleep(1.50)
        typingPrint( "\nYou try to not look as scared as you feel.\n" )
        time.sleep(1.50)
        typingPrint( "\nBefore you can say anything to your men, you hear the captain's voice over the intercom: 'I have my orders, sergeant, just as you do. That includes not surrendering my ship or my men. The Walkure will arrive in about thirty minutes - I suggest you and your men get off my ship before it arrives.'\n" )
        time.sleep(1.50)
        clearScreen()
        typingPrint( "The engine room falls silent. Your men are looking up at you, waiting.\n" )
        time.sleep(1.50)
        typingPrint( "\n'What are your orders?' Simons asks.\n" )
        time.sleep(1.50)
        pickRetreat = input( "\nDo you cut your losses and leave the ship, or do you stay and find a way to fight? Enter 1 for leave, or 2 to fight:   " )
        if int(pickRetreat) == 1:
            clearScreen()
            plzRedo = youSuck()
            if plzRedo == 1:
                reloadLast()
            else:
                sys.exit()

        else:
            clearScreen()
    if int(pickSplit) == 1:
        typingPrint( "You key up your radio, next: 'Team two leader, come in.'\n" )
        time.sleep(1.50)
        typingPrint( "\n'Go for team two leader.'\n" )
        time.sleep(1.50)
        typingPrint( "\n'I just heard from the ship's captain,' you say. 'They aren't surrendering. Be prepared for stiff resistance.'\n" )
        time.sleep(1.50)
        typingPrint( "\n'Aye, sir,' the team leader says.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou sign off from the radio.\n")
        time.sleep(1.50)
    typingPrint( "\n'What are your orders, sir?' Simons asks.\n" )
    time.sleep(1.50)
    typingPrint( "\nYou consider it for a moment. Staying in the engine room seems like the best course of action - you can respond quickly to changes from there. Still: you know that you can't take the bridge from there. You can think of a few options. You know that Kiwi has some limited weapons on board the drop ship - nothing big, but it could potentially be detrimental to the Saalwachter and everyone on board, including your men. You also know you have control of many more systems on the ship. You could ask Simons to take more of them down, but if he isn't focused on blocking potential signals, the bridge might be able to get a distress signal out to the Walkure.\n")
    time.sleep(1.50)
    pickKiwi = input( "\nDo you ask Kiwi for air support? Do you see what other systems you can take down to help the other team? Or do you do both? Enter 1 for air support, 2 to check for other systems, or 3 for both:     " )
    if int(pickKiwi) == 1:
        clearScreen()
        typingPrint( "Taking out more systems would be beneficial, but not if the other ship is able to call the Walkure to them. The Farragut is close, but not only is the Walkure closer, it's a faster ship. Keeping that ship away is your team's best bet of not just success, but survival. Pulling Simons' focus away from keeping them from signalling other ships doesn't seem like the best course of action.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou call up to the drop ship on your radio: 'Drop ship, this is Sergeant " + Name2 + ", come in, drop ship.'\n" )
        time.sleep(1.50)
    elif int(pickKiwi) == 2:
        clearScreen()
        typingPrint( "'Is it just the electrical that you have access to?' you ask Simons.\n" )
        time.sleep(1.50)
        typingPrint( "\n'That's the big one,' Simons says. 'I've also got access to communications.'\n" )
        time.sleep(1.50)
        typingPrint( "\nYou consider it. Both have their advantages and disadvantages. Electrical could cut their controls, but it could also cut your own. Cutting communications would keep them from signalling the Walkure, but it might also cut your ability to communicate with the bridge.\n" )
        time.sleep(1.50)
        pickElectric = input( "\nDo you ask Simons to cut the electrical, the communications, or both? Enter 1 for electrical, 2 for communications, or 3 for both:   " )
        if int(pickElectric) == 1:
            clearScreen()
            typingPrint( "'Let's focus on the electrical,' you say. 'Cut power everywhere but here.'\n" )
            time.sleep(1.50)
            typingPrint( "\nSimons continues typing. 'I can do that.'\n" )
            time.sleep(1.50)
            if int(pickSplit) == 1:
                typingPrint( "\nYou key up your radio: 'Barlowe, this is Sergeant " + Name2 + ", come in, Barlowe.'\n" )
                time.sleep(1.50)
                typingPrint( "\n'This is Barlowe.'\n" )
                time.sleep(1.50)
                typingPrint( "\n'The whole ship's about to go dark,' you say. 'Be ready for it.'\n" )
                time.sleep(1.50)
                typingPrint( "\n'Aye, sir.'\n" )
                time.sleep(1.50)
                clearScreen()
            typingPrint( "The whine of the generators slowly quiets down.\n" )
            time.sleep(1.50)
            typingPrint( "\n'Lights are out everywhere,' Simons says.\n" )
            if int(pickSplit) == 1:
                typingPrint( "\nYou nod, then key up your radio: 'Barlowe, this is Sergeant " + Name2 + ".\n" )
                time.sleep(1.50)
                typingPrint( "\n'This is Barlowe.'\n" )
                time.sleep(1.50)
                typingPrint( "\n'How close to the bridge are you?' you ask.\n" )
                time.sleep(1.50)
                typingPrint( "\n'Not far, I don't think,' Barlowe says. 'In fact... I think that's the door in front of us.'\n" )
                clearScreen()

                typingPrint( "You take a deep breath before you speak into the radio next. 'Take the bridge. Be smart about it.'\n" )
                time.sleep(1.50)
                typingPrint( "\n'Aye sir,' you hear Barlowe say. 'Going in now.\n'" )
                time.sleep(1.50)
                typingPrint( "\nThe radio goes silent. You hang up the intercom mic and you wait.\n" )
                time.sleep(1.50)
                                                                                                    
                clearScreen()
                time.sleep(1.50)
                typingPrint( "You don't know how long it takes for Barlowe to speak, again. It feels like hours before you hear anyone, but you know it was likely only minutes. You can cut the tension in the room with a knife." )
                time.sleep(1.50)
                typingPrint( "\n'Sergeant " + Name2 + ", can you hear me?' Barlowe's voice comes over the ship's intercom system rather than over the radio.\n" )
                time.sleep(1.50)
                typingPrint( "\nYou pick up the intercom mic, again. 'I can hear you. I take it you took the bridge?'\n" )
                time.sleep(1.50)
                typingPrint( "\n'We did,' Barlowe says.\n" )
                time.sleep(1.50)
                typingPrint( "\nThat news should make you happy. However, there's one more thing you need to ask before you can celebrate.\n" )
                time.sleep(1.50)
                typingPrint( "\n'Did you take any casualties?' You're almost afraid to ask." )
                time.sleep(1.50)
                bridgeCas = random.randint(1, 5)
                if bridgeCas <= 3:
                    clearScreen()
                    typingPrint( "'Everyone on team two is up,' Barlowe says. 'I think we're all looking a little worse for wear, though.'\n" )
                    time.sleep(1.50)
                    typingPrint( "\nNow, you're able to breathe. Some.\n" )
                    time.sleep(1.50)
                    typingPrint( "\n'Great work, Barlowe,' you say.\n" )
                    time.sleep(1.50)
                    typingPrint( "\nYou key up your radio, next: 'Drop ship: this is Sergeant " + Name2 + "; come in, drop ship.'\n" )
                    time.sleep(1.50)
                    typingPrint( "\n'This is drop ship,' Kiwi says.\n" )
                    time.sleep(1.50)
                    typingPrint( "\n'The Saalwachter is ours,' you say. 'Call the Farragut for a pickup.'\n" )
                    saalwachterEnd = 2
                    checkpoint = 0

                else:
                    clearScreen()
                    typingPrint( "\n'Not yet,' Barlowe says. 'If we don't get medical soon, though, we will.'\n" )
                    time.sleep(1.50)
                    typingPrint( "\nYou feel sick to your stomach.\n" )
                    time.sleep(1.50)
                    typingPrint( "\n'Do what you can, and hang in there,' you say. 'Help is on the way.'\n" )
                    time.sleep(1.50)
                    typingPrint( "\nYou key up your radio, next: 'Drop ship: this is Sergeant " + Name2 + "; come in, drop ship.'\n" )
                    time.sleep(1.50)
                    typingPrint( "\n'This is drop ship,' Kiwi says.\n" )
                    time.sleep(1.50)
                    typingPrint( "\nCall the Farragut, and tell them to get the medbay ready,' you say. 'The ship is ours.'\n" )
                    saalwachterEnd = 3
                    checkpoint = 0
        
    else:
        clearScreen()
        typingPrint( "Both options are excellent - combining the two seems like the best course of action.\n" )
        time.sleep(1.50)
        typingPrint( "\n'Simons: break everything you can get access to that won't kill us all,' you say. 'Make sure we can still call the bridge.'\n" )
        time.sleep(1.50)
        typingPrint( "\n'Aye, sir,' he says as he continues typing.\n" )
        time.sleep(1.50)
        typingPrint( "\nNext, you call up Kiwi on your radio: 'Drop ship, this is Sergeant " + Name2 + ", come in, drop ship.'\n" )
        time.sleep(1.50)
    typingPrint( "\nThere are a few seconds of silence before you hear Kiwi's voice: 'Sergeant " + Name2 + ", this is drop ship. Go ahead.\n" )
    time.sleep(1.50)
    typingPrint( "\n'The Saalwachter's captain isn't surrendering,' you say.\n" )
    time.sleep(1.50)
    typingPrint( "\n'Were you expecting him to? What can I do to help?'\n" )
    time.sleep(1.50)
    pickBroadside = input( "\nDo you ask him to fire a broadside at the Saalwachter? Do you ask him to call the Farragut for backup? Or do you do both? Enter 1 for broadside, 3 to call the Farragut, or 3 for both:   " )
    if int(pickBroadside) == 1:
        clearScreen()
        typingPrint( "'How would you feel about putting the fear of God in them?' You ask. 'I think that might help negotiations.'\n" )
        time.sleep(1.50)
        typingPrint( "\n'Will do,' Kiwi says. 'Firing now.'\n" )
        time.sleep(1.50)
        typingPrint( "\nThe radio cuts.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou wait a few seconds to see if the captain calls back, himself.\n" )
    elif int(pickBroadside) == 2:
        clearScreen()
        typingPrint( "'How far away from the Farragut are we?' you ask.\n" )
        time.sleep(1.50)
        typingPrint( "\nThere's a few seconds of silence. '...If they were to start heading here right now, they'd be here in about an hour. Why?'\n" )
        time.sleep(1.50)
        typingPrint( "\n'Would you be able to get them closer?'\n" )
        time.sleep(1.50)
        typingPrint( "\n'Absolutely.'\n" )
        time.sleep(1.50)
        typingPrint( "\n'Let me know what they say.' You key off the radio.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou consider your options. You want to end things quickly with the bridge. You might be able to convince him to surrender if you're able to convince him that a much bigger ship is on the way. However, that might also backfire if he doesn't believe you, or gains a sense of urgency about signalling the Walkure.\n" )
        time.sleep(1.50)
        pickBluff = input( "\nDo you bluff about how close the Farragut is? Enter 1 for yes, or 2 for no:   ")
        if int(pickBluff) == 1:
            clearScreen()
            typingPrint( "You hear Barlowe's voice over the intercom: 'Sergeant " + Name2 + ", this is Barlowe. We're in position at the Bridge.'\n" )
            time.sleep(1.50)
            typingPrint( "\n'Hold,' you say into your radio. 'Wait for my signal.'\n" )
            time.sleep(1.50)
            typingPrint( "\n'You speak into the intercom system next: 'You have about ten minutes to make a decision. There's a battleship on the way as we speak. I'd suggest making things as easy as possible for them.'\n" )
            time.sleep(1.50)
            typingPrint( "\n'Which ship?' the captain asks.\n" )
            time.sleep(1.50)
            typingPrint( "\n'The Farragut.'\n" )

            clearScreen()
            typingPrint( "The captain is silent for a few moments, apparently weighing his options. You have a guess as to what he's thinking about. The Farragut is a notorious ship. The flagship of Unified Space Command, and the bane of the Weltraumwaffen. A smart man would surrender the ship. But, you know all too well that the Weltraumwaffen officers have a tendency to do the brave thing rather than the smart thing. You can only hope that this one will choose the latter.\n" )
            time.sleep(1.50)
    else:
        clearScreen()
        typingPrint( "It's time to pull off the kid gloves - doing both seems like your best bet.\n" )
        time.sleep(1.50)
        typingPrint( "'How far away from the Farragut are we?' you ask.\n" )
        time.sleep(1.50)
        typingPrint( "\nThere's a few seconds of silence. '...If they were to start heading here right now, they'd be here in about an hour. Why?'\n" )
        time.sleep(1.50)
        typingPrint( "\n'Would you be able to get them closer?'\n" )
        time.sleep(1.50)
        typingPrint( "\n'Absolutely.'\n" )
        time.sleep(1.50)
        typingPrint( "\n'Do it,' you said. 'Fire a warning shot across their bow, while you're at it.'\n" )
        time.sleep(1.50)
        typingPrint( "\n'Sounds good.'\n" )
        time.sleep(1.50)
        typingPrint( "\nThe radio cuts.")
        time.sleep(1.50)
        typingPrint( "You wait for a few seconds for one of them to call you back.\n" )
        time.sleep(1.50)
        clearScreen()
    captCalls = random.randint(1, 2)
    if pickBluff == 1:
        clearScreen()
    elif captCalls == 1:
        typingPrint( "Sure enough, you hear the captain's voice over the intercom, again: 'I have you to thank for that, don't I?'\n" )
        time.sleep(1.50)
        typingPrint( "\nYou pick up the intercom mic, again. 'That was from our drop ship. The nearest Nazi battleship is close, but that ship's closer. I can't guarantee he'll keep missing the bridge at this rate.'\n" )
        time.sleep(1.50)
        typingPrint( "\n'You expect me to believe you'll continue shooting at this ship?' the captain asks.\n" )
        time.sleep(1.50)
        typingPrint( "\nIn truth: continuing to shoot at the bridge would put the team currently going there in danger. More danger than you're willing to risk.\n" )
        time.sleep(1.50)
        typingPrint( "\n'Do you want to risk that?' You ask.\n" )
        time.sleep(1.50)
    else:
        clearScreen()
        typingPrint( "The captain, however, doesn't speak over the intercom.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou pick up the intercom mic: 'Bridge, this is Sergeant " + Name2 + ". I don't suppose you saw that light show, did you?'\n" )
        time.sleep(1.50)
        typingPrint( "\n'I did,' the captain says.\n" )
        time.sleep(1.50)
        typingPrint( "\n'The next one goes directly into your porthole,' you say. 'Surrender the ship, or I'll order him to fire.'\n" )
        time.sleep(1.50)
    captSurrender = random.randint(1, 2)
    if captSurrender == 1:
        clearScreen()
        typingPrint( "A sigh comes over the radio. 'I have your word my men won't be harmed?'\n" )
        time.sleep(1.50)
        typingPrint( "\n'You do,' you say.\n" )
        time.sleep(1.50)
        typingPrint( "\nA few more seconds of silence. 'The ship is yours.'\n" )
        time.sleep(1.50)
                                                                                        
        clearScreen()
        typingPrint( "You're ecstatic, but you keep yourself cool and collected. 'A team of my men is on their way to you. Their leader will accept your surrender.'\n" )
        time.sleep(1.50)
        typingPrint( "\nYou hang up the intercom mic. 'Fine work, Sergeant " + Name2 + ",' Simons says from his spot at the terminal.\n" )
        time.sleep(1.50)
        typingPrint( "\nYou change channels on your own radio to the one the drop ship is on and call up: 'Drop ship, this is Sergeant " + Name2 + ". Come in, drop ship. Over.'\n" )
        time.sleep(1.50)
        typingPrint( "\nThere's a few seconds of silence before Kiwi's voice comes in over the radio: 'This is drop ship. How'd they like the light show?'\n" )
        time.sleep(1.50)
        typingPrint( "\n'More than I expected,' you say. 'Tell the Farragut we've captured the ship and we're ready for pickup.'\n" )
        time.sleep(1.50)
        saalwachterEnd = 1
        checkpoint = 0

    else:
        clearScreen()
        if pickBroadside == 1 or pickBroadside == 3:
            typingPrint( "'I think you're bluffing,' the captain says. 'You have men on this ship, too. I doubt you'd so readily sacrifice their lives for this ship.'\n" )
            time.sleep(1.50)
        if pickBluff == 2:
            typingPrint( "\n'My men are ready to die for their country. Are yours?' he finally asks.\n" )
            time.sleep(1.50)
        typingPrint( "\nYou wince. It seems your skills at bluffing aren't quite good enough to trick this captain.\n" )
        time.sleep(1.50)
        if int(pickSplit) == 1:
            typingPrint( "\nYou hear Barlowe's voice over your radio: 'Sergeant " + Name2 + ", this is Barlowe. I think we're about at the bridge.\n" )
            time.sleep(1.50)
            typingPrint( "\nYou swear quietly to yourself. You don't know that this captain will surrender his ship without a good showing. However, you also don't know how many Weltraumwaffen marines are on that bridge - as far as you know, you'll be sending those men to their end if you send them in.\n" )
            time.sleep(1.50)
            pickNegotiate = input( "\nDo you try one more time to get him to see reason, or do you send Barlowe's team into the bridge? Enter 1 to negotiate, or 2 to send in Barlowe's team:   ")
            if int(pickNegotiate) == 1:
                clearScreen()
                typingPrint( "'Hold outside the bridge,' you say quietly into your radio. 'Wait for my signal.'\n" )
                time.sleep(1.50)
                typingPrint( "\n'Roger.'\n" )
                time.sleep(1.50)
                typingPrint( "\n'Let's cut to the chase, captain,' you say into the intercom. 'You have your price. What is it?'\n" )
                time.sleep(1.50)
                typingPrint( "\n'My price?' The captain seems confused.\n" )
                time.sleep(1.50)
                typingPrint( "\n'What will it take to get you to surrender this ship?' you ask. 'I'd be happy to send in my marines to take the bridge by force, or shoot a hole into your porthull. I'd just as soon get this resolved without bloodshed, though.'\n" )
                time.sleep(1.50)
                typingPrint( "\nMore silence. 'My men are ready to die for their country. Are yours?'\n" )
                time.sleep(1.50)
                typingPrint( "\nYou were worried he would say that. Now, you have a difficult decision to make.\n" )
                time.sleep(1.50)
                pickKiwiShoot = input( "\nDo you ask Kiwi to shoot into the bridge, or do you send Barlowe's team in? Enter 1 for shoot into the bridge, or 2 to send Barlowe's team in:   " )
                if int(pickKiwiShoot) == 2:
                    clearScreen()
                    typingPrint( "You take a deep breath before you speak into the radio next. 'Take the bridge. Be smart about it.'\n" )
                    time.sleep(1.50)
                    typingPrint( "\n'Aye sir,' you hear Barlowe say. 'Going in now.\n'" )
                    time.sleep(1.50)
                    typingPrint( "\nThe radio goes silent. You hang up the intercom mic and you wait.\n" )
                    time.sleep(1.50)

                    clearScreen()
                    time.sleep(1.50)
                    typingPrint( "You don't know how long it takes for Barlowe to speak, again. It feels like hours before you hear anyone, but you know it was likely only minutes. You can cut the tension in the room with a knife." )
                    time.sleep(1.50)
                    typingPrint( "\n'Sergeant " + Name2 + ", can you hear me?' Barlowe's voice comes over the ship's intercom system rather than over the radio.\n" )
                    time.sleep(1.50)
                    typingPrint( "\nYou pick up the intercom mic, again. 'I can hear you. I take it you took the bridge?'\n" )
                    time.sleep(1.50)
                    typingPrint( "\n'We did,' Barlowe says.\n" )
                    time.sleep(1.50)
                    typingPrint( "\nThat news should make you happy. However, there's one more thing you need to ask before you can celebrate.\n" )
                    time.sleep(1.50)
                    typingPrint( "\n'Did you take any casualties?' You're almost afraid to ask." )
                    time.sleep(1.50)
                    clearScreen()
                    bridgeCas = random.randint(1, 5)
                    if bridgeCas <= 3:
                        typingPrint( "'Everyone on team two is up,' Barlowe says. 'I think we're all looking a little worse for wear, though.'\n" )
                        time.sleep(1.50)
                        typingPrint( "\nNow, you're able to breathe. Some.\n" )
                        time.sleep(1.50)
                        typingPrint( "\n'Great work, Barlowe,' you say.\n" )
                        time.sleep(1.50)
                        typingPrint( "\nYou key up your radio, next: 'Drop ship: this is Sergeant " + Name2 + "; come in, drop ship.'\n" )
                        time.sleep(1.50)
                        typingPrint( "\n'This is drop ship,' Kiwi says.\n" )
                        time.sleep(1.50)
                        typingPrint( "\n'The Saalwachter is ours,' you say. 'Call the Farragut for a pickup.'\n" )
                        saalwachterEnd = 2
                        checkpoint = 0

                    else:
                        typingPrint( "\n'Not yet,' Barlowe says. 'If we don't get medical soon, though, we will.'\n" )
                        time.sleep(1.50)
                        typingPrint( "\nYou feel sick to your stomach.\n" )
                        time.sleep(1.50)
                        typingPrint( "\n'Do what you can, and hang in there,' you say. 'Help is on the way.'\n" )
                        time.sleep(1.50)
                        typingPrint( "\nYou key up your radio, next: 'Drop ship: this is Sergeant " + Name2 + "; come in, drop ship.'\n" )
                        time.sleep(1.50)
                        typingPrint( "\n'This is drop ship,' Kiwi says.\n" )
                        time.sleep(1.50)
                        typingPrint( "\nCall the Farragut, and tell them to get the medbay ready,' you say. 'The ship is ours.'\n" )
                        saalwachterEnd = 3
                        checkpoint = 0

    clearScreen()
    typingPrint( "You need to take the ship. You don't see the captain surrendering without putting up a fight, possibly killing your men in the process.\n" )
    time.sleep(1.50)
    typingPrint( "\nIt's a risk, but you only see one more option left to you.\n" )
    time.sleep(1.50)
    typingPrint( "\n'Are there blast doors leading to the bridge?' you ask Simons.\n" )
    time.sleep(1.50)
    typingPrint( "\'There are,' Simons confirms. 'What do you have in mind?'\n" )
    time.sleep(1.50)
    typingPrint( "\nYou nod. 'Seal them, and make sure they can't open them.'\n" )
    time.sleep(1.50)
    typingPrint( "\nSimons hesitates, but he starts typing, anyway. It seems he knows what you're about to do.\n" )
    time.sleep(1.50)
    clearScreen()

    typingPrint( "Next, you call up Kiwi over the radio: 'Drop ship, this is Sergeant " + Name2 + "; come in, drop ship.\n" )
    time.sleep(1.50)
    typingPrint( "\n'This is drop ship,' Kiwi says.\n" )
    time.sleep(1.50)
    typingPrint( "\nYou hesitate before you give the order. 'Shoot into the porthull.'\n" )
    time.sleep(1.50)
    typingPrint( "\nThere's silence as Kiwi considers the order. For a moment, you think he might fight you on it. In fact, you kind of hope he does. Instead, you hear him say: 'Roger. Firing now.'\n" )
    time.sleep(1.50)
    typingPrint( "\nThere's a few second's pause before anything happens. A few seconds for you to wonder if this is the right decision.\n" )
    time.sleep(1.50)

    clearScreen()
    typingPrint( "The entire ship shutters underneath your feet, nearly throwing you and the rest of your team to the ground. You see warning lights flashing around you.\n" )
    time.sleep(1.50)
    typingPrint( "\n'What's the status on the bridge?' you ask Simons.\n" )
    time.sleep(1.50)
    typingPrint( "\nSimons doesn't respond for a few seconds. He's typing furiously, seemingly looking through a damage report.\n" )
    time.sleep(1.50)
    typingPrint( "\n'The bridge's airlock failed,' Simons says. 'Everything else seems to be fine.'\n" )
    time.sleep(1.50)
                                                                                                    
    clearScreen()
    typingPrint( "You nod. You don't know what to say, or if there's even words. You know you need to process this, but you also know that will need to wait: you have a mission to complete, after all.\n" )
    time.sleep(1.50)
    typingPrint( "\nYou call up on your radio: 'Drop ship, this is Sergeant " + Name2 + ".'\n" )
    time.sleep(1.50)
    typingPrint( "\n'This is drop ship,' Kiwi says.\n" )
    time.sleep(1.50)
    typingPrint( "\n'Call the Farragut,' you say. 'The Saalwachter is ours.'")
    saalwachterEnd = 4
    checkpoint = 0

    
    if checkpoint != 7.1:
        break



if checkpoint == 0:
    clearScreen()
    typingPrint(missionSuccess)
    time.sleep(1.50)
    sys.exit()