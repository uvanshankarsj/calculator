// Git/GitHub workshop: Hands on session
// Program: Calculator
// Author: Manav Patnaik

// Import required header files
#include <stdio.h>
#include <math.h>

// Calculator function to be written here
// Functionalities required:
// 1. Add
// 2. Subtract
// 3. Multiply
// 4. Divide
// 5. Percentage
// 6. Exponentiation
// 7. Sine (sin)
// 8. Cosine (cos)
// 9. Tangent (tan)
// 10. Square root
// 11. Ceil
// 12. Floor
// 13. Absolute value
// 14. Natural exponent (e^x)

// Sample code for 1. Add
double add(double a, double b) {
    return a + b;
}
// Code for 14. Natural Exponent (e^x)
/*
  Code Written By Rengaraj R
  Written on Windows 10 15-05-2021 17:55
  input  double 
  returns double
*/
double naturalExponent( double number)
{
    double answer;
    answer = exp(number);
    return answer;
}

double squareroot(double a){
    return sqrt(a);
}
// Insert your code below
#include<stdio.h>

void ceiling(float x)
{scanf("%f",x);
int ceil;
ceil=x/1;
if(ceil<=0) 
printf("the ceil of the number %d is %d",x,ceil);
else
ceil+=1;
printf("the ceil of the number %d is %d",x,ceil);
}

int main() {
    add();
}
