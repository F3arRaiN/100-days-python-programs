def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    counter1 = 0
    counter2 = 0
    word1 = "true"
    word2 = "love"

    for letter in word1:
        for letter1 in name1:
            if letter == letter1:
                counter1 += 1
        for letter2 in name2:
            if letter == letter2:
                counter1 += 1
    
    for letter in word2:
        for letter1 in name1:
            if letter == letter1:
                counter2 += 1
        for letter2 in name2:
            if letter == letter2:
                counter2 += 1

    if counter1 > 9:
        counter1 = counter1 % 10
    
    if counter2 > 9:
        counter2 = counter2 % 10
    
    love_score = str(counter1) + str(counter2)
    print(int(love_score))
    
calculate_love_score("Kanye West", "Kim Kardashian")