# Input and Output

We use the cin operator in a similar way that we use the cout operator
Both are defined in the iostream library and std namespace
One main difference is that instead of using the *put to* operator << we use the *get from* operator >>

> Ex: main.cpp

```cpp
  #include <iostream>
  int main(){
    string name = "adsfasdfasdf"; // initiliazing a string with a random name

    std::cout << "Your name is not " << name << "!" << std::endl;

    std::cout << "Please enter your name: "; // We should always prompt the user before using cin, so that the user knows what to do

    std::cin >> name ;

    std::cout << "Thanks, " << name << std::endl;

    return 0;
  }
```

> output

` Your name is not adsfasdfasdf!
  Please enter you name: 
  <input>
  Thanks, <input> `

  
