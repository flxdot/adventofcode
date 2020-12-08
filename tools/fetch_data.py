"""
This module contains some code to scrape the adventofcode.com website for inputs and task descriptions.
"""
import os

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


def get_task_url(year: int, day: int) -> str:

    return f"https://adventofcode.com/{year}/day/{day}"


def get_task_description(year: int, day: int) -> str:
    """Fetches the description of the task for the specified year and day."""

    url = get_task_url(year, day)
    page = urlopen(url)
    html = page.read().decode("utf-8")
    page = BeautifulSoup(html, "html.parser")
    description = page.find_all("article", class_="day-desc")[0]
    return description.get_text()


def get_task_input(year: int, day: int) -> str:
    """Fetches the input of the specified day and task."""

    url = os.path.join(get_task_url(year, day), "input")

    response = requests.get(url, cookies={"session": read_cookie()})

    return response.text


def read_cookie():

    with open("../aoc_session.cookie", "r") as r:
        return r.read()

if __name__ == "__main__":
    print(get_task_input(2015, 23))
