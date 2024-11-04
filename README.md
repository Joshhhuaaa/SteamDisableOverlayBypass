# <img src="icon.ico" width="32"> SteamDisableOverlayBypass
SteamDisableOverlayBypass is a simple command-line script to bypass the `DisableOverlay` flag set by certain Steam AppIDs.

Some games have their Steam Overlay disabled regardless of user settings because the developers thought it might lead to conflicts. However, many games with this flag can have their overlay restored without issues.

## Usage
- Run the executable: `SteamDisableOverlayBypass.exe`
- If Steam is running when the script is executed, restart Steam to apply the changes.

> [!NOTE]
> The executable release may be falsely flagged by antiviruses. If concerned, you can manually run the `SteamDisableOverlayBypass.py` file with Python.

## Restore Changes
To restore Steam to its default settings, go to your Steam installation folder and delete the `appinfo.vdf` file in the appcache folder. After deleting it, restarting Steam will generate a new `appinfo.vdf` file.

## Games with `DisabledOverlay` flag
- Tom Clancy's Splinter Cell: Chaos Theory
- Tom Clancy's Rainbow Six: Vegas
- Thief: Deadly Shadows
- Tomb Raider: Legend
- Tomb Raider: Underworld
- Prince of Persia: The Sands of Time
- Prince of Persia: Warrior Within
- Prince of Persia: The Two Thrones
- Prince of Persia (2008)
- Fallout 
- Fallout 2
- Silent Hunter III
- Silent Hunter: Wolves of the Pacific
- Silent Hunter: Wolves of the Pacific U-Boat Missions

For a full list of AppIDs with `DisableOverlay` flag, you can check SteamDB [here](https://steamdb.info/search/?a=app_keynames&type=-1&keyname=91&operator=3&keyvalue=1).

> [!NOTE]
> The Steam Overlay requires the game to be using DirectX 8 or higher. For older games running on DirectX 7, the Steam Overlay will not work. As a workaround, you can use a wrapper like dgVoodoo2.
