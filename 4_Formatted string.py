"""
Formatted string converts a primitive variable of the programming language into a 
human-readable string representation.
"""
# Print -- " Harry is a [Good] boy "

print("Harry is a " + '[' + "Good" + ']' + " boy")

# Using formatted string for the same

name = "Harry"
var2 = "Good"
msg = f'{name} is a [{var2}] boy'
print(msg)


msg2 = "Harry is a "  f"[{'Good'}] boy"
print(msg2)