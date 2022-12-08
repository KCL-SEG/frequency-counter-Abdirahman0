"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
 
  frequencies = {}
  
  for item in items:
    
    if isinstance(item, str):
      key = item
    else:
      key = str(item)

    # Step 4
    if key in frequencies:
      frequencies[key] += 1
    else:
      frequencies[key] = 1

  # Step 5
  return frequencies
