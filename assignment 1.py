```python
def check_traffic_light(color):
    """
    Determines the action based on the traffic light color.
    """
    # Convert input to uppercase for case-insensitive check
    signal = color.upper()
    
    if signal == "RED":
        print("🔴 Stop. Wait for the green light.")
    elif signal == "YELLOW":
        print("🟡 Caution. Prepare to stop or proceed with care.")
    elif signal == "GREEN":
        print("🟢 Go. Proceed through the intersection.")
    else:
        print(f"❌ '{color}' is not a valid traffic light color.")