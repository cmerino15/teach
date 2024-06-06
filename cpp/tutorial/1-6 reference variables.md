# Reference Variables

We now focus on a better way of accessing variables without the use of global variables 

> [!NOTE]
> We generally don't use global variables because they could be accidentally changed from anywhere. 

Instead, we use a reference variable **&a**. A reference variable is just another name for an already existing variable. This other name just has the added property that it can be referenced outside a function.  
Consider the following code. 

> main.cpp -> inside main function

```cpp
int a = 5;
int &b = a; 

std::cout << "The value of a is: " << b; 
```

The great thing about reference variables is that they can be used in functions and used to reference variables outside that function too.
We don't always need to do this however.
Consider the following code. 

> main.cpp

```cpp
#include <iostream>
int sumF(int a, int b);  // declares a function that will return an integer and accept two integers a and b
int main(){
   std::cout "The sum of 2 and 3 is " << sumF(2, 3); // takes 2 and 3 and passes it to the function to work with
}
int sumF(int a, int b){
  return a + b;  // return the sum of the two integers entered
}
```
In the above code, we just need to return the sum of two given values so no variables are needed.

> main.cpp

```cpp
#include <iostream>
int sumF(int a, int b);  // declares a function that will return an integer and accept two integers a and b
int main(){
   int sum, a = 5, b = 7;
   sum  = sumF(a, b); sums a and b and returns the sum to be stored in 'sum'
   std::cout "The sum of a and b is " << sum;
}
int sumF(int a, int b){
  return a + b;  // return the sum of the two integers entered
}
```

This changes the value of int sum by returning the sum. But we can also do this using a void function. I.E. without returning anything. 

Here's an example of this not quite working without a reference variable.
> main.cpp

```cpp
#include <iostream>
void sumF(int sum, int a, int b); // accepts inputs of sum (to be calculated) and a and b
int main(){
   int sum = 0, a =2, b = 8;
   sumF(sum, a, b); // calls the sumF function below
   std::cout << "The sum of a and b is " << sum; 
}
void sumF(int sum, int a, int b){ 
  sum = a + b;  // looks like sum should equal a + b. It does, but only inside this function. 
}
```

We change this by using a reference variable. 


> main.cpp

```cpp
#include <iostream>
void sumF(int &sum, int a, int b); // accepts inputs of a reference sum (to be calculated) and a and b
int main(){
   int sum = 0, a =2, b = 8;
   sumF(sum, a, b); // calls the sumF function below but now sum is passed as a reference
   std::cout << "The sum of a and b is " << sum; 
}
void sumF(int &sum, int a, int b){ 
  sum = a + b;  // sum equals a + b here and to whatever it was referencing ... i.e. the sum in the main function
}
```

To be very clear this also works if we call our reference variable something else. 

> main.cpp

```cpp
#include <iostream>
void sumF(int &x, int a, int b); // accepts inputs of a reference x (to be calculated) and a and b
int main(){
   int sum = 0, a =2, b = 8;
   sumF(sum, a, b); // calls the sumF function below but sum is passed as a reference by using x as it's reference
   std::cout << "The sum of a and b is " << sum; 
}
void sumF(int &x, int a, int b){ 
  x = a + b;  // x equals a + b. and it references sum so it also changes sum
}
```

