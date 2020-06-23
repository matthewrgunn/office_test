from collections import Counter 

def most_frequent(list): 
    occurence_count = Counter(list) 
    return occurence_count.most_common(1)[0][0] 

def determineChar(answer):
    if answer == "1": 
        return "Michael"
    elif answer == "2": 
        return "Pam" 
    elif answer == "3": 
        return "Dwight" 
    elif answer == "4": 
        return "Jim"
    elif answer == "5": 
        return "Kelly" 
    else: 
        return "Toby"

def returnChar(char): 
    if char == "Michael":
        return "Desperate to be loved, you are undoubtedly wilting under the forced quarantine, but with any luck, your office mates have taken at least a little pity on you."
    elif char == "Pam": 
        return "Resiliant and empathetic, you are undoubtedly flourishing in the forced quarantine even as you fret about the chaos in the world. Thank you for lending your formidable artistic talents to the Black Lives Matter movement."
    elif char == "Dwight":
        return "You are seizing the moment to rise to greatness. Again."
    elif char == "Jim":
        return "Your ironic sensibilities don't hide your sensitive core. Despite the many pranks you've played this quarantine, we see you standing up for the little person."
    elif char == "Kelly":
        return "Deep down, we all know who this moment is really about--you. Nothing we can say will change your mind, so we're just going to agree."
    else: 
        return "Why do you choose to be the way that you are?"





# 1 - Michael 
# 2 - Pam 
# 3 - Dwight
# 4 - Jim
# 5 - Kelly