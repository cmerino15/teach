# If/Else-If Conditional Statements and the Basic For Loop

We can use if and else-if statements to write conditional code. 
For example, say we wanted to ask the user to choose their honorific (either mr and mrs to keep it simple for now).
Then, we want to cout a greeting. We can do this with an if and else-if statement. 

> [!NOTE]
> We only need one if statement and we can nest as many else-if statements as we want. Furthermore, we can end with an optional else statement.

> Ex: main.cpp

```cpp
#include <iostream>
int main(){
  int x = 0;
  std::cout <<"Enter 1 if you prefer Mr. and 3 if you prefer Mrs.\n";
  std::cin >> x;  // awaits for user to enter any integer
  if(x == 1){  // notice the use of double equals.  x == 1 may evaluate to 'true' or 1 OR it may evaluate to 'false' or 0
    std::cout <<"Welcome, Mr. " << std::endl; // you can add more code as you please
  } else if ( x == 3){ 
    std::cout <<"Welcome, Mrs. " << std::endl;
  }
  // the following code is optional ... but, be careful, an else statement must always follow an if statement
  else {   // notice there is nothing to evaluate...this handles all other cases or integers entered
    std::cout <<"You didn't enter a valid answer (1 or 3) \n";
  }
}
```

> output

```console
  Enter 1 if you prefer Mr. and 3 if you prefer Mrs.
  <your input...assume you enter 3>
  Welcome, Mrs. 
```

In C++, we can also use a basic C-style for-loop (We'll cover other types of for loops later). 
The for loop is used to run code for a certain range of integers. 
For example, assume you wanted to ask the user to enter 3 numbers and return the numbers squared. 
You could do that with a for loop. We first initialized what we call a counter (usually starting at 0) and then increase or increment the counter by 1 three times. 

> Ex: In main.cpp

> [!NOTE]
> From now on I won't include the entire code in the main.cpp file. For now, though, everything should be inside of the main loop.

```cpp
// in the line below we need semicolons to separate the expressions. Also, i++ is another way of writing i = i + 1
for( int i = 0; i < 3; i++){ // read 'for the integer i starting at 0, while i is less than 3, execute some code below, and then increment the counter i by 1
  std::cout << "Enter an integer: ";
  std::cin >> x; // x should be declared before the for loop somewhere
  std::cout << i*i << std::endl;  // the code to be executed
}
```

> output

```console
  Enter an integer: <input>
  <input>^2
  Enter an integer: <input>
  <input>^2
  Enter an integer: <input>
  <input>^2
``` 

You should read up on other C++ loops and conditional statements on your own. See the learncpp link in the main readme file. 

# Modern C++
## Range-Based For Loop

With the **auto** keyword, we can write for loops much quicker. 

The basic syntax is `for(auto x : y){ //run some code }`

Read, for some deduced type x, in the collection y, run some code. 

We'll talk about what types of 'collections' we can use in later sections (arrays and beyond). For now, the easiest example that you can use is with the std::string 'collection' or 'object' or 'container'.

> Ex: main.cpp

```cpp
#include <iostream>
int main(){
  std::string y = "some randome message";

  for( auto x: y){  // read, for the characters x in the string y ...
    std::cout << x; // ... print the character x
  }
  // also try
  for( auto x: y){
    std::cout << x << std::endl;
  }
}
```

> [!NOTE]
> I won't always show the output of the code in this tutorial. My suggestion is to open Replit (or the IDE of your choice) and try running the code yourself.
> If you're a beginner, then I suggest you type the code out instead of copying and pasting.


