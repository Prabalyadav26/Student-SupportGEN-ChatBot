history = []


def add_message(role, message):

    history.append(
        {
            "role": role,
            "message": message
        }
    )


def get_history():

    return history