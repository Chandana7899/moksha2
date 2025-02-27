Implementation and Approach
This script uses Python to perform an infinite set of arithmetic on user input.

Step-by-Step Breakdown
1. Ask the user how many numbers they want to calculate with (`a`).
2. The first number will be taken as an integer and stored in `answer`, which is the first value. As this is the starting value.
3. `(a-1)` times, enter: 
   - One arithmetic operation operators: `+`, `-`, `*`, `/`.
   - Another number being input as a floating-point.
4. The program then checks which operation was chosen and applied it to `answer`.
5. The program avoids division by zero if the divisor is zero.
6. After every iteration, new results will always be printed.
7. The final answer is printed out in the end.


Extra Features and Possible Improvements
Features:
- Multiarithmetic operation support.
- Division by zero protection.
- Result after each arithmetic operation is announced.

Possible Improvements:
1. Input Validation: 
   - Input validation for proper numbers and operators must take place.
2. The Loop to be more Robust:
   - The final result should be shown outside the loop to avoid repetition of results.
3. Better User Experience:
   - Do step-by-step calculation.
   - Allow continuity/modification if a wrong value is entered.
4. It should include computational precedence with parentheses.
-Evaluating the operation from left to right without precedence of operations. 
