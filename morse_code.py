import winsound
import time
morse={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.",
"G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..",
"M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.",
"S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-",
"Y":"-.--","Z":"--.."}
text=input("ENTER TEXT : ").upper()
for char in text:
    if char==" ":
        time.sleep(0.6)
        continue
    for symbol in morse[char]:
        winsound.Beep(800,150 if symbol=="."else 450)
        time.sleep(0.1)
    time.sleep(0.3)
