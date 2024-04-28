'''
Creates a function that will initialize all the aspects of the game that need to be set into place
'''

import csv

from Classes.OperationsRelated.room_class import Room
from Classes.OperationsRelated.ingredient_room_class import IngredientStorage
from Classes.CookingRelated.ingredient_class import Ingredient
from Classes.BookRelated.logbook_class import Logbook
from Classes.CookingRelated.dev_ingredient_class import devIngredient
from Functions.instruction_delivery_fn import instructions

def init_game(map, logbook):
    map.add_room(IngredientStorage('storage room','A large room where you store the ingrediants that are not currently in use. It is not a vary interesting rooms with no lighting of its own other than the doorway and walls lined with simple shelves full of ingedients.',['drying room']))
    map.add_room(Room('bedroom','The room you first awoke in. A simple room decorated only by maps and a small French flag. The only furniture is a bed desk and small dresser full of clothes identical to the set you wear right now.',['front room']))
    map.add_room(Room('front room','A long room with a bartop placed about halfway between you and the door to leave the shop. The walls are lined with empty glass jars about half a liter in size. Everytime you cross over the bar you feel a deep sense of dread that worsens the closer you drift towards the door. You have never been able to overcome it and try that door.',['bedroom', 'drying room', 'bottling room']))
    map.add_room(Room('bottling room','A dim room with a cobblestone floor walls and ceiling. In one corner you see an ornately decorated water well and in another you see a large cauldron bubbling over a heat-source hidden from sight. In the other two corners you see crates of empty bottles as well as a desk with a clear upper surface and a lower surface completely covered in different tools and utensils that would seem helpful in potion creation including a mortar and pestle.',['front room']))
    map.add_room(Room('drying room','A bright room lit with natural light from a greenhouse-like ceiling made of a hazy translucent material. The walls and ceiling are lined with strings from which hang various types of plants roots and barely-recognizable items all in various stages of drying. A sign forbids you from touching any of the plants you found hanging but didn\'t hang yourself. You see below the command there is a list of Alchemists with their respective roman numerals next to their names with little grave stones above each one. You decide to only touch the plants you hang.',['front room', 'storage room']))

    with open('/home/jspeebl/CPSC-1050-Project-2/ingredient_info.csv', 'r') as csvfile:
        ingredient_info = csv.DictReader(csvfile)
        for row in ingredient_info:
            for i in range(0,int(row['amount'])):
                ingredient = Ingredient(row)
                map.get_room('storage room').store_ingredient(ingredient)

    thistle = devIngredient('thistle','An odd looking plant broken up into stiff yet fleshy brown-yellow bits. The bits have no odor but have a rubbery texture when examined.','uncooked','dried','ground')
    esots = devIngredient('essence of the sea','A dark green powder contained in a large jar. It is only labeled with its name and has a salty odor when opened however it also seems to have a slightly sour undertone.','uncooked','dried','ground')
    unholy = devIngredient('bone of the unholy serpent','An off-white powder with no notable qualities other than its color and suspicious name. You sense this one is difficult to acquire and handle it with care.','uncooked','dried','ground')
    logbook.order1.add_ingredients(thistle)
    logbook.order1.add_ingredients(esots)
    logbook.order1.add_ingredients(unholy)

    mushroom1 = devIngredient('mushroom','A large white mushroom with a spherical cap. Seems to smell and look edible but who knows what it might do to a person.','uncooked','dried','ground')
    mushroom2 = devIngredient('mushroom','A large white mushroom with a spherical cap. Seems to smell and look edible but who knows what it might do to a person.','uncooked','dried','ground')
    esots = devIngredient('essence of the sea','A dark green powder contained in a large jar. It is only labeled with its name and has a salty odor when opened however it also seems to have a slightly sour undertone.','uncooked','dried','ground')
    leaves = devIngredient('leaves of the sacred vine','A collection of yellow-green leaves in a medium sized jar. They are waxy to the touch and seem to have retained moisture even though their musty smell seems to indicate they are quite old.','uncooked','dried','ground')
    logbook.order2.add_ingredients(mushroom1)
    logbook.order2.add_ingredients(mushroom2)
    logbook.order2.add_ingredients(esots)
    logbook.order2.add_ingredients(leaves)

    coffee = devIngredient('coffee','This one seems familiar. It is a brown powder that smells exactly like the ground coffee you know.', 'uncooked', 'dried', 'ground')
    esots = devIngredient('essence of the sea','A dark green powder contained in a large jar. It is only labeled with its name and has a salty odor when opened however it also seems to have a slightly sour undertone.','uncooked','dried','ground')
    leaves = devIngredient('leaves of the sacred vine','A collection of yellow-green leaves in a medium sized jar. They are waxy to the touch and seem to have retained moisture even though their musty smell seems to indicate they are quite old.','uncooked','dried','ground')
    logbook.order3.add_ingredients(coffee)
    logbook.order3.add_ingredients(esots)
    logbook.order3.add_ingredients(leaves)
