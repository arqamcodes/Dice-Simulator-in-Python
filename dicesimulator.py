import random
import time

x = "r"
print("\n")
print(f"'Welcome to Dice Simulator'\n")
print("Instructions: The Dice simulator generates a number between 1 and 6 in a single dice.\n")
time.sleep(1)

while x == "r":
    
    x= input(f"Press 'r' to roll again and 'e' to exit:")


    # Generates a random number
    # between 1 and 6 (including
    # both 1 and 6
    no = random.randint(1,6)

    if x == "r":
        print()
    elif x == "e":
        print("Thankyou for playing!")
        break
    else:
        print("Invalid input")
        break


    

    if no == 1:
        print("[--------]")
        print("[        ]")
        print("[    0   ]")
        print("[        ]")
        print("[--------]")


    if no == 2:
        print("[--------]")
        print("[   0    ]")
        print("[        ]")
        print("[     0  ]")
        print("[--------]")

    if no == 3:
        print("[--------]")
        print("[        ]")
        print("[ 0 0 0  ]")
        print("[        ]")
        print("[--------]")
    if no == 4:
        print("[--------]")
        print("[0      0]")
        print("[        ]")
        print("[0      0]")
        print("[--------]")
    if no == 5:
        print("[--------]")
        print("[0      0]")
        print("[    0   ]")
        print("[0      0]")
        print("[--------]")
    if no == 6:
        print("[--------]")
        print("[0  0  0 ]")
        print("[        ]")
        print("[0  0  0 ]")
        print("[--------]")
    

    
    print("\n")