```python
def calculate_grade(score):
    """
    Assigns a letter grade based on a numerical score.
    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    F: Below 60
    """
    if score >= 90:
        return "A (Excellent!)"
    elif score >= 80:
        return "B (Very good!)"
    elif score >= 70:
        return "C (Good work!)"
    elif score >= 60:
        return "D (Satisfactory)"
    else:
        return "F (Needs improvement)"