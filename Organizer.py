def organizer():
    with open("README.md", "r+") as file:
        lines = file.readlines()
        sorted_lines = sorted(lines)  # Corrected sorting
        file.seek(0)
        file.writelines(sorted_lines)  # Write the sorted lines back

def order():
    with open("README.md", "r+") as file:
        sorted_lines = file.readlines()  # Read the sorted lines
    with open("README.md", "w") as file:
        for i, line in enumerate(sorted_lines, start=1):
            file.write(f"{i} {line} \n")

if __name__ == "__main__":
    organizer()
    order()
