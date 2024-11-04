import os
import sys
import shutil
import winreg

# Registry keys for Steam installation path
steam_registry_keys = [
    r"SOFTWARE\WOW6432Node\Valve\Steam",  # Windows 64-bit
    r"SOFTWARE\Valve\Steam"               # Windows 32-bit
]
steam_registry_value = "InstallPath"

def get_steam_install_path():
    for key_path in steam_registry_keys:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
                install_path, _ = winreg.QueryValueEx(key, steam_registry_value)
                return install_path
        except FileNotFoundError:
            continue
    return None

search_pattern = bytes.fromhex("00 64 69 73 61 62 6C 65 6F 76 65 72 6C 61 79 00")
replacement_pattern = bytes.fromhex("00 64 69 73 61 62 6C 65 30 76 65 72 6C 61 79 00")

def hex_edit_file(file_path, search_pattern, replacement_pattern):
    backup_path = file_path + ".bak"
    try:
        shutil.copy2(file_path, backup_path)
        print(f"Backup created: {backup_path}")
    except (PermissionError, IOError) as e:
        print(f"Error creating backup: {e}")
        return False

    with open(file_path, 'rb') as file:
        data = file.read()

    offset = data.find(search_pattern)
    if offset == -1:
        return False

    modified_data = data[:offset] + replacement_pattern + data[offset + len(search_pattern):]

    try:
        with open(file_path, 'wb') as file:
            file.write(modified_data)
    except (PermissionError, IOError) as e:
        print(f"Error writing to file: {e}")
        return False

    return True

if __name__ == "__main__":
    install_path = get_steam_install_path()
    if install_path:
        print(f"Steam installation path found: {install_path}")
        file_path = os.path.join(install_path, "appcache", "appinfo.vdf")
        if os.path.exists(file_path):
            if hex_edit_file(file_path, search_pattern, replacement_pattern):
                print("\nDisableOverlay flag successfully patched. If Steam is running, you must restart it to apply changes.")
            else:
                print("\nDisableOverlay flag not found, it may already be patched.")
        else:
            print(f"appinfo.vdf not found.")
    else:
        print("Could not retrieve Steam installation path.")
    input("\nPress Enter to exit.")