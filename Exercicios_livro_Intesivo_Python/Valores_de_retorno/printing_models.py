from time import sleep

unprinted_designs = ['dragon ball', 'fly', 'jaspion', 'bleach', 'hunter x hunter', 'demon slayer']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()

    print(f"Printing models: {current_design.title()}")
    completed_models.append(current_design)
    sleep(1)

if __name__ == '__main__':
    print("\nThe following models have been printed")
    for model in completed_models:
        print(f"{model.title()}")
        sleep(1)
