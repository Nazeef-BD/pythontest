import random, math
print("Number guessing game!!!")
rand=0
while rand == 0:
    rand= math.floor(random.random()*50)+1
i=0
while i!=5:
    guess=int(input("What is your guess?"))
    if guess==rand:
        print("You got the number!!!")
        breaki=True
        break
    elif abs(rand-guess)<7:
        print("Very close! 🔥hot")
        i+=1
        print("You have ",5-i," ❤hearts  left!")
        breaki=False
    elif abs(rand-guess)<13:
        print("Very close! 🌡warm")
        i+=1
        print("You have ",6-i," ❤hearts  left!")
        breaki=False
    elif abs(rand-guess)<30:
        print("not close! 🥶cold")
        i+=1
        print("You have ",5-i," ❤hearts  left!")
        breaki=False
    else:
        print("Very not close! 🧊ice cold")
        i+=1
        print("You have ",5-i," ❤hearts  left!")
        breaki=False

if breaki==True:
        print("Congrats")

if breaki==False:
    print("The answer was,,,",rand)
