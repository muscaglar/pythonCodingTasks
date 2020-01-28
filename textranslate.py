#Short program to convert the text characters into a pure number following a set of translation rules
#Translation rules are given in the dictionaries defined below

string_conv = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

convert = ""
prev = ""

lower = {'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j':'9', 'k':'10', 'l':'11', 'm':'12', 'n':'13', 'o':'14', 'p':'15', 'q':'16', 'r':'17', 's':'18', 't':'19', 'u':'20', 'v':'21', 'w':'22', 'x':'23', 'y':'24', 'z':'25'}

upper = {'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'F':'6', 'G':'7', 'H':'8', 'I':'9', 'J':'10', 'K':'11', 'L':'12', 'M':\
'13', 'N':'14', 'O':'15', 'P':'16', 'Q':'17', 'R':'18', 'S':'19', 'T':'20', 'U':'21', 'V':'22', 'W':'23', 'X':'24', 'Y':'25', 'Z':'26'}

space = {' ':'+'}

operations = {',':'-', '.':'*'}

for letter in string_conv:
    if letter in lower and letter != 'a':
        convert += lower[letter]
    if letter in lower and letter == 'a':
        if prev == ' ':
            pass
        else:
            convert += lower[letter]
    if letter in upper:
        convert += upper[letter]
    if letter in space and prev in operations:
        convert += operations[prev]
    if letter in space and prev not in operations:
        convert += space[letter]

    prev = letter

print(eval(convert))
