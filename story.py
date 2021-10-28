import sys,time,random
import turtle as tr

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.045)
    return ""

def death():
    tr.clear()
    tr.color('red')
    tr.write('You died', font = ['Arial', 16, 'normal'])

wn = tr.Screen()
wn.addshape('EnglishProjectInn.gif')
tr.shape('EnglishProjectInn.gif')
wn.mainloop()

print_slow("A Belle Dame Trope.")
print_slow(" \nThis story follows a version of you, in the 1930s, looking for a job. You need money to pay rent, and are willing \
to work any job.") 

q1 = input(print_slow("\nWalking down a wet street, you stumble upon a nice and clean looing inn that says, Looking for worker to clean tables. \
You decide to: \n1) Walk into the inn and take the job or \n2) Walk away. "))
if q1 == '2':
    print_slow(" \n You turn around and head to your house. ONE MONTH LATER. You are kicked out of your apartment and dragged \
    to a debtors prison. You really should have taken the job.")
    sys.exit()
elif q1 == '1':
    print_slow("Walking inside, you see that the place is in high use and the floor is getting dirty. Clearly it needed \
a cleaner. Perhaps you could negotiate a good income...")
else:
    print_slow("Enter Valid Answer")
    sys.exit()

print_slow("\n")

print_slow(" \n A smiling lady, with the name badge Dorthy, greets you. She asks to what main course you would like, \
    \n and if you wanted a window table. Not wanting to buy anything, you ask if the cleaning job had been taken.")
q2 = input(print_slow("Already taken? We just put the poster up this morning. Our old cleaner left with no explanation. \
\nDon't worry about that, though. Well, if your here for the job, we start payment at 40 pence an hour ($30 an hour in today's\
money. Is that enough? y/n "))

if q2 == 'y':
    print("")
    print_slow("Well, let me take you to the supplies. Walking through a door in the back of the inn, she brings you \
    a small closet with a mop and bucket. Well, I would recommend starting with the kitchen and then going to the tables.")
elif q2 == 'n':
    print("")
    print_slow("Well, at most, I can offer you a sign-on bonus of 1 shilling. Is that enough? Quickly accepting, you \
    grab a mop/bucket and start cleaning. \n")
else:
    q2 = input("ENTER VALID ANSWER.")
    sys.exit()

q3 = input(print_slow("A Few Hours Later. At night, the inn is quite crowded. You have your hands full cleaning up. Eventually, \
you finish up. Heading back inside, you can find Dorthy. She hands you your payment and you head to the enterance. You can \
\n 1) order food right now at the inn \n 2) Head home and cook some food"))

if q3 == '1':
    print_slow("You walk to the cashier and ask what is on the menu. The cashier responds, We have some pasta for vegetarians and\
    grilled lamb with red wine sauce for others. Dessert is the chefs special, a souffle. You decide to take your money and \
    buy all of them. Enjoying your lavish meal, you head home to sleep.")
elif q3 == "2":
    print_slow("You head to the grocery store and buy some pasta and veggies. You go home, cook some veggie pasta, \
    and go go to sleep.")
else:
    print_slow("Enter Valid Answer")
    sys.exit()

print_slow("") 

q4 = input(print_slow("\nTommorow\nYou walk to the inn and start cleaning. Finishing up pretty quickly, you decide to explore \
around. After all, no one is here untill noon. You can \n1) check out the kitchen \n2) The tables \n3) or some of the accomadation rooms \
on the second story."))

