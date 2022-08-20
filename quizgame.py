print("Welcome to my computer quiz!")


playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! let's play :)")
score = 0
answer = input("what does CPU stand for? ").lower()
if answer == "central processing unit":
    print('correct!')
    score += 1
else:
    print('wrong!')
    print('Try again!')

answer = input("what does GPU stand for? ").lower()
if answer == "graphic processing unit":
    print('correct!')
    score += 1
else:
    print('wrong!')
    print('Try again!')

answer = input("what does RAM stand for? ").lower()
if answer == "random access memory":
    print('correct!')
    score += 1
else:
    print('wrong!')
    print('Try again!')

answer = input("what is JS? ").lower()
if answer == "javascript":
    print('correct!')
    score += 1
else:
    print('wrong!')
    print('Try again!')

print("You GOT " + str(score) + " QUESTIONS CORRECT")
print("You GOT " + str((score/4)* 100) + "%")



