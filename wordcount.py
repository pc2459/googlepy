#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# create a dictionary to store words
words = {}

#########

def open_and_count(filename):
  """Opens and reads words and their counts into a dictionary"""

  # open the file
  f = open(filename,'r')

  # iterate through each line
  for line in f:
    # split words on whitespace
    allthings = line.split()

    # add words to the dictionary
    for word in allthings:
      if word.lower() not in words:
        words[word.lower()] = 1
      else:
        words[word.lower()] += 1

  f.close()

#########

def get_count(dictionary):
  """Helper function to grab the count from a word/count dictionary tuple"""
  return dictionary[1]

#########

def print_words(filename):
  """Prints all the words and their counts from a file"""
  open_and_count(filename)
  for word in sorted(words.keys()):
    print word, words[word]

#########

def print_top(filename):
  """Prints the top twenty words and their counts from a file"""

  # open and build the wordcount dictionary
  open_and_count(filename)
  
  # sort the tuples list of the dictionary by the second item in the tuple pair (the count) 
  toplist = sorted(words.items(), key=get_count, reverse=True)

  for word, count in toplist[:20]:
    print word, count

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
