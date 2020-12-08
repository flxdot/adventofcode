import os
from datetime import datetime

from tools.setup_repo import write_day

if __name__ == "__main__":
    day = datetime.now().day
    year = datetime.now().year

    input_file = os.path.join(f"year{year}", "inputs", f"day{day}.txt")
    if os.path.getsize(input_file) == 0:
        write_day(year, day)
