# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount_plus):
    pet_shop["admin"]["total_cash"] += amount_plus

def add_or_remove_cash(pet_shop, amount_minus):
    pet_shop["admin"]["total_cash"] += amount_minus 

def get_pets_sold(sold_pets):
    return sold_pets["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sold_pets):
    pet_shop["admin"]["pets_sold"] += sold_pets

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

    
def get_pets_by_breed(pet_shop, breed):
    list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
             list.append(pet)
    return list


def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)
    return pet_shop

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet) 
    return pet_shop

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount 
    return customer

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet) 
    return customer

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet is None:
        return
    if customer["cash"] < pet["price"]:
        return
    customer["pets"].append(pet)
    pet_shop["pets"].remove(pet)
    customer["cash"] -= pet["price"]
    pet_shop["admin"]["total_cash"] += pet["price"]
    pet_shop["admin"]["pets_sold"] += 1





