data: list[str] = [
    "Pessoa 1",
    "Pessoa 2",
    "Pessoa 3",
    "Pessoa 4",
    "Pessoa 5",
    "Pessoa 8"
]


def get_studies_list() -> str:
    global data

    ret = "<ul>"

    for study_user in data:
        ret += "<li>" + study_user + "</li>"

    ret += "</ul>"

    return ret
