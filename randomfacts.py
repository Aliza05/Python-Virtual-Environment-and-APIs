import randfacts

print("Some Random Facts are: ")

for facts in range(3):
    fact = randfacts.get_fact()
    print(fact)
