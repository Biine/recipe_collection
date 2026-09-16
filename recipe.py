import os, pickle, sys


def clear_console():
    if "idlelib" in sys.modules:
        print("\n" * 30) #If using pythons IDLE it will print 30 new lines instead of clearing the terminal.
    else:   
        os.system("cls" if os.name == "nt" else "clear") #This only works if you're running the program in termnial

    
   



def return_menu():
    input("\nPress Enter to return to the main menu...")
    


class Recipe:
    def __init__(self, name, category, ingredients, instructions=""):
    

        self.name = name # Expected to be a string. Recipe title.
        self.category = category #This is a list of strings
        self.ingredients = ingredients #This is a list of strings
        self.instructions = instructions #This is a string. It is optional to add, will otherwise return an empty string.

    def print_recipe(self):
        print("Name:", self.name)

        category_string = ", ".join(self.category)
        print("Category:", category_string)
        
       
        ingredients_string = ", ".join(self.ingredients)
        print("Ingredients:", ingredients_string)

        if self.instructions:
            print("Instructions:", self.instructions)

        print("_ " * 25)
        print("\n")

    
                

# Takes users input wuth name, turns into lists and save the recipe.
def add_recipe(recipe_list):
    clear_console()
    print("    Add New Recipe    ")
    name = input("Enter recipe name: ") 
    
    if name == "":
        print("Error: The recipe must have a name.")
        return_menu()
        return
    #Turning the string input into a nice list without any whitespaces
    category = input("Enter category (e.g., Dinner, Dessert): ")
    category = [
            item.strip() for item in category.split(",") if item.strip()
        ]

    
    ingredients = input("Enter ingredients (separated by comma): ")
    ingredients = [
        item.strip() for item in ingredients.split(",") if item.strip()
    ]

    # Adds a string with instructions. Optional to add. Will otherwise return an empty string.
    instructions = input("Enter instructions (optional): ")

    new_recipe = Recipe(name, category, ingredients, instructions)
    recipe_list.append(new_recipe)
    print(f"The recipe '{name}' has been saved!")

    return_menu()

 
# Shows all the recipes available
def show_recipes(recipe_list):
    clear_console()
    if len(recipe_list) == 0:
        print("The recipe collection is empty.")
        return_menu()
        return

    print("    All Saved Recipes    \n")
    for recipe in recipe_list:
        recipe.print_recipe()

    return_menu()

# Searches the recipe list (catergory, name, ingriendents) based on the users input and prints the matching recipes. 
def search_recipe(recipe_list):
    clear_console()
    if len(recipe_list) == 0:
        print("The recipe collection is empty.")
        return_menu()
        return

    search_word = input("\nEnter search word (name or category): ")
    
    found = []
    for recipe in recipe_list:
        if search_word in recipe.name or search_word in recipe.category or search_word in recipe.ingredients:
            found.append(recipe)
        
    if len(found) > 0:
        print(f"\nFound {len(found)} matching recipes:\n\n")
        for recipe in found:
            recipe.print_recipe()
    else:
        print("\nNo recipes matched your search.")

    return_menu()

# Searches the recipe list after users input and shows numbered matches and then waits for users input to see what recipe to delete 
def remove_recipe(recipe_list):
    clear_console()
    if len(recipe_list) == 0:
        print("\nThe recipe collection is empty.")
        return_menu()
        return
        
    
    search_word = input("\nEnter search word (name, category, ingredient) to delete: ")
        
    found = []
    for recipe in recipe_list:
        if search_word in recipe.name or search_word in recipe.category:
            found.append(recipe)
        
    if len(found) > 0:
        print(f"Found {len(found)} matching recipes:")
    else:
        print ("No matching recipes")
        return_menu()
        return

    
    # I have used enumerate for my list so each recipe starts with an index of 1
    for i, recipe in enumerate(found, 1):
        print(f"\nRecipe {i}    \n")
        recipe.print_recipe()
        
    option = input("\nEnter the number of the recipe you want to delete (or press Enter to cancel): ")

 
    #Checks if the users input is a number 
    if option.isdigit():
        index = int(option) - 1
        if 0 <= index < len(found):
            recipe_to_remove = found[index]
            recipe_list.remove(recipe_to_remove)
            print("The recipe has been removed!")
        else:
            print("Invalid! No recipe was removed.")
    else:
        print("Deletion cancelled.")

    return_menu()



''' The down below code is for saving the recipes in the below binary file '''

FILENAME = "recipe.pkl"

def save_recipes(recipe_list):
    # Saves the recipes to a file using pickle.
    try:
        with open(FILENAME, "wb") as file:
            pickle.dump(recipe_list, file)
    except Exception as e:
        print(f"Could not save recipes: {e}")
        return_menu()

def load_recipes():
    #Loads recipes from the pickle file if it exists.
    if not os.path.exists(FILENAME):
        return []
    
    try:
        with open(FILENAME, "rb") as file:
            return pickle.load(file)
    except (pickle.UnpicklingError, EOFError): #Cathing errors here like if the file is corrupted or there is no more data.
        print("Recipe file is empty or does not exist.")
        return []