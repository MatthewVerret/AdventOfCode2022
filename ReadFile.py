from typing import List

def read_files(file_txt: str) -> List[str]:
    lines: List[str] = []
    with open(file_txt) as f:
        lines = f.read().splitlines()
    return lines