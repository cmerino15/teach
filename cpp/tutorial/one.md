# A basic cpp message 👋 

> [!NOTE] 
> In cpp we use two forward slashes // to denote a comment.
> I'll be commenting lines of code to explain what they do

Create a main.cpp file and copy the code below
> main.cpp
```cpp
#include <iostream>             // includes the input/output standard library. Needed for cout operator below
// sometimes i'll use comments before a line of code like this
int main(){                     // every cpp file must have a main function. the main function returns an integer (see below). We'll look at functions later.
   std::cout << "Hello World";  // std is the standard namespace where cout is defined. We'll look at namespaces later.
   return 0;                    // the int that the main function returns. 0 means that everything ran correctly
}
```
> output
```console
Hello World
```

