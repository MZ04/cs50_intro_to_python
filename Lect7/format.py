import re

name = input("What's your name? ").strip()
#The values in the () are captured
#if "," in name:
#    last, first = name.split(", ")
#    name = f"{first} {last}"
if matches:=re.search(r"^(.+), ?(.+)$", name):
    #first, last=matches.groups()
    #first and last take the values captured by the parenthesis
    #name = f"{first} {last}"
    name = f"{matches.group(1)} {matches.group(2)}"
print(f"hello, {name}")