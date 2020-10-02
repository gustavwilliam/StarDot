import argparse
import sys

CHAR_DELIMITER = "*"
LINE_DELIMITER = ":"

parser = argparse.ArgumentParser(description="Interpreter for the Stardot language.")
parser.add_argument("file", type=argparse.FileType('r'), help="The file to parse.")
parser.add_argument("--mode", "-m", 
					nargs='?',
					const="execute",
					choices=["execute", "encode", "decode"],
					type=str,
					help="Specifies what the program should do."
					)

args = parser.parse_args()
mode = args.mode
code = "\n".join(args.file.readlines())


def _line_to_python(line: str) -> str:
	"""Converts a line from Stardot to Unicode."""
	characters = line.split(CHAR_DELIMITER)

	for i, char in enumerate(characters):
		characters[i] = chr(len(char))

	return "".join(characters)

def _line_to_stardot(line: str) -> str:
	"""Converts a line from Unicode to Stardot."""
	chars = list(line)

	for i, char in enumerate(chars):
		chars[i] = "." * ord(char)

	return "*".join(chars)

def to_python(code: str) -> str:
	"""Converts code from Stardot to Python."""
	lines = code.split(LINE_DELIMITER)

	for i, line in enumerate(lines):
		lines[i] = _line_to_python(line)

	return "\n".join(lines)

def to_stardot(code: str) -> str:
	"""Converts code from Python to Stardot."""
	code_list = [line for line in code.split("\n") if line]

	for i, line in enumerate(code_list):
		code_list[i] = _line_to_stardot(line)
	
	return ":".join(code_list)


if __name__ == "__main__":
	if mode == "execute":
		exec(to_python(code))

	elif mode == "encode":
		print(to_stardot(code))

	else:
		print(to_python(code))
