# Explain, optimize, and benchmark your python code here.
def iterate_a_lot():
    for i in range(1000):
        for j in range(100):
            j


def iterate_a_little():
    for i in range(10):
        i

    # Reporting


import time
import statistics

list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]


def anagrams_for(word="threads"):
    """We receive a target word, and a list of strings that could potentially be our target word but scrambled.


    Args:
        word (String): This is our target word that we must find within a list of words if they exist
        list_of_words (List): This is our list of words to compare against

    Returns:
        List: List of all words that if any exist that match our target word
    """
    # We initialize an answer list to return
    answer_list = []
    # Let's loop through each word in the list of words
    for listed_word in list_of_words:
        # If both word, and listed_word while sorted are equal then
        if sorted(word) == sorted(listed_word):
            # Append to the answer list our match
            answer_list.append(listed_word)
    # We have cycled the entire list, let's return our answer list
    return answer_list


functions = anagrams_for, iterate_a_lot, iterate_a_little
# iterate_a_lot, iterate_a_little

# this is just a one line way to make this: {'iterate_a_lot': [], 'iterate_a_little': []}
times = {f.__name__: [] for f in functions}

for func in functions:
    for i in range(500):  # adjust accordingly so whole thing takes a few sec
        t0 = time.time()
        func()
        t1 = time.time()
        times[func.__name__].append((t1 - t0) * 1000)

for name, numbers in times.items():
    print('FUNCTION:', name, 'Used', len(numbers), 'times')
    print('\tMEDIAN', statistics.median(numbers))
    print('\tMEAN  ', statistics.mean(numbers))
    print('\tSTDEV ', statistics.stdev(numbers))
