first_template = "It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation). The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. There are nurses here who have (Color) (Part of the Body ). If someone wants to come into my room I told them that they have to (Verb) first. I’ve decorated my room with (Number2) (Noun2). Today I talked to a doctor and they were wearing a (Noun3) on their ( Part of the Body 2). I heard that all doctors (Verb) (Noun4) every day for breakfast. The most ( Adjective3) thing about being in the hospital is the (Silly Word ) (Noun) ! "
second_template = "This weekend I am going camping with ( Proper Noun (Person’s Name)). I packed my lantern, sleeping bag, and (Noun). I am so (Adjective (Feeling)) to (Verb) in a tent. I am (Adjective (Feeling) 2) we might see a(n) (Animal), I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and (Verb2). I have heard that the (Color) lake is great for ( Verb (ending in ing) ). Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure of Time). If I see a (Color) (Animal) while hiking, I am going to bring it home as a pet! At night we will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!! "
third_template = "Dear (Proper Noun (Person’s Name) ), I am writing to you from a (Adjective) castle in an enchanted forest. I found myself here one day after going for a ride on a (Color) (Animal) in (Place). There are (Adjective2) (Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural)2) here! In the ( Room in a House) there is a pool full of (Noun). I fall asleep each night on a (Noun2) of (Noun(Plural)3) and dream of (Adjective4) ( Noun (Plural)4). It feels as though I have lived here for (Number) ( Measure of time). I hope one day you can visit, although the only way to get here now is (Verb (ending in ing)) on a (Adjective5) (Noun5)!!"

def first_template() :
    number = int(input("Type Number: "))
    date = input("Type a Measure of Time: ")
    transport = input("Type Mode of Transport: ")
    adjective = input("Type Adjective: ")
    adjective2 = input("Type Adjective 2: ")
    noun = input("Type Noun: ")
    color = input("Type a Color: ")
    body = input("Type Part of the Body: ")
    verb = input("Type Verb: ")
    number2 = input("Type Number 2: ")
    noun2 = input("Type Noun 2: ")
    noun3 = input("Type Noun 3: ")
    body2 = input("Type Part of the Body 2: ")
    # verb
    noun4 = input("Type Noun 4: ")
    adjective3 = input("Type Adjective 3: ")
    sillyWord = input("Type Silly Word: ")
    # noun

    print("It was about " + number + " " + date + " ago when I arrived at the hospital in a " + transport + ".")
    print(" The hospital is a/an " + adjective + " place, there are a lot of " + adjective2 + " " + noun + " here.")
    print(" There are nurses here who have " + color + " " + body + ".")
    print(" If someone wants to come into my room I told them that they have to " + verb + " first.")
    print(" I’ve decorated my room with " + number2 + " " + noun2 + ".")
    print(" Today I talked to a doctor and they were wearing a " + noun3 + " on their " + body2 + ".")
    print(" I heard that all doctors " + verb + " " + noun4 + " every day for breakfast.")
    print(" The most " + adjective3 + " thing about being in the hospital is the " + sillyWord + " " + noun + "! ")

def second_template() :
    print("")

def third_template() :
    print("")

template = int(input("Which Template you going to pick (1, 2, 3): "))

match template:
    case 1:
        first_template()
    case 2:
        second_template()
    case 3:
        third_template()
    case _:
        print("Invalid Template Number.")
