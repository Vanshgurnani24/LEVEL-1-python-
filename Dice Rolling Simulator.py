import random
x="y"
while x=="y":
    no=random.randint(1,6)
    if no==1:
        print("[-------]")
        print("[       ]")
        print("[   o   ]")
        print("[       ]")
        print("[-------]")
    if no==2:
        print("[-------]")
        print("[o      ]")
        print("[       ]")
        print("[      o]")
        print("[-------]")
    if no==3:
        print("[-------]")
        print("[o      ]")
        print("[   o   ]")
        print("[      o]")
        print("[-------]")
    if no==4:
        print("[-------]")
        print("[o     o]")
        print("[       ]")
        print("[o     o]")
        print("[-------]")
    if no==5:
        print("[-------]")
        print("[o     o]")
        print("[   o   ]")
        print("[o     o]")
        print("[-------]")
    if no==6:
        print("[-------]")
        print("[o     o]")
        print("[o     o]")
        print("[o     o]")
        print("[-------]")
    x=input("press y to roll again and n to exit")
    print("\n")  