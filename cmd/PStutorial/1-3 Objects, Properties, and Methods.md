
We can get basic info on a service

```PowerShell
get-service w32time # will display some properties
````

To list all members, functions, and properties

```PowerShell
get-service w32time | get-member
```

> [!NOTE]
> get-member also returns the object type. In this case, 'w32time' has type servicecontroller

So, get-service is a command that produces a type of *servicecontroller* when the parameter is the w32time object.
Thus, we can see what other commands will accept 'servicecontroller' **types** as a parameter

```PowerShell
get-command -parametertype servicecontroller
```


Now we can select other properties with additional info.

```PowerShell
get-service w32time | select-object -property *
```

To display methods

```PowerShell
get-service | get-member -membertype method
```

Try, to see the powershell process with members   

```PowerShell
get-process powershell | get-member
```

