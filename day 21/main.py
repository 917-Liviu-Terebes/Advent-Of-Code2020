"""
--- Day 21: Allergen Assessment ---
- Strategy:
Set magic: For part 1, we keep intersecting lists of possible allergen ingredients and then return the number of
ingredients which do not appear in that set
For part 2: While we have not found all pairs ingredient-allergen, we try to find the pairs in the set of possible
allergen ingredients and, if a pair is found, we save it and extract it from other possible sets.
"""


def part1():
    """
    Part 1 of the problem
    """
    # List to store all food ingredients
    food_ingredients_list = []

    # Perform the task on each stripped line from the file
    for line in map(str.rstrip, f.readlines()):
        # Get the ingredients and the allergens from the line
        line_ingredients, line_allergens = line.split(" (contains ")

        # Place each ingredient in a food set (current food)
        foods = set(line_ingredients.split())

        # Save the ingredients in the list
        food_ingredients_list.append(line_ingredients.split())

        # Place each allergen in a set
        allergens = set(line_allergens[:-1].split(", "))

        for allergen in allergens:
            # If the allergen is new, create a new entry in the dict and place all line ingredients as value
            if allergen not in possible_allergens:
                possible_allergens[allergen] = foods.copy()
            else:
                # Else, keep only the intersection of the sets (an ingredient which is only in one set cannot be
                # the source for the allergen)
                possible_allergens[allergen] &= foods

    # Get all allergen ingredients from the set of possible allergens
    all_allergen_ingredients = set(ingredient for allergen_list in possible_allergens.values()
                                   for ingredient in allergen_list)
    # Return the number of ingredients which are not in the previous set
    return sum(ingredient not in all_allergen_ingredients for food in food_ingredients_list for ingredient in food)


def part2():
    """
    Part 2 of the problem
    """
    # Containers to hold the items
    found_allergen_ingredients = set()
    allergen_ingredient_list = []
    # Keep searching for the ingredients until the search is complete
    while True:
        for allergen, ingredient_list in possible_allergens.items():
            # ingredient_list - found_allergen_ingredients is the set of ingredients which may contain the allergen
            # but which set does not contain the already found allergen ingredients for other allergens
            # So, if the length is 1, that means that the remaining ingredient is the source for the allergen
            # And we memorize it
            if len(ingredient_list - found_allergen_ingredients) == 1:
                # Get the faulty ingredient
                found_allergen_ingredient = min(ingredient_list - found_allergen_ingredients)
                # And place it in the containers
                allergen_ingredient_list.append((allergen, found_allergen_ingredient))
                found_allergen_ingredients.add(found_allergen_ingredient)
                # Break to get to restart the search with the new found ingredient
                break
        else:
            break

    # Return the ingredients, sorted by their allergen
    return ",".join(x[1] for x in sorted(allergen_ingredient_list))


if __name__ == '__main__':
    f = open('input.txt', 'rt')
    possible_allergens = {}

    print("Part 1: ", part1())
    print("Part 2: ", part2())

    f.close()
