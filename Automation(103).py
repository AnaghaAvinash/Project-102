
print("What do you want to overcome?")
print("1.Procrastination   2.Laziness")
number = int(input("Choose a number, 1 or 2: "))

if (number == 1):
    print("Steps to overcome procrastination-")
    print("Step 1: Recognize that you're procrastinating.")    
    print("Step 2: Work out WHY you're procrastinating")    
    print("Step 3: Adopt Anti-Procrastination Strategies")    
    print("That's it!")
    print("a.More information b.Another task")
    moreP = input("Type a for more information or b to choose another task: ")
        
    if (moreP == "a"):
        print("Visit this for more information - https://www.mindtools.com/pages/article/newHTE_96.htm")
    elif (moreP == "b"):
        print("Choose something you want to overcome-")
        print("1.Procrastination   2.Laziness")
        number = int(input("Choose a number, 1 or 2: "))
    else:
        print("Sorry, that's not a valid input.")

elif (number == 2):
    print("Steps to overcome laziness-")
    print("Step 1: Make your goals manageable.")    
    print("Step 2: Ask for help")    
    print("Step 3: Make tedious tasks fun")   
    print("Step 4: Reward yourself")     
    print("That's it!")
    print("a.More information b.Another task")
    moreL = input("Type a for more information or b to choose another task: ")     
    if (moreL == "a"):
        print("Visit this for more information - https://www.healthline.com/health/how-to-stop-being-lazy#mental-tips-and-ideas")
    elif (moreL == "b"):
        print("Choose something you want to overcome-")
        print("1.Procrastination   2.Laziness")
        number = int(input("Choose a number, 1 or 2: "))
    else:
        print("Sorry, that's not a valid input.")
else:
    print("Sorry, that's not a valid option")