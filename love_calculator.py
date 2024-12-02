def calculate_love_score(name1, name2):
    combined_name = name1.upper() + " " + name2.upper()
    true_counter = 0
    for letter in combined_name:
        if "T" == letter:
            true_counter += 1
        elif "R" == letter:
            true_counter += 1
        elif "U" == letter:
            true_counter += 1
        elif "E" == letter:
            true_counter += 1

    # print("Total = ", true_counter)

    love_counter = 0
    for letter in combined_name:
        if "L" == letter:
            love_counter += 1
        elif "O" == letter:
            love_counter += 1
        elif "V" == letter:
            love_counter += 1
        elif "E" == letter:
            love_counter += 1

    # print("Love Total = ", + love_counter)

    love_score = str(true_counter) + str(love_counter)
    love_score_int = int(love_score)
    print(love_score_int)

calculate_love_score("Kanye West", "Kim Kardashian")