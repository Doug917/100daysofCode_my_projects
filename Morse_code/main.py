import json
import sys

with open("morse_keys.json", "r") as morse_data:
    morse_keys = json.load(morse_data)

try:
    filename = sys.argv[1]
except:
    sys.exit("Usage: python3 main.py filename.txt")
else:
    with open(filename, "r") as input_file:
        content = input_file.readlines()
        output_lines = []
        for line in content:
            line_output = []
            for c in line:
                if c.isnumeric():
                    line_output.append(morse_keys[c])
                elif not c.isalnum():
                    line_output.append(c)
                else:
                    line_output.append(morse_keys[c.upper()])
            output_lines.append(" ".join(line_output))

with open("output_file.txt", "w") as out_file:
    for line in output_lines:
        out_file.write(line)

