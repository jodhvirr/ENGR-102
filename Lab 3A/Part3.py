# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jodhvir Singh
#               Chase Sims
#               Rayyan Dulvi
#               Vraj Desai
# Section:      550
# Assignment:   Lab 3A
# Date:         13 September 2026 


name = input("What's your name?: ")
horror_movie = input("What's your favorite horror movie?: ")
wakeup_time = input("When do you usually wake up?: ")
location = input("Name a scary location: ")
sound = input("Name a strange sound: ")
item = input("Name an object to grab: ")
friend = input("Name a friend: ")
monster = input("Name a scary creature or monster: ")
bench_press = float(input("How much can you bench press in lbs?"))
bench_press_kgs = 0.453592 * bench_press


print("\n")
print(f"One day… {name} woke up at {wakeup_time} in {location}...")
print(f"Later at night, {name} started watching a scary horror movie called {horror_movie} while bench pressing {bench_press_kgs} kgs...")
print(f"Suddenly, {name} heard {sound}.")
print(f"{name} grabbed {item} and called {friend}, \'is anyone there\', but nobody answered.")
print(f"Slowly, a shadowy {monster} stepped out from the dark!")
print(f"{name} was never heard from again..." )
print("\t The End")




