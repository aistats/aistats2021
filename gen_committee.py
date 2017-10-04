import sys
import os

data_dir = "/home/antreas/antreasantoniou.github.io/committee.csv"
target_dir = "/home/antreas/antreasantoniou.github.io/committee.txt"
with open(data_dir, mode="r") as open_csv:
    data = open_csv.readlines()

data = data[1:]
output_file = ["- type: Senior Committee\npeople:\n"]
    # - family: Crowley
    #   given: Elliot
    #   url: http://homepages.inf.ed.ac.uk/ecrowley/
    #   institute: School of Informatics, University of Edinburgh

for entry in data:
    name, surname, institution, email = entry.replace("\n", "").split(",")
    entry_line = "  - family: {surname}\n    given: {name}\n    url: {url}\n    institute: ({institution})\n".format(
        name=name, surname=surname, institution=institution, url=email)
    output_file.append(entry_line)

with open(target_dir, mode="wb+") as write_file:
    write_file.writelines(output_file)
