def quiz():
   """
    Generates module 2 quiz
    outputs print statements
    user needs to type and line execute each answer before the next question shows up
    """
    #Question 1
    print("Module 2 Quiz (4 questions)")
    print()
    print("Question 1: A tide is _____?")
    print()
    print("a. a wave")
    print("b. random")
    print("c. made by whales")
    answer = input("Make your choice: ")
    if answer.lower() == "a":
        print("Correct!")
    else:
        print("Incorrect")

    #Question 2
    print("Question 2: Peak tide elevation at each port happens at the same time: True or False: ?")
    print()
    print("a. True")
    print("b. False")
    answer = input("Make your choice: ")
    if answer.lower() == "b":
        print("Correct!")
    else:
        print("Incorrect")

    #Question 3
    print("Question 3: Neah Bay's tidal elevation is always higher than Port Townsends: True or False?")
    print()
    print("a. True")
    print("b. False")
    answer = input("Make your choice: ")
    if answer.lower() == "b":
        print("Correct!")
    else:
        print("Incorrect")
    #Question 4
    print("Question 4: If Neah Bay's tidal elevation is lower than Port Townsends, which way is the water flowing")
    print()
    print("a. To the Ocean")
    print("b. To the Estuary")
    print("c. Nowhere")
    answer = input("Make your choice: ")
    if answer.lower() == "a":
        print("Correct!")
    else:
        print("Incorrect")
    print("Go to Module 3")