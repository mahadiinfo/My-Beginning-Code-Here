import random
 
ludugame = True

print(" a beda ludu khelbi ludu ko taile khela howk ak mach")
while ludugame:
   
    play = input(" ko taile aeihane [ y / n] :").lower()
    if play == "y":
        roll = random.randint(1, 6)
        if roll == 6:
               print(f"🎯 তোর ছক্কায় পরছে: {roll} — ছক্কা! আবার খেলবি?")
        else:
               print(f"🎲 তোর ছক্কায় পরছে: {roll}")

        continue
   
   
    else:
        print ("<@> GAME OVER <@>")
        break

# alhamdulilla project compilit 