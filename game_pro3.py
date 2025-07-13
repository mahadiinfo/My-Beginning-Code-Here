import random

print(" son ami 1-10 porjonto akta namber choiche korbo ar tui jodi seta koite paros aile ami tore akta puruskar dibo raji thakle enter a tip de")

Randomnamber = random.randrange(1,10)
userinput = int(input(" ko dehi ki kobi tui kto namber chas? : "))

if userinput > Randomnamber : 

    print(f"kire beda koi choilla geso ami to koisi {Randomnamber} namber ha ha ha.... abar try kor")

elif Randomnamber > userinput :

     print( f" ha ha ha.... koi choilla geso ato kom na.." 
     f" ami to koisi {Randomnamber} namber ha ha ha..... abar try kor")


else: 
     print(f"kire beda kemne koili amito koiselam {Randomnamber} nambari...." 
     " jak tui ahon ki chas ko amare likhe de")
     userinput2 = input(" ki chaw ko likhe de : ")
     print( " ore babare ato asa ha ha ha ...... jah ditam na.....")




     # project successsss alhamdulillah