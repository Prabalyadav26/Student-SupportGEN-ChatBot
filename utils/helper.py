import json
import os


def load_json(filename):

    base_dir = os.path.dirname(os.path.dirname(__file__))

    file_path = os.path.join(
        base_dir,
        "knowledge",
        filename
    )

    with open(file_path, "r", encoding="utf-8") as file:

        data = json.load(file)

    return data


# ADD THIS
def load_knowledge():

    return load_json("knowledge_base.json")