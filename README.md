# luhn_gen
Command line tool to create a list of all possible "masked" values in a credit card number that would pass the luhn (i.e. mod10) check.

Example Usage:
shell$ python luhn_gen.py 123456789012345X
['123456789012345', 'X', '']
1234567890123452
Number of possible values passing Luhn check: 1
shell$
