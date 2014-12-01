#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """

  # create the list

  babynames = []
  ranking = {}

  # open the file
  f = open(filename,'r')

  # read all the text from the file
  fulltext = f.read()

  # extract the year
  matchdate = re.search(r'Popularity in \d\d\d\d',fulltext)  
  date = re.search(r'\d\d\d\d',matchdate.group())

  # append year to list
  babynames.append(date.group())

  # extract each line of rank data
  matchranks = re.findall(r'<tr align="right"><td>\d+</td><td>\w+</td><td>\w+</td>',fulltext)
  for row in matchranks:

    # find the ranks 
    rank = re.search(r'\d+',row)
    
    # treat with the male/female names
    names = re.findall(r'<td>\w+</td>',row)
    
    # get rid of the <td> tags
    male = re.sub(r'<.*?>',r'',names[1])
    female = re.sub(r'<.*?>',r'',names[2])

    # add the names and ranks to a dictionary
    ranking[male] = rank.group()
    ranking[female] = rank.group()



  print babynames
  
  for name in sorted(ranking.keys()):
    print name, ranking[name]

  return babynames


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for arg in args:
    extract_names(arg)
  
if __name__ == '__main__':
  main()
