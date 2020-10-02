import argparse
import sys

CHAR_DELIMITER = "*"
LINE_DELIMITER = ":"


def _line_to_python(line: str) -> str:
	"""Converts a line from Stardot to Unicode."""
	characters = [chr(len(char)) for char in line.split(CHAR_DELIMITER)]
	return "".join(characters)

def _line_to_stardot(line: str) -> str:
	"""Converts a line from Unicode to Stardot."""
	chars = ["."*ord(char) for char in list(line)]
	return "*".join(chars)

def to_python(code: str) -> str:
	"""Converts code from Stardot to Python."""
	lines = [_line_to_python(line) for line in code.split(LINE_DELIMITER)]
	return "\n".join(lines)

def to_stardot(code: str) -> str:
	"""Converts code from Python to Stardot."""
	code_list = [line for line in code.split("\n") if line]
	code_list = [_line_to_stardot(line) for line in code_list]
	return ":".join(code_list)


if __name__ == "__main__":
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

	if mode == "execute":
		exec(to_python(code))

	elif mode == "encode":
		print(to_stardot(code))

	else:
		print(to_python(code))
