import collections
if not hasattr(collections, 'Mapping'):
    import collections.abc
    collections.Mapping = collections.abc.Mapping

from experta import *
from facts import *
from rules import EliteBookTroubleshooter

def start_diagnostic():
    print(f"{'='*50}")
    print(" HP ELITEBOOK 845 G8 DIAGNOSTIC EXPERT SYSTEM ")
    print(f"{'='*50}\n")
    
    engine = EliteBookTroubleshooter()
    engine.reset()
    
    # Gathering Facts through user interview
    print("Please answer the following (y/n):")
    
    if input("- Does the laptop turn on at all? ") == 'n':
        engine.declare(Symptom(power_on=False))
        if input("- Is the side charging light visible? ") == 'n':
            engine.declare(Symptom(charging_light=False))
    else:
        engine.declare(Symptom(power_on=True))
        if input("- Are the cooling fans very loud? ") == 'y':
            engine.declare(Symptom(fans_loud=True))
        if input("- Is the bottom of the chassis hot? ") == 'y':
            engine.declare(Symptom(laptop_hot=True))
        if input("- Is the keyboard backlight currently off? ") == 'y':
            engine.declare(Symptom(light_off=True))
            engine.declare(Symptom(key_press_works=True))

    print("\nProcessing rules and knowledge base...")
    engine.run()

if __name__ == "__main__":
    start_diagnostic()