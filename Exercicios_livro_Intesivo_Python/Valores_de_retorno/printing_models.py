from time import sleep


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print(f"Printing models: {current_design.title()}")
        completed_models.append(current_design)
        sleep(1)

def show_completed_models(completed_models):
    print("\nThe following models have been printed")
    for model in completed_models:
        print(f"{model.title()}")
        sleep(1)

