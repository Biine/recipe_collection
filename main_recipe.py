import recipe

def print_menu():
    print("@  " * 17)
    print("@  " * 17)
    print("\n")

    indent = "        "
    print("@" + indent + "    RECIPE COLLECTION    " + "              @")
    print("\n@" + indent + "    Add new recipe    ( 1 )" + "            @")
    print("@" + indent + "    Show all recipes  ( 2 )" + "            @")
    print("@" + indent + "    Search for recipe ( 3 )" + "            @")
    print("@" + indent + "    Remove a recipe   ( 4 )" + "            @")
    print("@" + indent + "    Exit program      ( 5 )" + "            @")


def main():
   # Loading recipes from the pickle file "recipe.pkl"
    recipe_list = recipe.load_recipes()
    #Adding a starting recipe to the collection to have something there to work with
    # if not recipe_list:
    #     recipe_list.append(recipe.Recipe("Pancakes", ["Dessert", "Lunch"], ["Flour", "Milk", "Eggs", "Salt", "Butter"], "Mix everything and fry in a pan."))
    #     recipe.save_recipes(recipe_list)

    if not recipe_list:
        recipe_list.append(
            recipe.Recipe(
                "Pancakes", 
                ["Dessert", "Lunch"], 
                ["Flour", "Milk", "Eggs", "Salt", "Butter"], 
                ["2 dl", "3 dl", "2", "1/4 tsp", "50 g"],  # Added amounts list
                "Mix everything and fry in a pan."          # Instructions
            )
        )
        recipe.save_recipes(recipe_list)


    while True:
        recipe.clear_console()
        print_menu()
        option = input("\n             Choose an option  (1-5): ") 

        if option == "1":           # Adds new recipe
            recipe.add_recipe(recipe_list)
            recipe.save_recipes(recipe_list)

              
        elif option == "2":         # Shows all recipes
            recipe.show_recipes(recipe_list)


        elif option == "3":        #Searches for a recipe
            recipe.search_recipe(recipe_list)


        elif option == "4":        # Removes a recipe
            recipe.remove_recipe(recipe_list)    
            recipe.save_recipes(recipe_list)  


        elif option == "5":        #Exits program
            recipe.save_recipes(recipe_list)
            print("\nExiting program. Enjoy your meal!")
            break
        else:
            print("\nInvalid choice! Please choose a number between 1 and 5.")
            recipe.return_menu()


   
if __name__ == "__main__":
    main()