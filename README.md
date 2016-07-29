# luhn_gen
Command line tool to create a list of all possible "masked" values in a credit card number that would pass the luhn (i.e. mod10) check.

Example Usage:<br>
shell$ python luhn_gen.py 123456789012345X<br>
['123456789012345', 'X', '']<br>
1234567890123452<br>
Number of possible values passing Luhn check: 1<br>
shell$<br>
