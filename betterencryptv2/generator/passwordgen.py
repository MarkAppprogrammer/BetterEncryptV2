import string
import random
import yake
from random_word import RandomWords
import os

#from rake_nltk import Rake 
#import nltk


#vars
alphabet = list(string.ascii_lowercase)
numbers = list(string.digits)
specialChars = list(string.punctuation)
r = RandomWords()
#nltk.download('stopwards')
#rake = Rake()


def passwordAlgorithm(securityLevel, memorabilityLevel, prompt):
    baseLength = max(8, min(12, securityLevel + 5 - memorabilityLevel))
    lengthModifier = (securityLevel - memorabilityLevel) / 2
    finalLength = baseLength + lengthModifier

    numUppercase = round(finalLength * securityLevel / 20)
    numLowercase = round(finalLength * (10 - securityLevel) / 20)
    numNumbers = round(finalLength * securityLevel / 25)
    numSpecial = finalLength - numUppercase - numLowercase - numNumbers

    password = ""
    password += randomChar(numUppercase, [char.upper() for char in alphabet])
    password += randomChar(numLowercase, alphabet)
    password += randomChar(numNumbers, numbers)
    password += randomChar(numSpecial, specialChars)

    # add shuffle function
    shuffle(password)

    # add memrobality / pattern maker if mem > 5
    if (memorabilityLevel >= 5):
        password = patternize(memorabilityLevel, password, prompt)

    return password

def shuffle(password):
    return ''.join(random.sample(password, len(password)))

def randomChar(n, inputList):
    string = ""
    for _ in range(int(n)):
        string += inputList[random.randrange(0, len(inputList) - 1, 1)]
    return string#generate n random 

def patternize(memorabilityLevel, password, prompt):
    #get key phrases
    keywords = []

    kw_extractor = yake.KeywordExtractor()
    begKeywords = kw_extractor.extract_keywords(prompt)
    
    for kw in begKeywords:
        keywords.append(kw[0])
    
    #print(keywords)
    #rake.extract_keywords_from_text(prompt)
    #keywords = rake.get_ranked_phrases()
    #print("inital:" + str(keywords))

    if (len(keywords) > 11):
        numLetters = random.randint(2, 5)
        keywords = [keyword[0:numLetters+1] for keyword in keywords]
    else:
        keywords = [keyword[0:random.randint(2, 5)+1] for keyword in keywords]
    #print("new:" + str(keywords))

    # decide how many patterns wanted ( 5 = .5 and 10 = 2.5)
    numPatterns = round((memorabilityLevel - 4) * .6)
    #print(str(numPatterns))

    """     for _ in range(numPatterns):
        password += keywords[random.randint(0, len(keywords) - 1)] """
    
    #print(password)
    for _ in range(numPatterns):
        start_index = random.randint(0, len(password))
        end_index = random.randint(start_index, len(password))
        keyword = keywords[random.randint(0, len(keywords) - 1)]
        password = password[:start_index] + keyword + password[end_index:]


    return password


""" test
print(passwordAlgorithm(7, 6, "home computer I acess everyday and stores my taxes")) """

def select_word():
    random_line_number = random.randint(1, 10000)

    current_dir = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(current_dir, 'words.txt')

    with open(file_path, "r") as file:
        for current_line_number, line in enumerate(file, start=1):
            if current_line_number == random_line_number:
                selected_word = line.strip()  # Remove any extra spaces or newlines
                break

    return selected_word

def passphraseAlgorithm(request):
    breaker = ""
    if request.POST.get('none') == "True":
        breaker = ""
    elif request.POST.get('spaces') == "True":
        breaker = " "

    numWords = random.randint(5, 7)

    password = ""

    for _ in range(numWords):
        password += select_word() + breaker

    if request.POST.get('numbers') == "True":
        password += str(random.randint(0, 9))
    if request.POST.get('uppercase') == "True":
        choice = random.randint(0, len(password) - 1)
        print(password[choice])
        print(type(password[choice]))
        password = password[:choice] + password[choice].upper() + password[choice + 1:]
    if request.POST.get('specialChars') == "True":
        password += randomChar(1, specialChars)
        
    return password