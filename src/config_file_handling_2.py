import json
import pathlib
import requests

with open("..//src//config//config.json", "r") as f:
    config = json.load(f)


def get_users() -> dict:
    r = requests.get(config["api"]["url"])
    x= {
        "api":config["api"]["url"]
    }
    print(x["api"])
    return r.text


if __name__ == "__main__":
    # print(get_users())
    get_users()