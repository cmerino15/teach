# Basic output, data types, and operations

In c++ we have to **declare** our variables for the data we would like to use. 
We'll be working with 3 `data types` for now. 

<details>
<summary> data types </summary>

1. int: integers 
2. string: strings 
3. double: decimal values

</details>

We can do basic math operations on ints and doubles. Some care must be taking when using the divison / and modulo % operations however. 

> [!NOTE]
> Throughout this tutorial you may need to research the details on your own. 
> The purpose of this course is to get you started quick but also to get you thinking.
> A good website for more details is [learncpp](https://www.learncpp.com/)

> Example: main.cpp

```cpp
#include <iostream>

// note: some compilers include string in iostream. I suggest always including the line that's commented-out below
// #include <string>

int main(){
   int x = 5; // the integer, x, is declared to be an int and assigned the value 5. 
              // declaring and assigment is known as initializing

   // the equals symbol is used to assign values after operations
   x = x + 2;  // from right to left, two is added to x and THEN the new value is assigned to x
   std::string name; // the string, name, is declared. 
   name = "John"; // and assigned the value John 

   // std::endl below is used to create a new line. Sometimes you'll see this as a \n in a string literal (see the other example further down)
   std::cout << "Hi, " << name << std::endl; // we can ouput different data by separating each thing with <<
   // notice the comma AND the space after hi. endl makes a new line and comes from the standard namespace
   std::cout << "Ten times the integer in x is " << 10*x << std::endl; // multiply x by 10, remember that x now holds the value 7

}
```

> output
```console
   Hi, John
   Ten times the integer in x is 70
```

> [!NOTE]
> Throughout this tutorial, I'll be introducing some basic modern Cpp concepts and building on them later. These concepts are generally not needed to continue reading the tutorial. However, seeing the concepts applied next to similar topics would be very beneficial for further learning. 

# Modern C++

C++11 introduced the **auto** keyword which allows for type deduction. Care should be taken, however, that you don't allow the auto keyword to obfuscate your code. 

For example, the following code also works. 

> Ex: main.cpp

```cpp
#include <iostream>
int main(){
   auto x = 5; // the type int is deduced
   auto y = "my message"; // careful, the type const char* is deduced (not std::string)
   // thus auto is useful, but you should understand how the types are being deduced
   std::cout << "x: " << x << "\ny: " << y << std::endl; // we can still display the values as before
}
```

> output

```console
   x: 5
   y: my message
```

> To further see the difference in the above two example try concatenating a string. i.e. Try name + "something" or y + "something" and see what works.
