# ----- Reading and Parsing -----
def read_input_file(file_name: str) -> list[str]:
    with open(file_name) as f:
        lines = f.readlines()
    return lines

def remove_newline_char(lines: list):
    return [line.strip() for line in lines]

def split_lines(lines: list, pattern: str = " "):
    return [line.split(pattern) for line in lines]
