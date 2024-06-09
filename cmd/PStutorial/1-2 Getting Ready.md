# Getting Ready

Start by updating the `get-help` cmdlet

```PowerShell
Update-Help
```

Note that you may have to run this command as an admin.

Use help in conjunction with a cmdlet and then -parameter to see more info on parameters

```PowerShell
help get-childitem  # will list info on get-childitem and it's parameters
help get-childitem -parameter directory # will explain what the parameter directory will do
```

Use get-help with -examples parameter to see eazmples of commands

```PowerShell
get-help get-childitem -examples
```

To challenge yourself everynow and then try 

```PowerShell
Get-Command | Get-Random | Get-Help -Full
```
