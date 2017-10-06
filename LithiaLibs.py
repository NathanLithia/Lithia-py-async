import os

#CLEAR CONSOLE
# Usage: LithiaLibs.clear()
clear = lambda: os.system('cls')

#LEGACY COLORS
# Usage: LithiaLibs.prRed("This text is red.")
def prRed(prt): print("\033[91m{}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m{}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m{}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m{}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m{}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m{}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m{}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m{}\033[00m" .format(prt))

#REVISED COLORS
# Usage: print(LithiaLibs.liCyan + "My Text" + LithiaLibs.liEND)
liRed = "\033[91m"
liGreen = "\033[92m"
liYellow = "\033[93m"
liLightPurple = "\033[94m"
liPurple = "\033[95m"
liCyan = "\033[96m"
liLightGrey = "\033[97m"
liBlack = "\033[98m"
liEND = "\033[00m"
