from animatronic import Animatronic
from digraph import DiGraph
from pizza import Pizzeria

adj = {
    "1A": ["1B", "5"],
    "1B": ["2A", "5"],
    "1C": [],
    "2A": ["2B", "3"],
    "2B": ["3", "-2"],
    "3": ["2A", "-2"],
    "4A": [],
    "4B": [],
    "5": ["1B", "2A"],
    "6": [],
    "7": [],
    "-1": ["death"],
    "-2": ["1B"],
    "-4": [],
} 
vals = {
    "1A": "Show Stage",
    "1B": "Dining Room",
    "1C": "Pirates Cove",
    "2A": "West Hall",
    "2B": "W. Hall Corner",
    "3": "Supply Closet",
    "4A": "East Hall",
    "4B": "E. Hall Corner",
    "5": "Backstage",
    "6": "Kitchen",
    "7": "Restrooms",
    "-1": "In Office",
    "-2": "Left Door",
    "-4": "Right Door",
}
movement_graph = DiGraph(adj, vals)

fnaf = Pizzeria(Animatronic("Bonnie", 3, movement_graph), "1A")
# results vars
results = []
three_movements_any = 0
successes = 0
# number of times bonnie won in 3 moves, or the fastest possible time
three_movements_won = 0
fastest = 0
num_trials = int(input("How many trials: "))
num_movements = 10
for i in range(num_trials):
    # reset
    fnaf.reset()
    time_to_door = -1
    movements_in_row = 0
    made_three_row = False
    # simulate movements
    for j in range(num_movements):
        if fnaf.animatronic.move():
            movements_in_row += 1
        else:
            movements_in_row = 0
        if (not made_three_row) and movements_in_row > 3:
            three_movements_any += 1
            made_three_row = True
        # check if bonnie made it to the door
        if fnaf.animatronic.current_room == "-2":
            if made_three_row:
                three_movements_won += 1
            if j == 4:
                fastest += 1
            time_to_door = j + 1
            successes += 1
            break
    results.append({"Trial": i+1, "Time to Door": time_to_door, "3 Movements in a Row": made_three_row})

# process data
print(f"Ran a total of {num_trials} trials.")
print(f"There were {successes} successes, with a probability of {successes/num_trials * 100:.4f}%.")
print(f"Of all trials, Bonnie made 3 or more movements in a row {three_movements_any} times, for a probability of {three_movements_any/num_trials * 100:.4f}%.")
print(f"Of all successes, Bonnie made 3 or more movements {three_movements_won} times. This was {three_movements_won/successes * 100:.4f}% of all successes, and {three_movements_won/num_trials * 100:.4f}% of all trials.")
print(f"Of all successes, Bonnie made it to the door as fast as possible {fastest} times. This was {fastest/successes * 100:.4f}% of all successes, and {fastest/num_trials * 100:.4f}% of all trials.")