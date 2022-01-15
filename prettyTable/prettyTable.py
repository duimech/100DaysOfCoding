from prettytable import PrettyTable

# Create an object from a Class
table = PrettyTable()

# Use the methods to add data to a table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Set attributes of the table
table.align = "l"

print(table)