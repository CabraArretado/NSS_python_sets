# Sets (unordered, unindexed & does NOT allow duplicates)

# Using set() to create a set
languages = set()

# Using curly braces allows you to initialize the set with values
languages = { 'english', 'mandarin chinese', 'spanish', 'english', 'spanish', 'portugese' }

print(languages)

# Put more stuff into a set
languages.add("hindi")
print(languages)

# Loop over the set
for language in languages:
    print(language)

instructors = {"Joe", "Madi", "Bryan"}
# Check for item in a collection (You can do this with lists, dictionaries, and tuples as well!)
if "Joe" in instructors:
    print("Yes, Joe is in this collection")