def print_welcome_message():
    print("     _____      _            _       _")
    print("    / ____|    | |          | |     | |")
    print("   | |     __ _| | ___ _   _| | __ _| |_ ___  _ __")
    print("   | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|")
    print("   | |___| (_| | | (__| |_| | | (_| | || (_) | |")
    print("    \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|")
    print("       by Carlos Escalante")

    print(
        bgcolors.WARNING + "Welcome to the super awesome calculator made with love, in Python programming language, by Carlos Escalante" + bgcolors.ENDC)

def print_error(msg):
    print(bgcolors.FAIL + msg + " " + bgcolors.ENDC)

def print_success(msg):
    print(bgcolors.OKGREEN + msg + " " + bgcolors.ENDC)

class bgcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'