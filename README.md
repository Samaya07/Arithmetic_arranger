# Arithmetic_arranger
This repository has a code that changes an arithmetic question into the standard form that is shown in classroom textbooks
Students in primary school often arrange arithmetic problems vertically to make them easier to solve.
Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
1. If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
2. The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
3. Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
4. Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
