from experta import *
from facts import *

class EliteBookTroubleshooter(KnowledgeEngine):

    # Rule 1: Power Issue (No lights, no start)
    @Rule(Symptom(power_on=False), Symptom(charging_light=False))
    def check_adapter(self):
        print("\n[EXPERT RECOMMENDATION]")
        print("Conclusion: Possible Power Adapter Failure.")
        print("Action: Ensure the 65W Smart AC Adapter is firmly connected to the USB-C port.")
        self.declare(Issue(resolved=True))

    # Rule 2: Performance Issue (Slow/Overheating)
    @Rule(Symptom(fans_loud=True), Symptom(laptop_hot=True))
    def check_ventilation(self):
        print("\n[EXPERT RECOMMENDATION]")
        print("Conclusion: Thermal Throttling.")
        print("Action: Use HP Support Assistant to update BIOS and clear dust from the EliteBook vents.")
        self.declare(Issue(resolved=True))

    # Rule 3: Keyboard Backlight Issue (Based on your specific inquiry)
    @Rule(Symptom(key_press_works=True), Symptom(light_off=True))
    def check_backlight(self):
        print("\n[EXPERT RECOMMENDATION]")
        print("Conclusion: Backlight is Disabled or Not Present.")
        print("Action: Press the 'F9' or 'Fn + F9' key. Look for the 'clavier lumineux' icon.")
        self.declare(Issue(resolved=True))

    # Rule 4: Default catch-all
    @Rule(NOT(Issue(resolved=True)))
    def default_action(self):
        print("\n[EXPERT RECOMMENDATION]")
        print("Conclusion: Unknown Hardware Fault.")
        print("Action: Contact HP Enterprise Support or check warranty status via serial number.")