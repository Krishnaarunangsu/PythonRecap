import json
import pathlib
import requests

with open("..//src//config//config.json", "r") as f:
    config = json.load(f)

if __name__ == "__main__":
    print(json.dumps(config, indent=3))