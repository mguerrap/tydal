def quiz():
    """
    Generates module 1 quiz
    outputs print statements
    user needs to type and line execute each answer before the next question shows up
    """
    
    print("Module 1 Quiz (5 questions)")
    print()
    #Question 1
    print("Question 1: Why is the Earth affected by the Moon?")
    print()
    print("a. Massive")
    print("b. Close/Proximity")
    print("c. It isn't")
    answer = input("Make your choice: ")
    if answer.lower() == "b":
        print("Correct!")
    else:
        print("Incorrect")
    #Question 2    
    print("Question 2: How many high and low tides are there in a day for a semidurinal tidal day?")
    print()
    print("a. 2 high, 1 low")
    print("b. 1 high, 1 low")
    print("c. 2 high, 2 low")
    answer = input("Make your choice: ")
    if answer.lower() == "c":
        print("Correct!")
    else:
        print("Incorrect") 
    #Question 3
    print("Question 3: The tidal period is of of 24 hours by __ due to the Earth's roation about it's axis?")
    print()
    print("a. None")
    print("b. 50 minutes")
    print("c. 1 hour")
    answer = input("Make your choice: ")
    if answer.lower() == "b":
        print("Correct!")
    else:
        print("Incorrect") 
    #Question 4    
    print("Question 4: Spring tide causes tidal bulges to be ___ high tide and ___ low tide?")
    print()
    print("a. higher, lower")
    print("b. higher, higher")
    print("c. lower, higher")
    answer = input("Make your choice: ")
    if answer.lower() == "a":
        print("Correct!")
    else:
        print("Incorrect") 
    #Question 5    
    print("Question 5: Neap tide (First and Third Quarter moon) causes tidal bulges to be ___ high tide and ___ low tide?")
    print()
    print("a. higher, lower")
    print("b. higher, higher")
    print("c. lower, higher")
    answer = input("Make your choice: ")
    if answer.lower() == "c":
        print("Correct!")
    else:
        print("Incorrect") 
    print("Go to Module 2")