input_file = "app.log"
output_file = "errors.log"

error_lines = []

with open(input_file, "r") as file:
    for line in file:
        if "ERROR" in line:
            error_lines.append(line.strip())

with open(output_file, "w") as file:
    file.write("Error Log Summary\n")
    file.write("==================\n")
    for error in error_lines:
        file.write(error + "\n")

print(f"{len(error_lines)} error lines written to '{output_file}'")