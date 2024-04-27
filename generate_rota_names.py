import datetime
import pathlib
from copy import copy

import numpy as np
import yaml


def save_yaml(filepath, dict_list):
    with open(filepath, mode="w") as file_writer:
        yaml.dump(data=dict_list, stream=file_writer)


seed = 20220905

speaker_names = {
    "Antreas",
    "Tom",
    "Justin",
    "Elliot",
    "Joe",
    "Asif",
    "William",
    "Adam",
    "Amos",
    "Alessandro",
    "Mateusz",
    "Chenhongyi",
}

num_weeks_to_generate = 21

speakers_available = copy(speaker_names)

start_date = datetime.date(2022, 9, 5)  # YYYY, M, D - ENSURE THIS IS MONDAY

dates = [
    f"{start_date + datetime.timedelta(days=(7 * d))}"
    for d in range(num_weeks_to_generate)
]

dates = [
    datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%y") for date in dates
]

week_entries = []

for week_idx in range(num_weeks_to_generate):
    if len(speakers_available) < 2:
        speakers_available = copy(speaker_names)

    choose_speakers = np.random.choice(
        list(speakers_available), size=(2,), replace=False
    )
    week_entries.append(
        dict(
            week_date=str(dates[week_idx]),
            group=str(choose_speakers[0]),
            reading=str(choose_speakers[1]),
        )
    )

    speakers_available.remove(choose_speakers[0])
    speakers_available.remove(choose_speakers[1])

print(week_entries)
if not pathlib.Path("_data").exists():
    pathlib.Path("_data").mkdir()
save_yaml(filepath="_data/rota_names.yml", dict_list=week_entries)
