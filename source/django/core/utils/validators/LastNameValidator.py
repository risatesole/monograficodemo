"""
###############################################################################
###############################################################################

This module provides a utility for validating last names.
It ensures that surnames follow standard formatting rules:
- Minimum and Maximum length
- Character restrictions (Letters, hyphens, and spaces)
- Supports accented characters (ñ, é, etc.)

Example usage:
```
result = is_lastname_valid("Ramirez-Chevalier")

if result is True:
    print("Last name is valid.")
else:
    print(f"Errors: {', '.join(result)}")
```

###############################################################################
###############################################################################
"""

import re

def is_lastname_valid(name: str):
    """
    Validates a last name based on standard string requirements.
    Returns True if valid, or a list of error messages if invalid.
    """
    errors = []

    # 1. Clean input
    if not name:
        return ["Last name cannot be empty."]
    
    name = name.strip()

    # 2. Length Check
    if len(name) < 2:
        errors.append("Last name must be at least 2 characters long.")
    elif len(name) > 100:  # Surnames can often be longer than first names
        errors.append("Last name cannot exceed 100 characters.")

    # 3. Character Set Check 
    # Allows letters (including Unicode accents), hyphens, and spaces.
    # Rejects numbers and special symbols.
    if not re.match(r'^[a-zA-ZÀ-ÿ\s\-]+\Z', name):
        errors.append("Last name can only contain letters, hyphens, and spaces.")

    if not errors:
        return True
    
    return errors

if __name__ == "__main__":
    test_names = ["Ramirez", "St. John", "O'Reilly", "12345", "A"]
    
    for n in test_names:
        res = is_lastname_valid(n)
        if res is True:
            print(f"[SUCCESS] '{n}' is valid.")
        else:
            print(f"[FAILURE] '{n}': {', '.join(res)}")
