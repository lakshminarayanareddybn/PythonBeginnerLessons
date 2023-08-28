## https://regexone.com/
## https://docs.python.org/3/library/re.html

## what are regular expressions?
## A regex, or regular expression is a sequence of characters 
## that forms a search pattern.

## Why we use RegEx?
## It can be used to check if a string contains
## the specific search pattern

## Python provides a module called `re` to work with 
## regular expressions

## RegEx not specific to language python
## Perl, Java, Ruby etc

import re

# print(dir(re))

# Some of the re functions that we discuss in next 2-3 days
# 'compile'
# 'findall', 
# 'fullmatch', 
# 'match', 
# 'search'
# 'split'
# 'sub'

txt = "The rain is Spain"

## Search the `txt` string if it starts with "The" and ends with "Spain"
result = re.search("^The.*Spain$", txt)

if result:
    print("Yes we have found match")
else:
    print("No match found!!")

## Meta characters those have special meaning in regular expressions

## [] - set of characters - [a-m] "abcdefghijklm"
## \  - signals escaping a special sequence - "\d"
## .  - Any chacter except newline - "he..o"
## ^  - Starts with   - "^hello"
## $  - Ends with - "planet$"
## *  - Zero or more occurrences  - "he.*o"  heo
## +  - One or more occrrences - "he.+o" helo
## ?  - Zero or one occurrence - "he.?o"
## {} - Exactly specified number of occurrences  - "he.{2}o" 
## |  - Either or       - falls|stays|sleeps
## () - Capture and group


## Special Sequences
## A special sequence is a `\` followed by one of the 
# characters which has special meaning

## \A : Returns a match if the specified characters are at the beginning of the string 
##      example: "\AThe"

## \b : Returns a match where the specified characters are at the beginning of the
## string or at the end of the string
##      example: "\brain" , "rain\b"

## \B : Returns a match where the specified characters are present, but NOT at the
## beginning or at the end of word.
##      example: "\Brain", "rain\B"

## \d :Returns a match where the string contains digits (numbers from 0-9)
##      example: "I got \d{2} ruppes money" (I got 56 ruppes money)

## \D : Returns a match where the string Does not contain the digits
##      example : "\D"

## \s  : Returns a match where the string contains a white space character
##      example : "\s"

## \S  : Returns a match where the string does not contain a white space
##      example : "\S"

## \w  : Returns a match where the string contain any work characters 
## (characters from a to Z (a-z, A-Z), digits from 0-9 and the _ underscore character )

## \W  : Returns a match where the string does not contain any word characters
##      example: "\W"

## \Z  : Returns a match if the specified characters are at the end of the string.
##      example: "Spain\Z"

## Sets
## Set of characters inside a pain of square brackets [] with a special meaning

## [arn] - Returns a match where one of the specified characters (a, r, or n) is present
## [a-n] - Returns a match for any lower case character, alphabetically between a and n.
## [^arn] - Returns a match for any character EXCEPT a, r and n.
## [0123] - Returns a match where any of the specifid digits (0,1,2,3) are present.
## [0-9] - Returns a match where any of the specifid digits (0 to 9) are present.
## [0-5][0-9] - Returns a match for any digit digit numbers from 00 to 59
## [a-zA-Z] - Returns a match for any character alphabetically b/w a and z,
## lower case or upper case.
