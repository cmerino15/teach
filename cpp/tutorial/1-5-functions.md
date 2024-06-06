# Functions

We can write functions to save ourselves the time of rewriting code that we will often use. 
For example, say you want to create a username for a user based on their favorite number and name. 
If you only had one user, the code could be written as follows. 

> main.cpp

```cpp
#include <iostream>
int main(){
  std::string fname, lname, favnum;
  std::cout << "Enter your first and last name\n";
  std::cin >> fname >> lname;
  std::cout << "Thanks, " << fname << ". Now enter you favorite number\n";
  std::cin >> favnum;
  std::string uname = fname.at(0) + lname + favnum;  // std::string has an .at() function that lets us access the nth character of the string, by entering n-1.
  std::cout << "Thank you. Your username is " << uname;
}
```

Try running this code on your own and try different values for the 'at' function, to get the hang of it. 
This is great and all, but if we wanted to let the user create 100 usernames (using a file, for example), then we would benefit from having being able to repeat the code without writing it out again.
This is where functions come in. (We'll see how to read in data from files later.)

In C++, we have two basic types of functions. Void functions that don't return values and Value Returning functions that return a value. First, we'll focus on a void function so that we can easily copy our old code and paste it in our function. I'll show you how we could write this program with a value returning function further below.

In C++, we split a function into it's declaration and definition. The declaration usually goes before the main function and the definition afterward. Here's what the function would look like for our example. 

> main.cpp

```cpp
#include <iostream>

void createUName(); // all this does is it tells the compiler what the function's return type is (void) and its parameters (none)

int main(){
  createUName();   // the program jumps to our function definition below and runs that code once
  createUName();   // the program jumps to our function definition and runs that code again
  createUName();   // and again ... great! we didn't have to type all that code out again 
}

// here is where we actually define what our function will actually do everytime it's called
void createUname(){
  std::string fname, lname, favnum;
  std::cout << "Enter your first and last name\n";
  std::cin >> fname >> lname;
  std::cout << "Thanks, " << fname << ". Now enter you favorite number\n";
  std::cin >> favnum;
  std::string uname = fname.at(0) + lname + favnum;
  std::cout << "Thank you. Your username is " << uname;
}
```

And now using a value (string) returning function. In a very rough way.

> main.cpp

```cpp
#include <iostream>

std::string createUName(); // all this does is it tells the compiler what the functions return type is (void) and its parameters (none)

int main(){

  
  std::cout << "Thank you. Your username is " << createUName();   // the program jumps to our function definition and runs that code once
  std::cout << "Thank you. Your username is " << createUName();    // the program jumps to our function definition and runs that code again
  std::cout << "Thank you. Your username is " << createUName();    // and again ... great! we didn't have to type all that code out again 
}

// here is where we actually define what our function will actually do everytime it's called
st::string createUname(){
  std::string fname, lname, favnum;
  std::cout << "Enter your first and last name\n";
  std::cin >> fname >> lname;
  std::cout << "Thanks, " << fname << ". Now enter you favorite number\n";
  std::cin >> favnum;
  std::string uname = fname.at(0) + lname + favnum;
  return uname;  // instead of using std::cout we return the string to the main program
  
}
```
Although the above works. It's not typically recommended to let value returning functions do much more than return values. In the above code, std::cout is being called before the function is called and inside of the function when the function is called. So there is the possibility of std::cout being called at different unwanted times. 

We'll try to split the program up into two parts. We'll try to use a void function to collect the user info and a value returning function to return the info. 

We'll do this in steps. I'll first write the void function for the input directions. And change the value returning function name and definition. Note that this program won't work right now. 

We run into a scope problem because all our variables are *only defined locally* when inside a function. 
In other words, we have no way of using fname, lname, and favnum outside the void function below **and** the value returning function has no idea what fname, lname, and favnum are.

```cpp
#include <iostream>

void getUName();
std::string returnUName(); 

int main(){
  getUName();  // ideally, this would gather our username info
  std::cout << "Thanks, " << returnUName();  // and this would create and return the uname for use in a message
}

void getUName(){
  std::string fname, lname, favnum;   // scope problem
  std::cout << "Enter your first and last name\n";
  std::cin >> fname >> lname;
  std::cout << "Thanks, " << fname << ". Now enter you favorite number\n";
  std::cin >> favnum;
}
st::string returnUName(){
  std::string uname = fname.at(0) + lname + favnum;  // scope problem
  return uname;  // instead of using std::cout we return the string to the main program
}
```

For now, we'll take care of this problem using global variables. 

```cpp
#include <iostream>

std::string fname, lname, favnum, uname;   // global scope ... we can refer to these variables throughout our program. This is generally NOT recommnended.
// We'll see how to do this better in the next section

void getUName();
std::string returnUName(); 

int main(){
  getUName();  // ideally, this would gather our username info
  std::cout << "Thanks, " << returnUName();  // and this would create and return the uname for use in a message
}

void getUName(){
  std::cout << "Enter your first and last name\n";
  std::cin >> fname >> lname;
  std::cout << "Thanks, " << fname << ". Now enter you favorite number\n";
  std::cin >> favnum;
}
st::string returnUName(){
  uname = fname.at(0) + lname + favnum;  // scope problem
  return uname;  // instead of using std::cout we return the string to the main program
}
```
