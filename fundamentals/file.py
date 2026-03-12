# program_to_count_the_number_of_capital_letter.py
with open("SOME_LARGE_FILE.txt","r") as file:
    count = 0
    text = file.read()
    for character in text:
        if character.isupper():
            count +=1

    print("Number of uppercase letters:", count)
