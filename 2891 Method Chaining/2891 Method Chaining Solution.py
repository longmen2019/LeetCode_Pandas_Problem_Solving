import pandas as pd
data = {
    "name": ["Tatiana", "Khaled", "Alex", "Jonathan", "Stefan", "Tommy"],
    "species": ["Snake", "Giraffe", "Leopard", "Monkey", "Bear", "Panda"],
    "age": [98, 50, 6, 45, 100, 26],
    "weight": [464, 41, 328, 463, 50, 349]

}

def findHeavyAnimals():
    # Create a DataFrame from the data
    animals = pd.DataFrame(data)

    # Here is the one-line solution using method chaining
    result = animals[animals["weight"] > 100].sort_values(by='weight', ascending=False)[['name']]
    return result

print(findHeavyAnimals())