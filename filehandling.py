def create_sample_file():
    with open("sample.txt", "w") as file:
        file.write("Hello, world!\nThis is a test file.")
    print("✅ 'sample.txt' created successfully.")



def modify_file_content(text):
    return text.upper()

def main():
    create_sample_file()  

    try:
        input_filename = input("Enter the name of the file to read: ")

        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("\nOriginal Content:\n")
            print(content)

        modified_content = modify_file_content(content)

        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"\nModified content written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print("❌ Error: The file was not found.")
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
