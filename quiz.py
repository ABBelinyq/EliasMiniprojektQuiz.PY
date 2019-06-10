from playsound import playsound
import random
import requests 

def syntaxcheck(svar):

    if str(svar) not in ("1", "x", "X", "2"):
        svar = str(input("Wrong input, Please choose '1', 'x', 'X' or '2'."))
        syntaxcheck(svar)
    
def addquestions(NQ):
    lenq = len(wow["Q"])
    lens = lenq -1
    if NQ > lenq:
    
        addquestion = NQ - lenq
        url = "https://opentdb.com/api.php?amount=1&difficulty=medium&type=multiple"
        getter = requests.get(url)
        result = getter.json()
        print
        for addquestion in result['results']:
            wow["Q"].append(addquestion["question"])
            wow["AC"].append(addquestion["correct_answer"])
            wow["FAQ1"].append(addquestion["incorrect_answers"][0])
            wow["FAQ2"].append(addquestion["incorrect_answers"][1])
        addquestions(NQ)
            
            


wow = {"Q": ["Who is Annika Anka?",
             "Which football club has Zlatan Ibrahimovic scored most goals for",
             "Which animal does NOT go into hibernation",
             "Which swede earned the most money in 2018 (according to DN)",
             "Which is correct?",
             "Which football team is nicknamed 'Änglarna'",
             "In which french city is the host for the biggest movie festival in the world?"],

            "AC": ["A character in the adventures of Bamse",
                   "Paris Saint-Germain",
                   "The Grouse",
                   "Sebastian Knutsson",
                   "Swedes eat the most candy per capita.",
                   "IFK Göteborg",
                   "Cannes"], 
            
            "FAQ1": ["Realityshowstar and exwife of Paul Anka", 
                     "Ajax",
                     "The bat",
                     "Stefan Löfven",
                     "Sweden has the happiest inhabitants.",
                     "GIF Sundsvall",
                     "Paris"],

            "FAQ2": ["A dish",
                     "Malmö FF",
                     "The viper",
                     "Agneta Birgitta Englund",
                     "Danes are best in scandinavia in english.",
                     "AFC Eskilstuna",
                     "Nice"]
}
NQ = int(input("How many questions do you want? \n 3,6,9 eller 12? "))
addquestions(NQ)
QN = 1



z=len(wow["Q"])
rättasvar = 0
while QN <= NQ:
    qx = list(range(0, z))
    random.shuffle(qx)
    v=qx[0]
    ett = []
    kryss = []
    två = []
    
    val =[0, 1, 2]
    random.shuffle(val)
    rätt = 0
    if val[0] == 0:
        ett.append(wow["AC"][v])
        rätt = "1"
    elif val[0] == 1:
        kryss.append(wow["AC"][v])
        rätt = "X"
    else:
        två.append(wow["AC"][v])
        rätt = "2"
    del val[0]
    del wow["AC"][v]

    random.shuffle(val)
   
    if val[0] == 0:
        ett.append(wow["FAQ1"][v])
    elif val[0] == 1:
        kryss.append(wow["FAQ1"][v])
    else:
        två.append(wow["FAQ1"][v])
    del wow["FAQ1"][v]
    del val[0]
    
    if val[0] == 0:
        ett.append(wow["FAQ2"][v])
    elif val[0] == 1:
        kryss.append(wow["FAQ2"][v])
    else:
        
        två.append(wow["FAQ2"][v])
    del wow["FAQ2"][v]
    del qx[0]


    print("Question " + str(QN)+ ": " + wow["Q"][v])
    print("1. " + ett[0])
    print("X. " + kryss[0])
    print("2. " + två[0])
    svar = str(input("1, X or 2?"))
    syntaxcheck(svar)
    del wow["Q"][v]
            
    if str(svar) == str(rätt):
        rättasvar+=1 
        playsound('correct_ping.mp3')  
        playsound('correct_voice.mp3')    
    elif str(svar) == "x" and str(rätt) == "X":
        rättasvar+=1
        playsound('correct_ping.mp3')
        playsound('correct_voice.mp3')    
    else:
        playsound('wrong_ping.wav') 
        playsound('wrong_voice.mp3')
    QN+=1
    z-=1
    
    # print(v)
    # print(z)
print("You got " + str(rättasvar) + "/" + str(NQ) + " correct answers" )


