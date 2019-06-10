from playsound import playsound
import random


wow = {"Q": ["Vad är Annika Anka?",
             "Vilket klubblag har 'Zlatan' gjort flest A-lagsmål för?",
             "Vilket djur går inte i dvala?",
             "Vem tjänade mest år 2018 (enligt DN)",
             "Vilket av dessa påstånden stämmer",
             "Vilket fotbollslag kallas för 'Änglarna'",
             "Vilken fransk stad är värdar för världens mest prestigefulla filmfestival?"],

            "AC": ["En figur i Bamses äventyr",
                   "Paris Saint-Germain",
                   "Ripa",
                   "Sebastian Knutsson",
                   "Svenskar äter mest godis per kapita.",
                   "IFK Göteborg",
                   "Cannes"], 
            
            "FAQ1": ["Realityshowstjärna och exmaka till Paul Anka", 
                     "Ajax",
                     "Fladdermusen",
                     "Stefan Löfven",
                     "Sverige har den lyckligaste befolkningen.",
                     "GIF Sundsvall",
                     "Paris"],

            "FAQ2": ["En maträtt",
                     "Malmö FF",
                     "Huggormen",
                     "Agneta Birgitta Englund",
                     "Danskar är bäst i skandinavien på Engelska.",
                     "AFC Eskilstuna",
                     "Nice"]
}
NQ = int(input("Hur många frågor vill du ha? \n 3,6,9 eller 12? "))
QN = 1
z=len(wow["Q"])
qx = list(range(0, z))
rättasvar = 0
while QN <= NQ:
    ett = []
    kryss = []
    två = []
    v=qx[0]
    random.shuffle(qx)
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


    print("Fråga " + str(QN)+ ": " + wow["Q"][v])
    print("1. " +ett[0])
    print("X. " + kryss[0])
    print("2. " + två[0])
    svar = str(input("1, X eller 2? "))
    del wow["Q"][v]
    if str(svar) not in ("1", "x", "X", "2"):
        svar = str(input("felaktig input, vänligen välj '1', 'x', 'X' eller '2'."))
        if str
    
    elif str(svar) == str(rätt):
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
print("Du fick " + str(rättasvar) + "/" + str(NQ) + " rätt" )


