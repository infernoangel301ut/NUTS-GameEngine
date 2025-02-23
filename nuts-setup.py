import os
import sys

print("Welcome to the NUTS Game Engine setup.\nEverything required to work with NUTS will be installed here.\n")
instruction_check = input("Have you checked the instructions? (y/n) ").lower()

if instruction_check == "n":
    print("Go read them lol (nuts-setup-instructions.txt)")
    sys.exit()
elif instruction_check == "y":
    if not (os.path.exists("nuts.py") and os.path.exists("nuts-setup-config.json")):
        print("liar liar pants on fire")
        sys.exit()
    print("Proceeding...")
else:
    print("Unknown answer.")
    sys.exit()

print("Phase 1: Installing required modules.")
needs_setuptools = False
needs_raylib = False
needs_pyinstaller = False

print("Checking for the setuptools module...")
try:
    import setuptools
    print("Setuptools found! No further action required for it.")
except:
    needs_setuptools = True
    print("Setuptools was not found. Requires installation.")

print("Checking for the Raylib module...")
try:
    import pyray
    print("Raylib found! No further action required for it.")
except:
    needs_raylib = True
    print("Raylib was not found. Requires installation.")

print("Checking for the PyInstaller module...")
try:
    import PyInstaller
    print("PyInstaller found! No further action required for it.")
except:
    needs_pyinstaller = True
    print("PyInstaller was not found. Requires installation.")

if needs_setuptools:
    print("Installing setuptools...")
    os.system(f"{sys.executable} -m pip install setuptools")
if needs_raylib:
    print("Installing Raylib...")
    os.system(f"{sys.executable} -m pip install raylib")
if needs_pyinstaller:
    print("Installing PyInstaller...")
    os.system(f"{sys.executable} -m pip install PyInstaller")

print("Phase 1 finished!\nPhase 2: Creating folder on disk.")

os.mkdir("C:/NUTSGameEngine")

print("NUTS Game Engine setup finished.")