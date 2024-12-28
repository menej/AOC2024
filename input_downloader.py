import yaml
import requests


def load_cookie_from_yaml(yaml_file):
    with open(yaml_file, "r") as file:
        config = yaml.safe_load(file)
    return config["adventofcode"]["session_cookie"]


def download_input(day, year, yaml_file):
    session_cookie = load_cookie_from_yaml(yaml_file)
    if not session_cookie:
        raise ValueError("Session cookie not found in the configuration file.")

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {
        "Cookie": f"session={session_cookie}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open(f"./Day{day:02}/input.txt", "w") as file:
            file.write(response.text)
        print(f"Input for Day {day} saved as day{day}_input.txt")
    else:
        print(f"Failed to download input: {response.status_code}, {response.text}")


if __name__ == "__main__":
    yaml_file = "config.yaml"

    day = 1
    year = 2024

    download_input(day, year, yaml_file)
