# Discord-Rich-Presence-Dynamic
Custom discord rich presence "dynamic" that will change on a specified interval of time

# Dependancies

```
pip install pypresence
```

- Tested using version ``4.3.0``

# json

Open [rpc.json](rpc.json) to configure

| Key | Value | Description |
|---|---|---|
| client ID | integer | Your application ID |
| interval update | integer | Time (In seconds) at wich the RPC will be updated |
| buttons | array<array> | Button labels (See bellow) |

# button

| Index | Value | Description |
|---|---|---|
| 0 | string | String to display within the button |
| 1 | string | Link to open when click the button |
| 2 | string | Imagen name to use for this button (Add to your Application) |
| 3 | string | String to display above the button |

# Running

Using [rpc.bat](rpc.bat) will execute it on the background (windows only. accepting pull requests)
