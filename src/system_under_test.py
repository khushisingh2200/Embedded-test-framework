def check_temperature(temp: float) -> str:
    """
    Simulated embedded system logic.
    Returns ALERT if temperature is above 100,
    otherwise returns NORMAL.
    """
    if temp > 100:
        return "ALERT"
    return "NORMAL"