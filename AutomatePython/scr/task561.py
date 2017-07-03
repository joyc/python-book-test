stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

displayInventory(stuff)


# task 5.6.2

def addToInventory(inventory, addedItems):
    for v in addedItems:
        # if v in inventory.keys():
        #     inventory[v] += 1
        # else:
        #     inventory[v] = 1
     inventory[v] = inventory.get(v, 1)
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)