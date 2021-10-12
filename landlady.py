print("A Belle Dame Trope")
print("This story follows a version of you, in the 1930s, looking for a job. You need money to pay rent, and are willing \
to work any job.") 

q1 = input("Walking down a wet street, you stumble upon a ok-looing inn that says, Looking for worker to clean tables. \
You decide to 1) Walk into the inn and take the job or 2) Walk away. ")
if q1 == '2':
    print("As you walk away, you realize that you need the money. Turning around, you head into the inn.")

print("Walking inside, you see that the walls are damaged and inn has not been cleaned.")
q2 = input("She says, Welcome to the job! I'm Dorthy. The mop and soap are in the corner. Confused about how she knew you were \
here for the job, you 1) Ignore your confusion and ask how high your pay is or 2) Ask how she knew what you came to the inn for.")

if q2 == '1':
    q3 = input("Responding, Dorthy says, I will pay you a shilling an hour ($70 an hour in today's money). Is that enough payment?\
    y/n")
elif q2 == '2':
    q3 = input("I just had a feeling you were here for that. Anyway, payment will be 1 shilling($70 in today's money) an hour.\
    Is that enough? y/n")
else:
    q2 = input("ENTER VALID ANSWER.")


if q3 == 'y':
    print("You graciously accept the payment. Walking to the corner, you start mopping the floor.")
elif q3 == "n":
    print("You ask if you can have more , and Dorthy responds, I can add some bonuses like me paying for insurance, if that\
is ok? Knowing that you hit the jackpot, you immediatly start working.")

q4 = input("Later that day, you are walking to your home. You finally have money to pay the rent. Deciding to celebrate. You can\
1) Take a good long rest, 2) Go out for a fancy dinner, or 3) Buy some tickets for the cricket game, with your favorite team\
playing.")

if q4 == '1':
    print("Heading home, you invite some friends over. After some fun small talk, your friends leave and you sleep soundly")
elif q4 == '2':
    print("")





