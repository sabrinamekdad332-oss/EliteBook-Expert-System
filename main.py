import collections
if not hasattr(collections, 'Mapping'):
    import collections.abc
    collections.Mapping = collections.abc.Mapping

from experta import *
from facts import *
from rules import EliteBookTroubleshooter


# ─── Helper ──────────────────────────────────────────────────────────────────

def ask(question):
    """
    Prompts the user with a yes/no question and validates the input.
    Keeps asking until the user types 'y' or 'n'.
    This prevents unexpected behavior from invalid input.

    Args:
        question (str): The question string to display.

    Returns:
        str: 'y' or 'n'
    """
    while True:
        answer = input(question + " (y/n): ").strip().lower()
        if answer in ('y', 'n'):
            return answer
        print("  ⚠ Invalid input. Please enter 'y' or 'n'.")


# ─── Diagnostic Engine ───────────────────────────────────────────────────────

def start_diagnostic():
    """
    Main entry point for the HP EliteBook 845 G8 Diagnostic Expert System.

    This function simulates backward-chaining by conducting a targeted
    interview: it only asks follow-up questions that are relevant to the
    current hypothesis being investigated, pruning irrelevant branches early.

    Facts are declared based on user answers, then the KnowledgeEngine
    fires all matching rules (forward chaining via the Rete algorithm).
    """
    print(f"\n{'='*52}")
    print("  HP ELITEBOOK 845 G8 — DIAGNOSTIC EXPERT SYSTEM  ")
    print(f"{'='*52}\n")
    print("This system will ask a series of diagnostic questions.")
    print("Please answer honestly with 'y' (yes) or 'n' (no).\n")

    engine = EliteBookTroubleshooter()
    engine.reset()

    # ── Branch 1: Power ──────────────────────────────────────────────────────
    if ask("1. Does the laptop turn on at all?") == 'n':
        engine.declare(Symptom(power_on=False))

        if ask("2. Is the side charging LED indicator light visible?") == 'y':
            # Power is reaching the board → likely battery fault
            engine.declare(Symptom(charging_light=True))
            engine.declare(HardwareStatus(battery="dead"))
        else:
            # No power at all → adapter failure
            engine.declare(Symptom(charging_light=False))

    # ── Branch 2: Performance & Thermals ────────────────────────────────────
    else:
        engine.declare(Symptom(power_on=True))

        if ask("2. Is the screen blank even though the laptop seems on?") == 'y':
            # Declare screen hardware status → triggers Rule 5
            engine.declare(HardwareStatus(screen="blank"))

        if ask("3. Are the cooling fans unusually loud?") == 'y':
            engine.declare(Symptom(fans_loud=True))

        if ask("4. Is the bottom of the chassis uncomfortably hot?") == 'y':
            engine.declare(Symptom(laptop_hot=True))

        # ── Branch 3: Keyboard ───────────────────────────────────────────────
        if ask("5. Is the keyboard backlight currently off?") == 'y':
            engine.declare(Symptom(light_off=True))

            if ask("6. Do key presses still register (i.e., typing works)?") == 'y':
                engine.declare(Symptom(key_press_works=True))

    # ── Run inference engine ─────────────────────────────────────────────────
    print("\n⟳  Analyzing symptoms against knowledge base...\n")
    engine.run()
    print(f"\n{'='*52}\n")


# ─── Entry Point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    start_diagnostic()
