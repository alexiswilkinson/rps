import random
# Check that users have entered a valid
# option based on a list

def string_checker(question, valid_ans=('yes', 'no')):

    # Displays instructions

    def instructions():
        ...
    # checks for an integer more than 0 (allows <enter>)
    def int_check(question):
        while True:
            error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

         # checks that the number is more than \ equal to 13
        if response < 1:
            print(error)
        else:
            return response

        except ValueError
        print(error)

# compares user / computer choice and returns
# result (win / lose / tie)
def rps_compare(user, comp):


# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("💎📄✂️ Rock / Paper / Scissors Game 💎📄✂️")
print()


# ask the user if they want to see the instructions and display
# them if requested
want_instructions = yes_no("Do you want to read the instructions?")

# Checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds \ infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:


    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_headings = f"\n xxx Round {rounds_played + 1} (Infinite Mode) xxx"
    else:
        rounds_headings = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds}💿💿💿"

    print(rounds_heading)

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)


    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    # print ("you chose", user_choice)


    # if user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)
print(f"{user_choice} vs {comp_choice}, {result}")

rounds_played += 1


 # if users are in infinite mode, increase number of rounds!
if mode == "infinite":
        num_rounds += 1



# Game loop end here


# Game History / Statistics area