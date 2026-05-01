from experta import Fact

class Issue(Fact):
    """
    Represents the final diagnosis state of the system.
    Used to track whether a conclusion has been reached.
    Example: Issue(resolved=True)
    """
    pass

class Symptom(Fact):
    """
    Specific observable behavior reported or detected on the HP EliteBook 845 G8.
    Each attribute represents a yes/no observable condition.
    Example: Symptom(power_on=False), Symptom(fans_loud=True)
    """
    pass

class HardwareStatus(Fact):
    """
    State of a specific hardware component on the laptop.
    Used to represent component-level diagnostics.
    Example: HardwareStatus(battery="dead"), HardwareStatus(screen="blank")
    """
    pass
