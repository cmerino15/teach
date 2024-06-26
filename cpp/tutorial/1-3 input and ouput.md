# Input and Output

We use the cin function in a similar way that we use the cout function.
Both are defined in the iostream library and std namespace.
One main difference is that instead of using the *put to* operator << we use the *get from* operator >>

> Ex: main.cpp

```cpp
  #include <iostream>

  // note: some compilers include string in iostream. I suggest always including the line that's commented-out below
  // #include <string>

  int main(){
    std::string name = "adsfasdfasdf"; // initiliazing a string with a random name

    std::cout << "Your name is not " << name << "!" << std::endl;

    std::cout << "Please enter your name: "; // We should always prompt the user before using cin, so that the user knows what to do

    std::cin >> name ;

    std::cout << "Thanks, " << name << std::endl;

    return 0;
  }
```

> [!NOTE]
> Througout this course I'll use \<input\>, \<your-input\>, or {input}, etc. in place of something you should be typing into the console

> output

```console
  Your name is not adsfasdfasdf!
  Please enter your name: <your-input>
  Thanks, <your-input>
```

  
