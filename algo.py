'''
2a) Zeller’s algorithm (Practice Program)
1. Write a program to compute Zeller’s algorithm, which is used to tell the day of the week, provided a date is given.
Ask the user for the month as a number between 1 – 12 where March is 1 and February is 12.
If born in Jan or Feb, enter previous year.
Zeller’s algorithm computation is defined as follows:
Let A, B, C, and D denote integer variables that have the following values:
A = the month of the year, with March having the value 1, April the value 2,
December the value 10, and January and February being counted as months 11 and
12 of the preceding year (in which case, subtract 1 from C)
B = the day of the month (1, 2, 3, … , 30, 31)
C = the year of the century (e.g. C = 89 for the year 1989)
D = the century (e.g. D = 19 for the year 1989)
Note: if the month is January or February, then the preceding year is used for computation. This is because there was a period in history when March 1st, not January 1st, was the beginning of the year.
Let W, X, Y, Z, R also denote integer variables. Compute their values in the following
order using integer arithmetic:
W = (13*A - 1) / 5
X = C / 4
Y = D / 4
Z = W + X + Y + B + C - 2*D
R = the remainder when Z is divided by 7
Hint: Use integer division “//” for division
Now the value of “R” is used to find the day of the week.
If R is zero, then it is a Sunday. If R is one, then it is Monday and so on. When R = 6, the day is Saturday.
Sample Output:

'''