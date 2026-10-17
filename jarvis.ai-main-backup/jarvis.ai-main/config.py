import platform

is_windows = platform.system() == "Windows"
is_mac = platform.system() == "Darwin"
is_linux = platform.system() == "Linux"

def get_os():
    if is_windows:
        return "windows"
    if is_mac:
        return "mac"
    if is_linux:
        return "linux"
    return platform.system().lower()
