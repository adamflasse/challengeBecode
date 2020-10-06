#Challenge 'OCR digits'
by Adam

First I needed to identify each digit with underscores and pipes.
So I've created lists for each digits composed by 4 elements (each element is a line).


Then I've defined a function ( check_input() ) with the role of checking what digits it is and if it's garble it will return an '?'.

The second function is to basically deal with multiple digits. So it takes as an argument a list with 4 long strings. The problem here was the fact that the digits were divided by lines and not by digits. The goal of the divide_digits function was to gather each digit in a similar list as defined at the beginning.

The final function takes as an argument the result of the previous method and goes through each digit's list, calls the first function to know which digit it is and place the result in a string.

I hope that the challenge is succesfully completed!



 
