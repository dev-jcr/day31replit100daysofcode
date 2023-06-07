# Music interface with change of color and alignment

import os, time

def colPrint(color, word):
  if color=="red":
    print(f"\033[0;31m", word, sep="", end="")
  elif color=="blue":
    print(f"\033[0;34m", word, sep="", end="")
  elif color=="white":
    print(f"\033[1;37m", word, sep="", end="")
  elif color=="yellow":
    print(f"\033[1;33m", word, sep="", end="")
  elif word==" ":
    print(f"\033[0;31m", f"{word: ^10}", sep="", end="")

red = "\033[0;31m"
blue = "\033[0;34m"
white = "\033[1;37m"
yellow = "\033[1;33m"
green = "\033[1;32m"
purple = "\033[1;35m"

print("Interface 1")

colPrint("none", " ")
colPrint("red", "=")
colPrint("white", "=")
colPrint("blue", "=")
colPrint("yellow", " Music App ")
colPrint("blue", "=")
colPrint("white", "=")
colPrint("red", "=")
print()
print()
colPrint("yellow", "Choose a song:")
print("""
1. Robi Draco Rosa - Penelope
2. Radiohead - Creep
3. The Weeknd - Save Your Tears

""")
while True:
  song = input("Write the number of the song...\n")
  int(song)
  playLogo = "🔥▶️"
  if song == "1":
    title = "Penelope"
    artist = "Robi Draco Rosa"
    print(f"""{white}
    {playLogo} {title}
      {yellow}  {artist}""")
    break
  elif song==2:
    title = "Creep"
    artist = "Radiohead"
    print(f"""{white}
    {playLogo} {title}
      {yellow}  {artist}""")
    break
  elif song==3:
    title = "Save Your Tears"
    artist = "The Weeknd"
    print(f"""{white}
    {playLogo} {title}
      {yellow}  {artist}""")
    break
  else:
    print("Not available (yet!)")
    continue
  
print()
print()

print(f"""
  {white}PREV
        {green}NEXT
              {purple}PAUSE
""")

time.sleep(3)

print("Interface 2")
print()
i2title = "WELCOME TO"
i2subtitle = "--     ARMBOOK     --"
text = "Definitively not a rip off of"
text3 = "a certain other social"
text4 = "networking site."
text2 = "Honest."
user = "Username:"
password = "Password:"
print(f"""
{white:^40}{i2title}
{blue:^35}{i2subtitle}

{yellow:>30}{text:>30}
{yellow:>30}{text3:>30}
{yellow:>30}{text4:>30}

{red:^42}{text2}

{white:^42}{user}
{white:^42}{password}
""")



# Course solution

# def colorChange(color):
#   if color=="red":
#     return ("\033[31m")
#   elif color=="white":
#     return ("\033[0m")
#   elif color=="blue":
#     return ("\033[34m")
#   elif color=="yellow":
#     return ("\033[33m")
#   elif color == "green":
#     return ("\033[32m")
#   elif color == "purple":
#     return ("\033[35m")

# title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}= {colorChange('yellow')}Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}="

# print(f"        {title:^35}")
# print(f"🔥▶️\t{colorChange('white')}Radio Gaga")
# print(f"\t{colorChange('yellow')}Queen")

# prev = "prev"
# next = "next"
# pause = "pause"

# print(f"{colorChange('white')}{prev:<35}")
# print(f"{colorChange('green')}{next:^35}")
# print(f"{colorChange('purple')}{pause:>35}")


# print()
# print()
# text = "WELCOME TO"
# print(f"{colorChange('white')}{text:^35}")
# text = "--  ARMBOOK  --"
# print(f"{colorChange('blue')}{text:^35}")
# text = "Definitely not a rip off"
# print(f"{colorChange('yellow')}{text:>35}")
# text = "a certain other social"
# print(f"{colorChange('yellow')}{text:>35}")
# text = "networking site"
# print(f"{colorChange('yellow')}{text:>35}")
# text = "Honest."
# print(f"{colorChange('red')}{text:^35}")
# text = "Username: "
# username = input(f"{colorChange('white')}{text:^35}")
# text = "Password: "
# username = input(f"{colorChange('white')}{text:^35}")