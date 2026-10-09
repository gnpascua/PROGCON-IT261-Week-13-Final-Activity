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
