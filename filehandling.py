def read_and_write_modified_file():
    source = input("Enter the source filename: ")
    destination = input("Enter the destination filename: ")

    try:
        # Attempt to read the source file
        with open(source, 'r') as src_file:
            content = src_file.read()
            print("Original content read successfully.")

        # Modify the content 
        modified_content = content.upper()

        
        with open(destination, 'w') as dest_file:
            dest_file.write(modified_content)
            print(f"Modified content written to '{destination}'.")

    except FileNotFoundError:
        print(f"Error: The file '{source}' does not exist.")
    except PermissionError:
        print("Error: You don't have permission to read or write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_write_modified_file() 
