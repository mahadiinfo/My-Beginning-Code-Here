word = "mahadi"
chances = 8
userstore = []
done = False

print("Assalamu alaikum vaijan! Hobe naki akta game?")
name = input("Raji thakle bolen [y / n] ami game ar rules bujie dissi okk: ").lower()

if name == "y":
    print("Game rule sohoj: ami mone mone akti word vabbo.")
    print("Apni jodi seta bujhte paren tahole gift dibo.")
    print("Apnar chance thakbe 8 ta. Na parle... mair khaite hobe 😆")

    while not done and chances > 0:
        for letter in word:
            if letter in userstore:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()

        userinput = input(f"Akhon bolen ami ki vabsi? Apnar chance ase {chances} bar: ").lower()

        if userinput in userstore:
            print("Apni agei ei letter bolsen!")
        elif userinput in word:
            print (f"oh ho boro vsi kemne parlen ? " \
            f"ami to {userinput} bolsilam")
            continue

        userstore.append(userinput)

        if userinput not in word:
            chances -= 1
            print("Ha ha ha... apni to parlen na. -1 chance gelo.")
            if chances == 1:
                print("Warning! Shesh chance!!")
            elif chances == 0:
                print("Apnar sob chance sesh. 😵 <@> GAME OVER <@>")
                break

        # Check if all letters matched
        done = True
        for letter in word:
            if letter not in userstore:
                done = False
                break

    if done:
        print(f"\n🎉 Oh hoo! Boro vai you are the winner! Ami vabsi '{word}'")
    else:
        print("Boro vai parlen na... abar mair khawar jonno toiri hoiya naw. <@> GAME OVER <@>")

else:
    print("Tui game e asli na. Bujhlam tui valo manush. 😅 <@> GAME OVER <@>")
