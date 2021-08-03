print('Welcome to the COVID-19 support service. Please select an option below')
print('1.Statistics')
print('2.Prevention')
print('3.Symptoms')
print('4.Treatment')
print('5.Report case')
print('6.Exit')

num = int(input("Enter choice(1/2/3/4/5/6):\n"))

if num == 1:
    print('Currently in South Africa there are 27 403 Confirmed cases')
    print('Currently in USA there are 1 700 000 Confirmed cases')
    print('Currently in China there are 82 995 Confirmed cases')

    ran = str(input("Would you like see the confirmed cases from a random country? y/n:"))
    if ran == 'y':
        random = int(input("Enter a number from 0 to 9 to see a random countries statistics\n"))

        # Random countries
        if random == 0:
            print("Australia has 7155 confirmed cases.\n")
        elif random == 1:
            print("UK has 900 000 confirmed cases\n")
        elif random == 2:
            print("Netherlands has 50 000 confirmed cases\n")
        elif random == 3:
            print("Brazil has 800 000 confirmed cases\n")
        elif random == 4:
            print("Argentina has 100 000 confirmed cases\n")
        elif random == 5:
            print("Canada has 30 000 confirmed cases\n")
        elif random == 6:
            print("Ghana 20 000 confirmed cases\n")
        elif random == 7:
            print("Saudi Arabia has 10 000 confirmed cases\n")
        elif random == 8:
            print("Thailand has 100 000 confirmed cases\n")
        elif random == 9:
            print("New Zealand has 40 000 confirmed cases\n")
    elif ran == 'n':
        exit(0)
elif num == 2:

    print("To prevent the spread of COVID-19:"
          "Clean your hands often. Use soap and water, or an alcohol based hand rub."
          "Maintain a safe distance from anyone who is coughing or sneezing.")
    print("Don't touch your eyes, nose or mouth."
          "Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze. "
          "Stay home if you feel unwell.")
    print("if you have a fever, cough and difficulty breathing, seek medical attention. "
          "Call in advance."
          " Follow the directions of your local health authority.")
    nom = str(input("Enter b to return to menu:"))
    if nom == 'b':
        exit(0)
        # menu
        # Symptoms

elif num == 3:

    print('''Most common symptoms:
            Fever
            Dry throat
            Tiredness''')
    print('''Less common symptoms:
            Aches and pains
            Diarrhea
            Conjunctions
            Headache 
            Loss of taste or smell)
            a Rash on skin
            or discolouration of fingers or toes''')
    print('''Serious symptoms:
            Difficulty breathing shortness of breath
            Chest pain or pressure
            Loss of speech or movement''')
    nom = str(input("Enter b to return to menu:"))
    if nom == 'b':
        exit(0)
        # menu
        # Treatment

elif num == 4:
    print("If you feel sick you should rest, "
          "drink plenty of fluids, "
          "and eat nutritious food. "
          "Stay in a separate room from other family members, "
          "and use a dedicated bathroom if possible. "
          "clean and disinfect frequently touched surfaces.")
    nom = str(input("Enter b to return to menu:"))
    if nom == 'b':
        exit(0)
        # menu
        # Report case
elif num == 5:
    sym = str(input("Do you have any of the symptoms? y/n:"))

    if sym == 'y':
        sym = str(input("Is your temperature above 38.5°C? y/n:"))

    if sym == 'y':
        sym_no = int(input('''In which country are you? Select an option below.
                1.SA
                2.USA
                3.China
                Enter option (1/2/3:)'''))
        if sym_no == 1:
            sym_count == intOne
            intOne += 1
            print(intOne)
        if sym_no == 2:
            sym_count == intTwo
            intTwo += 1
            print(intTwo)
        if sym == 3:
            sym_count == intThree
            intThree += 1
            print(intThree)
            print("You have COVID=19. Please seek treatment\n")

        elif sym == 'n':
            print("You don't have COVID-19\n")

            nom = str(input("Enter b to return to menu:\n"))
            if nom == 'b':
                exit(0)
                # menu
                # Exit

elif num == 6:
    print('Goodbye!')
    exit(0)
