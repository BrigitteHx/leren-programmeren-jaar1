#multiplier-x.py

def multiplier(tafel):
    for i in range(1,11):
        print(f"{i} x {tafel} = {i*tafel}")
multiplier(tafel = int(input("Kies een tafel van 1-10. ")))