def computePetCarePoints(activityCode, minutes):
    if activityCode == 1:
        petCarePoints = 4 * minutes
        print("For Activity 1, you earned " + str(petCarePoints) + " points.")
    else:
        if activityCode == 2:
            petCarePoints = 3 * minutes
            print("For Activity 2, you earned " + str(petCarePoints) + " points.")
        else:
            if activityCode == 3:
                petCarePoints = 2 * minutes
                print("For Activity 3, you earned " + str(petCarePoints) + " points.")
            else:
                petCarePoints = 0
                print("For Activity 3, you earned " + str(petCarePoints) + " points.")
    
    return petCarePoints

# Main
print("Hello, dear user! I am Flowy, your friendly pet caretaker. I am here to help you keep track of the time you spend taking care of your pets and calculate the pet care points you earn! But before that, what's your name?")
name = input()
print("What a great name, " + name + "! Now, let's start calculating your pet care points, shall we? Let's see how many points you can earn from walking, playing with, and grooming your pets!")
print("How many pet care activities did you complete?")
numActivities = int(input())
totalPoints = 0
index = 1
while index <= numActivities:
    print("Enter activity code:")
    activityCode = int(input())
    print("Enter the duration in minutes:")
    minutes = int(input())
    petCarePoints = computePetCarePoints(activityCode, minutes)
    totalPoints = totalPoints + petCarePoints
    index = index + 1
print("Dear " + name + ", you earned " + str(totalPoints) + " pet care points!")
