from datetime import datetime

from tools.setup_repo import write_readme_file


def update_all_readme():
    now = datetime.now()
    for year in range(2015, 2021):
        for day in range(1, 25):
            if year >= now.year and day > now.day:
                return
            print(f"{year}/{day}")
            write_readme_file(year, day)


if __name__ == "__main__":

    # write_readme_file(2017, 1)
    update_all_readme()
