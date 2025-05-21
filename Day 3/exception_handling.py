filename = "example.txt"  

try:
    if not filename.endswith(".txt"):
        raise ValueError("Unsupported file format. Only .txt files are allowed.")
    
    file = open(filename, "r")
    
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    
except PermissionError:
    print(f"Error: You don't have permission to read the file '{filename}'.")
    
except ValueError as ve:
    print(f"Error: {ve}")
    
else:
    print(f"Reading file: {filename}")
    content = file.read()
    print("File content:\n", content)
    
finally:
    try:
        file.close()
        print("File closed.")
    except NameError:
        print("No file to close.")
