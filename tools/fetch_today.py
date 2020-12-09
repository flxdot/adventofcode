import os
from datetime import datetime

from tools.setup_repo import write_day, write_readme_file

if __name__ == "__main__":
    day = datetime.now().day
    year = datetime.now().year

    input_file = os.path.join(f"year{year}", f"day{day}", "input.txt")
    if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
        write_day(year, day)
    else:
        write_readme_file(year, day)
