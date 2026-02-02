# Basic commands similar to cmd

Instead of `dir` we can `Get-ChildItem` to see the files in a directory
This is a bit more to type, but it comes with a lot more functionality
For example, to see the list of items or 'children' in a *all* subdirectories we can use the -recurse option.
Likewise, we can use Get-Help

```Powershell
Get-ChildItem -recurse #list files in dir and subdirectories
```

Or altenatively use the -depth parameter to specify the number of subdirectories

```PowerShell
Get-ChildItem -depth 1 # will list as far as 1 subdirectory
```

The `tree` command works just as it does in CMD

The `Get-verb` command lists the verb commands with their types

The `Get-command` command lists all commands on your system

The 'get-member' command can be used to pipe other commands into it and see their member functions

```PowerShell
get-childitem | get-member
```

> [!NOTE]
> The commandlets are not case sensitive

To find processes that work with -childitem use get-command with the * operator

```PowerShell
get-command *-childitem
```

To filter on verb use the `-verb` parameter with get-command

```PowerShell
get-command -verb get
```

To filter on noun use the `-noun` parameter with the get-command

```PowerhShell
get-command -noun childitem
```

