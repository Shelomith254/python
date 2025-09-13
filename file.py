try:
    filename = input("Enter the filename to read: ")

    with open(filename, "r") as f:
        content = f.read()

    # Example modification: make text uppercase
    modified_content = content.upper()

    with open("modified_" + filename, "w") as f:
        f.write(modified_content)

    print("File has been modified and saved as modified_" + filename)

except FileNotFoundError:
    print(" File not found. Please check the name and try again.")
except Exception as e:
    print("An error occurred:", e)
