# This is a choose your own adventure program
# Author: Ray Bolin
# Date: 1/2/2022
# 100DaysOfCoding

print('''
You wake up in a very small tavern, but you have no idea how you got there. 
The last thing you remember is that you were deep in the woods searching for a huge hog to kill so you can feed your family.
You're at the bar against the wall with your upper body mostly on top of the counter and you feel groggy.    
As you look around the room you can see the sun rising through a small barred up window.
The tavern appears to not have been cleaned in quite some time and it has a four odor.
 You notice a door to the left where you can exit just as the barkeep comes out from the back. 
 ''')

leaveOrTalk = ""
while (leaveOrTalk.lower() != "door") and (leaveOrTalk.lower() != "barkeep"):
    leaveOrTalk = input('Type "door" to leave the tavern or "barkeep" to speak to the barkeep:  ')

if leaveOrTalk.lower() == "door":
    print('''
        You stumble over to the door and find that it is locked. 
        You notice something odd as it is actually locked from the outside rather than the inside.
        Your head is so fuzzy you think this must not be the exit.
        You decide to go speak to the barkeep.
    ''')

print('''
You ask the barkeep how you got here. 
He says "Ya don't remember anything do ya? Ya better remember that you owe me three gold! Settle up right now!"
''')

payOrRefuse = ""
while (payOrRefuse.lower() != "pay") and (payOrRefuse.lower() != "refuse"):
    payOrRefuse  = input('Type "pay" to pay the barkeep or "refuse" to refuse to pay:  ')

if payOrRefuse.lower() == "pay":
    print('''
        You tell the barkeep to calm down and that you will pay. 
        You search your pockets and realize that you have been robbed. 
        All of your possessions are gone. 
        Your fearfully look up at the barkeep as he realizes that you have no money.     
    ''')
else:
    print('''
        You try your best to remember what happened the night before, but everything is a blur. 
        You don't understand why you feel so groggy and can't think straight.
        You tell the barkeep that you refuse to pay because you cannot remember anything.        
    ''')

print('''
You try to explain that you believe that you were drugged.
The barkeep angrily pulls a knife and gives you two options. 
    
Option 1: The barkeep will agree to wipe your bill if you manage to kill a huge hog that has been scaring away patrons.
Option 2: The barkeep will kill you himself. 
''')

questOption = ""
while (questOption.lower() != "hog") and (questOption.lower() != "barkeep"):
    questOption = input('Type "hog" to go kill the hog or "barkeep" if you want to test the barkeeps patience:  ')

if questOption.lower() == "hog":
    print('''
        The barkeep takes you to the back and lets you outside of the tavern.
        You still feel inebriated as he hands you a sword. 
        Upon inspection of the sword you see that it has wet blood on it.
        The barkeep yells "Ya got twenty minutes to find and kill that hog!"
        You watch him load six bullets into a revolver as he looks at you and says "One of these has your name on it"
         
        You begin to stumble slowly away from the tavern trying to hold yourself up tree by tree. 
        You know that you are in no condition to be fighting hogs of any size, but you want to try to get as far away as you can.
        You see a path that might lead to a main road and you begin walking in that direction as fast as possible. 
        You fall into a deep trap that was covered with leaves and you land on many sharp spikes. 
        You have fallen to your death. 
          
        GAME OVER
    ''')
else:
    print('''
        The barkeep says "I don't have time for your games!"
        He smacks you around a bit and gets you pinned into a corner.
        The barkeep says "Perhaps you've heard of The Woodsmen killer?"
        The barkeep begins to laugh hysterically as he explains to you that he is a serial killer that has drugged and robbed you.
        The barkeep pulls out a huge knife and pierces your heart. 
        
        GAME OVER
    ''')
