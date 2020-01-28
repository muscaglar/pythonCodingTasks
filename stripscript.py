text = "#indiefilm #film #filmmaking #filmmaker #director #actor #shortfilm #cinematography #cinema #movie #movies #producer #filmmakers #hollywood #filmproduction #cinematographer #indie #independentfilm #filmfestival #indiefilmmaking #actorslife #production #filmdirector #videoproduction #supportindiefilm #setlife #acting #photography #videography #tv #shortfilm #filmmakerslife #filmlife #canon #art #setlife #photographer #writers #featurefilm #supportindiefilm #actress #comedy #horror #like #producers #videomaking #filmschool #directorofphotography #independentfilm #artist #a #sonya #videomaker #nollywood #filmphotography #d #directing #follow #filmmakers #filmmaking #film #filmmaker #cinematography #actor #director #cinematographer #cinema #videoproduction #filmproduction #hollywood #indiefilm #producer #actors #movie #movies #production #photography #videography #directors #videographer #video #onset #films #actorslife #filming #bhfyp"

text2 = ""

for char in text:
    if char == '#':
        text2 += "'"
    elif char == " ":
        text2 += "', "
    else:
        text2 += char

print text2
