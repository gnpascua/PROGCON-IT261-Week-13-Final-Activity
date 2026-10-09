# PROGCON-IT261-Week-13-Final-Activity-P03
This repository is for the Final Activity Pair Programming Assignment. 

**Program Logic:**
The Pet Care Points Calculator helps users track the points they earn from taking care of their pets. First, Flowy greets the user and asks for their name and the number of pet care activities they have finished. For each activity, the user enters an activity code and the number of minutes spent. The program uses the computePetCarePoints() function to calculate the points earned: walking gives 4 points per minute, playing gives 3 points per minute, and grooming gives 2 points per minute. Invalid activity codes earn 0 points. The program repeats this process for every activity, adds the points to the total, and displays the user's name and total points earned.

**Flowchart Outline:**
**Main Function:**
1. Start the program and display Flowy's greeting.
2. Ask for the user's name and number of activities.
3. Initialize totalPoints = 0 and index = 1.
4. Use a While loop to repeat the following steps while index <= numActivities.
5. Display the user's name and total points earned.
6. End the program.

**computePetCarePoints() Function:**
1. Receive activityCode and minutes.
2. Initialize petCarePoints = 0.
3. If the activity code is 1, calculate 4 * minutes.
4. If the activity code is 2, calculate 3 * minutes.
5. If the activity code is 3, calculate 2 * minutes.
6. Return petCarePoints to the Main function.
7. End the function.
