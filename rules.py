from experta import *
from facts import *

class EliteBookTroubleshooter(KnowledgeEngine):
    """
    Knowledge Engine for the HP EliteBook 845 G8 Diagnostic System.
    Each @Rule method represents a piece of expert knowledge mapping
    observed symptoms and hardware states to a recommended action.
    """

    # ─── Rule 1: Power / Adapter Issue ───────────────────────────────────────
    @Rule(Symptom(power_on=False), Symptom(charging_light=False))
    def check_adapter(self):
        """Fires when laptop does not turn on AND charging light is absent."""
        print("\n[EXPERT RECOMMENDATION]")
        print("Conclusion : Possible Power Adapter or DC Jack Failure.")
        print("Action     : Ensure the 65W Smart AC Adapter is firmly connected to the")
        print("             USB-C port. Try a different certified HP adapter if available.")
        self.declare(Issue(resolved=True))

    # ─── Rule 2: Dead Battery ─────────────────────────────────────────────────
    @Rule(Symptom(power_on=False), Symptom(charging_light=True),
          HardwareStatus(battery="dead"))
    def check_battery(self):
        """Fires when laptop won't start but charging light IS on → battery fault."""
        print("\n[EXPERT RECOMMENDATION]")
        print("Conclusion : Battery Hardware Failure.")
        print("Action     : Hold Power button 15 s to hard-reset, then reconnect adapter.")
        print("             If the issue persists, replace the internal Li-ion battery.")
        self.declare(Issue(resolved=True))

    # ─── Rule 3: Thermal Throttling / Overheating ────────────────────────────
    @Rule(Symptom(fans_loud=True), Symptom(laptop_hot=True))
    def check_ventilation(self):
        """Fires when fans are very loud AND chassis is hot → thermal issue."""
        print("\n[EXPERT RECOMMENDATION]")
        print("Conclusion : Thermal Throttling Detected.")
        print("Action     : Use HP Support Assistant to update BIOS firmware.")
        print("             Clear dust from vents with compressed air.")
        print("             Avoid use on soft surfaces that block airflow.")
        self.declare(Issue(resolved=True))

    # ─── Rule 4: Keyboard Backlight Issue ────────────────────────────────────
    @Rule(Symptom(key_press_works=True), Symptom(light_off=True))
    def check_backlight(self):
        """Fires when keys register input but backlight is off → software toggle."""
        print("\n[EXPERT RECOMMENDATION]")
        print("Conclusion : Keyboard Backlight is Disabled or Unavailable.")
        print("Action     : Press F9 or Fn + F9 — look for the 'clavier lumineux' icon.")
        print("             Note: Some EliteBook 845 G8 SKUs ship without a backlit keyboard.")
        self.declare(Issue(resolved=True))

    # ─── Rule 5: Blank Screen / Display Fault ────────────────────────────────
    @Rule(Symptom(power_on=True), HardwareStatus(screen="blank"))
    def check_display(self):
        """Fires when laptop is on but screen stays blank → display/GPU fault."""
        print("\n[EXPERT RECOMMENDATION]")
        print("Conclusion : Display or GPU Signal Failure.")
        print("Action     : Connect an external monitor via USB-C or HDMI.")
        print("             If external display works → replace internal screen.")
        print("             If external display also fails → GPU or driver issue;")
        print("             boot into Safe Mode and update display drivers.")
        self.declare(Issue(resolved=True))

    # ─── Rule 6: Default Catch-All ───────────────────────────────────────────
    @Rule(NOT(Issue(resolved=True)))
    def default_action(self):
        """Fires only when no other rule could reach a conclusion."""
        print("\n[EXPERT RECOMMENDATION]")
        print("Conclusion : Unknown or Complex Hardware Fault.")
        print("Action     : Contact HP Enterprise Support (1-800-334-5144) or check")
        print("             your warranty status via serial number at hp.com/go/support.")
