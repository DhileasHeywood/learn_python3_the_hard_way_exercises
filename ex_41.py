import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# setting up the phrases that the script is going to use to drill me
PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%",
    "class%%%(object):\n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and *** params",
    "class%%%(object):\n\tdef ***(self, @@@)" :
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "set *** to an instance of class %%%",
    "***.***(@@@)":
        "form *** get the *** function, call it with params self, @@@",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'"
}

#do they want to drill phrases first? If you specify when you run the script that you want the phrase to come first, it will, otherwise you'll get the code first.
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FISRT = True
else:
    PHRASE_FISRT = False

# load up the words from the website
# using the urlopen function that was imported.
# For each of the words imported, the words are stripped (removes leading and trailing characters), and encoded in utf-8 so that they can be read by terminal.
# They're then appended onto the WORDS list
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding = "utf-8"))


# defining a function!
# It does quite a lot.

def convert(snippet, phrase):
    # first, it defines class_names, which takes a random sample of words from the WORDS list, capitalises them, then makes a list out of them.
    # It'll take a random sample of words, from the number of times that "%%%" appears in the snippet.
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    # The other_names variable is a random sample from the WORDS list, that is as big as the number of times "%%%" appears in the offending snippet.
    other_names = random.sample(WORDS, snippet.count("%%%"))
    # Two empty lists are made, results and param names.
    results = []
    param_names = []

    # The first for loop. For i (a nice little temporary variable name) in the range of 0 - the number of times that "@@@" appears in the offending snippet.
    for i in range(0, snippet.count("@@@")):
        #first, it will choose a number between 1 and 3 inclusive using random.randint(), and assign it to param_count
        param_count = random.randint(1, 3)
        # then it will append param_names with: a random sample of words from WORDS, of size param_count, joined by ", "
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    # The next for loop:
    # for each sentence in snippet first, and then phrase, result is equal to the whole string.
    for sentence in snippet, phrase:
        result = sentence[:]

        #fake class names
        # for each word in class_names, result gets overwritten as the same sentence, but with 1 instance of %%% replaced with said word.
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        # for each word in other_names, result is overwritten with the same sentence, but with 1 instance of *** replaced by said word
        for word in other_names:
            result = result.replace("***", word, 1)

        #fake parameter lists
        # for each word in param_names, result is overwritten with the same sentence, but with 1 instance of @@@ replaced by said word
        for word in param_names:
            result = result.replace("@@@", word, 1)

        # the results string is then appended onto results. Results should be a string with no %*@ on it at all
        results.append(result)

    # just returns results at the end.
    return results

# keep going until they hit ctrl-D
# every time you hit enter, the while loop will run, because it's set to while True.
try:
    while True:
        # snippets is set to a list of the keys from the PHRASES dict.
        snippets = list(PHRASES.keys())
        # the snippets list is then shuffled into a random order.
        random.shuffle(snippets)

        # a for loop to go through the snippets lists
        for snippet in snippets:
            # setting phrase to be the value from PHRASES that the snippet, which is the key, relates to.
            phrase = PHRASES[snippet]
            # setting the variables question and answer to be the return values of the convert function above.
            # the convert function should return a tuple of the altered key and the altered value from the dict
            question, answer = convert(snippet, phrase)
            # Then if you want to have the english first to convert to code, this is what does that.
            if PHRASE_FISRT:
                question, answer = answer, question

            #then we shall print the question, or answer depending on what you've asked for.
            print(question)

            # The script asks for input, and whatever you type, will print what the answer should be afterwards.
            input("> ")
            print(f"ANSWER: {answer}\n\n")

# When you press ctrl-D, the input() function is interrupted, which generates an End-Of-File-Error, which will exit the program
except EOFError:
    print("\nBye")
