#!/usr/bin/env python3

import random
from faker import Faker

ENTRIES = 100
TARGET_FILE = "test.txt"
DISEASES = ["COVID-2019", "SARS-1", "H1N1", "FLU-2018", "SARS-COV-2", "MERS-COV", "EVD"]
COUNTRIES = ["Greece", "USA", "Brazil", "China", "Denmark", "Egypt", "Argentina", "Australia",
             "Russia", "Italy", "Switzerland", "Turkey", "Vietnam", "France", "Germany"]


if __name__ == "__main__":
    id_list = list(range(ENTRIES))
    random.shuffle(id_list)
    fake = Faker()
    # fake.country().replace(" ", "_")

    with open(TARGET_FILE, "w") as f:
        for i in range(ENTRIES):
            entry_date = fake.date_this_century(before_today=True, after_today=False)
            exit_date = fake.date_this_century(before_today=True, after_today=False)
            if entry_date > exit_date:
                entry_date, exit_date = exit_date, entry_date
            f.write("{} {} {} {} {} {}\n".format(
                id_list[i], fake.name(), random.choice(DISEASES),
                random.choice(COUNTRIES), entry_date.strftime('%d-%m-%Y'),
                str(random.choices([exit_date.strftime('%d-%m-%Y'), "-"], [0.9, 0.1])).strip("[]'")))
