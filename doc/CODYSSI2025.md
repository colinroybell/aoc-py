# Codyssi 2025

## General and setup

Some sort of general config for these puzzles (how many, prefix)

Consider what bringup should look like (skipped, with an assert commented out)

## Run scripts

Best would be to have a prefix defined (in a file? in an environment variable) for current puzzle set, day and part, and then the run and test scripts deal with that. Including one to put an answer in.

## day 03

Nicer to have a general range union class

## day 06

Here's notes on the filter for part 1: https://www.geeksforgeeks.org/python-count-of-elements-matching-particular-condition/

## day 08

Can we put PART in the class rather than passing it around? Yes... I realise I don't quite know how the aoc_module stuff works any more.

We will need to put a PART = None in the template.

## day 13

Would like to abstract out breadth-first-search into own function

Is my method for part 3 best?