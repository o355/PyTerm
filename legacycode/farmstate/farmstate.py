#This is legacy code.
#This program is removed from PyTerm, but still sticks around.
#It won't receive updates, but will stick around.
#License is the same as the PyTerm license.

import sys

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)

print("Launching program - Farmstate - v1.0")
print("")
print_slow("STATEFARM")
print_slow("\nTHE BEST OF INSURANCE ON THE PLANET!")
print_slow("\nYOU CAN SAVE NOW 30% IN JUST 10 MINUTES AT STATEFARM!")
print_slow("\nUNLIKE THOSE OTHER GUYS WHO ONLY SAVE 15% IN 15 MINUTES.")
print_slow("\nSTATEFARM HAS BEEN TRUSTED BY THE INDUSTRY FOR ABOUT 70 YEARS")
print_slow("\nSTATEFARM HAS OVER ONE MILLION STATISFIED CUSTOMERS!")
print_slow("\nSO, IS IT TIME TO SWITCH TO STATEFARM? YOU BET IT IS!")
print_slow("\nWE'LL EVEN PIE STATE FARM IF YOU SWITCH TODAY.")
print_slow("\nWHICH STATE FARM YOU ASK?")
print_slow("\nTHE ONE AT VASSAR. YEA. YOU KNOW THAT STATEFARM")
print_slow("\nSWITCHING TODAY IS EASY.")
print_slow("\nSWITCH TODAY!")
print_slow("\nIN FACT, IF YOU SWITCH TO STATEFARM TODAY, WE'LL GIVE YOU A REALLY, REALLY GOOD COUPON!!!!!!!!!!!")
print_slow("\nGO GO GO GO GO SWITCH")
print_slow("This poem has been approved by the man himself, Statefarm, or Farmstate.")
print_slow("Thanks.")
sys.exit()
