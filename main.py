import random

def first_template() :
    number = getNumber("Type Number: ")
    date = getNumber("Type a Measure of Time: ")
    transport = getString("Type Mode of Transport: ")
    adjective = getString("Type Adjective: ")
    adjective2 = getString("Type Adjective 2: ")
    noun = getString("Type Noun: ")
    color = getString("Type a Color: ")
    body = getString("Type Part of the Body: ")
    verb = getString("Type Verb: ")
    number2 = getString("Type Number 2: ")
    noun2 = getString("Type Noun 2: ")
    noun3 = getString("Type Noun 3: ")
    body2 = getString("Type Part of the Body 2: ")
    noun4 = getString("Type Noun 4: ")
    adjective3 = getString("Type Adjective 3: ")
    sillyWord = getString("Type Silly Word: ")

    print("It was about " + number + " " + date + " ago when I arrived at the hospital in a " + transport + ".")
    print(" The hospital is a/an " + adjective + " place, there are a lot of " + adjective2 + " " + noun + " here.")
    print(" There are nurses here who have " + color + " " + body + ".")
    print(" If someone wants to come into my room I told them that they have to " + verb + " first.")
    print(" I’ve decorated my room with " + number2 + " " + noun2 + ".")
    print(" Today I talked to a doctor and they were wearing a " + noun3 + " on their " + body2 + ".")
    print(" I heard that all doctors " + verb + " " + noun4 + " every day for breakfast.")
    print(" The most " + adjective3 + " thing about being in the hospital is the " + sillyWord + " " + noun + "! ")

def second_template() :
    properNoun = getString("Type Proper Noun (Person’s Name): ")
    noun = getString("Type Noun: ")
    adjective = getString("Type Adjective (Feeling): ")
    verb = getString("Type Verb: ")
    animal = getString("Type an Animal: ")
    adjective2 = getString("Type Adjective (Feeling) 2: ")
    verb2 = getString("Type Verb 2: ")
    color = getString("Type a Color: ")
    verbing = getString("Type a Verb (ending in ing): ")
    adverb = getString("Type Adverb (ending in ly): ")
    number = getNumber("Type Number : ")
    date = getNumber("Type Measure of Time: ")
    noun2 = getString("Type Noun 2: ")
    sillyWord = getString("Type Silly Word: ")

    print("This weekend I am going camping with " + properNoun + ".")
    print(" I packed my lantern, sleeping bag, and " + noun + ".")
    print(" I am so " + adjective + " to " + verb + " in a tent.")
    print(" I am " + adjective2 + " we might see a(n) " + animal + ", I hear they’re kind of dangerous.")
    print(" While we’re camping, we are going to hike, fish, and " + verb2 + ".")
    print(" I have heard that the " + color + " lake is great for " + verbing + ".")
    print(" Then we will " + adverb + " hike through the forest for " + number + " " + date + ".")
    print(" If I see a " + color + " " + animal + " while hiking, I am going to bring it home as a pet! At night we will tell " + number + " " + sillyWord + " stories and roast " + noun2 + " around the campfire!! ")

def third_template() :
    properNoun = getString("Type Proper Noun (Person’s Name): ")
    adjective = getString("Type Adjective: ")
    color = getString("Type a Color: ")
    animal = getString("Type an Animal: ")
    place = getString("Type Place: ")
    adjective2 = getString("Type Adjective: ")
    creature = getString("Type Magical Creature (Plural): ")
    adjective3 = getString("Type Adjective 3: ")
    creature2 = getString("Type Magical Creature (Plural) 2: ")
    room = getString("Type Room in a House: ")
    noun = getString("Type Noun: ")
    noun2 = getString("Type Noun 2: ")
    noun3 = getString("Type Noun (Plural) 3: ")
    adjective4 = getString("Type Adjective 4: ")
    noun4 = getString("Type Noun (Plural) 4: ")
    number = getNumber("Type number: ")
    date = getNumber("Type Measure of Time: ")
    verbing = getString("Type a Verb (ending in ing): ")
    adjective5 = getString("Type Adjective 5: ")
    noun5 = getString("Type Noun 5: ")

    print("Dear " + properNoun + ", I am writing to you from a " + adjective + " castle in an enchanted forest.")
    print(" I found myself here one day after going for a ride on a " + color + " " + animal + " in " + place + ".")
    print(" There are " + adjective2 + " " + creature + " and " + adjective3 + " " + creature2 + " here! In the " + room + " there is a pool full of " + noun + ".")
    print(" I fall asleep each night on a " + noun2 + " of " + noun3 + " and dream of " + adjective4 + " " + noun4 + ".")
    print(" It feels as though I have lived here for " + number + " " + date + ".")
    print(" I hope one day you can visit, although the only way to get here now is " + verbing + " on a " + adjective5 + " " + noun5 + "!!")

def getString(req) :
    res = input(req)
    if type(res) != str or res.isdigit():
        print("Invalid Input!")
        getString(req)        
    return res

def getNumber(req) :
    res = input(req)
    try:
        res = int(res)
    except ValueError:
        print("Invalid Number!")
        getNumber(req)        
    return res

try:
    template = int(input("Which Template you going to pick (1, 2, 3, 4(for random)): "))
except ValueError:
    print("Invalid number!")

if template == 4 :
    template = random.randint(1, 3)

match template:
    case 1:
        first_template()
    case 2:
        second_template()
    case 3:
        third_template()
    case _:
        print("Invalid Template Number.")
