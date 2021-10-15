import sys,time,random
import turtle as t

t.write("Hi")

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.045)
    return ""

print_slow("A Belle Dame Trope.")
print_slow(" \n This story follows a version of you, in the 1930s, looking for a job. You need money to pay rent, and are willing \
to work any job.") 

q1 = input(print_slow("\nWalking down a wet street, you stumble upon a ok-looing inn that says, Looking for worker to clean tables. \
You decide to: \n 1) Walk into the inn and take the job or \n2) Walk away. "))
if q1 == '2':
    print_slow(" \n You turn around and head to your house. ONE MONTH LATER. You are kicked out of your apartment and dragged \
    to a debtors prison. You really should have taken the job.")
else:
    print_slow("Enter Valid Answer")
    sys.exit()

print_slow("")

print_slow("Walking inside, you see that the walls are damaged and inn has not been cleaned.")
q2 = input(print_slow(" \n A seemingly nice lady says, Welcome to the job! I'm Dorthy. The mop and soap are in the corner. Confused about how she knew you were \
here for the job, you \n 1) Ignore your confusion and ask how high your pay is or \n 2) Ask how she knew what you came to the inn for."))

if q2 == '1':
    print("")
    q3 = input(print_slow("Responding, Dorthy says, I will pay you a shilling an hour ($70 an hour in today's money). Is that enough payment?\
    y/n"))
elif q2 == '2':
    print("")
    q3 = input(print_slow("I just had a feeling you were here for that. Anyway, payment will be 1 shilling($70 in today's money) an hour.\
    Is that enough? y/n"))
else:
    q2 = input("ENTER VALID ANSWER.")
    sys.exit()

print_slow("")

if q3 == 'y':
    print_slow("You graciously accept the payment. Walking to the corner, you start mopping the floor.")
elif q3 == "n":
    print_slow("You ask if you can have more , and Dorthy responds, I can add some bonuses like me paying for insurance, if that\
    is ok? Knowing that you hit the jackpot, you immediatly start working.")
else:
    print_slow("Enter Valid Answer")
    sys.exit()

print_slow("") 

q4 = input(print_slow("Later that day, you are walking to your home. You finally have money to pay the rent. Deciding to celebrate. You can\
\n 1) Take a good long rest, \n 2) Go out for a fancy dinner, or \n 3) Buy some tickets for the cricket game, with your favorite team\
playing."))

if q4 == '1':
    print_slow("Heading home, you invite some friends over. After some fun small talk, your friends leave and you sleep soundly")
elif q4 == '2':
    print_slow("Going out to a steak-house, you enjoy a fillet steak and wine. After stuffing yourself, you head home for a good \
    nights rest.")
elif q4 == '3':
    print_slow("Heading to the cricket game, you grab a burger and cheer as hard as you can. Your team wins, and you happily head home\
    . You then have a good nights rest.")
else:
    print_slow("Enter Valid Answer")
    sys.exit()

q5 = input(print_slow(" \n After a good nights rest, you get up and head to the inn. Your in a good mood and enter the inn.\
Upon etntering, you realize that Dorthy is not their. You can \n 1) Explore the area \n 2) Grab some paint and clean the walls\
\n 3) Leave"))

if q5 == '1':
    print_slow("Looking around, you see a section of the wall that seems to be broken. Pressing on it, the wall opens up and \
    reveals a secret room. Heading inside, you see another door. But before you go in, you hear a voice saying, \n \
    We got a nice young target to sell. They think their getting a great deal, but wait till we sell them into slavery! \
    They will fetch a nice price of 10 shillings or so ($700). Realizing what this means you run.")
elif q5 == '2':
    print_slow("As you start painting, you see a section of the wall that seems to be broken. Pressing on it, the wall opens up and \
    reveals a secret room. Heading inside, you see another door. But before you go in, you hear a voice saying, \n \
    We got a nice young target to sell. They think their getting a great deal, but wait till we sell them into slavery! \
    They will fetch a nice price of 10 shillings or so ($700). Realizing what this means you run. ")
else:
    print("Enter Valid Answer")
    sys.exit()

q6 = input(print_slow("Entering the main room of the inn, the secret door locks behind you. They heard you. You run towards the \
main door, but it is locked as well. \n Suddenly you notice a yellow gas on the floor. After wadding the air, you take a sniff of \
the gas. You instantly feel sleepy. Sleeping gas. You have to escape. You can \n 1) Try to find the source of the sleeping gas\
 and block it \n 2) Find a way to secape from the room \n 3) Accept your fate "))

if q6 == '1':
    q7 = input(print_slow("Looking aroudn you, you have 3 options. You can look \n 1) around the floor \n 2) Check the walls \n 3) Check\
     the roof. "))
elif q6 == '2':
    q7 = input(print_slow("Thinking for a second, you come up with 3 logical escape plans \n 1) Out through the secret room. \n 2) "))
elif q6 == '3':
    print_slow("Accepting your fate, you take a deep breath of the sleeping gas and fall to the ground. A day later, you think, \
    you wake up in a cage. The ground shakes, and the floor has puddles of water. You have got to escape, but that is a story for \
    another day.")
else:
    print("Enter Valid Awnswer")
    sys.exit()