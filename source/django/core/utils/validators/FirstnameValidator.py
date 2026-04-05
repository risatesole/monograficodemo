"""
###############################################################################
###############################################################################

This module provides a utility for validating first names.
It ensures that names follow standard formatting rules:
- Minimum and Maximum length
- Character restrictions (Only letters, hyphens, and spaces)
- No numeric or special characters

Example usage:
```
result = is_firstname_valid("Henry-Edilio")

if result is True:
    print("First name is valid.")
else:
    print(f"Errors: {', '.join(result)}")
```

###############################################################################
###############################################################################
"""

import re

def is_firstname_valid(name: str):
    """
    Validates a first name based on standard string requirements.
    Returns True if valid, or a list of error messages if invalid.
    """
    errors = []

    # 1. Strip whitespace to prevent " " passing as a name
    name = name.strip()

    # 2. Length Check
    if len(name) < 2:
        errors.append("First name must be at least 2 characters long.")
    elif len(name) > 50:
        errors.append("First name cannot exceed 50 characters.")

    # 3. Character Set Check 
    # Allows letters (Unicode), hyphens, and spaces (e.g., "Jean-Pierre" or "Mary Jane")
    # Does NOT allow numbers or symbols like @, #, $
    if not re.match(r'^[a-zA-ZÀ-ÿ\s\-]+\Z', name):
        errors.append("First name can only contain letters, hyphens, and spaces.")

    if not errors:
        return True
    
    return errors


# --- Manual Test ---
if __name__ == "__main__":
    test_names = ["H", "Henry", "Jean-Pierre", "John123", "  "]
    
    for n in test_names:
        res = is_firstname_valid(n)
        if res is True:
            print(f"[SUCCESS] '{n}' is valid.")
        else:
            print(f"[FAILURE] '{n}': {', '.join(res)}")
