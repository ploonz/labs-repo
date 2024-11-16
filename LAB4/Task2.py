# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open (INPUT_FILENAME) as inpf:
        rows=[]
        data=csv.DictReader(inpf,lineterminator="\n")
        for row in data:
            rows.append(row)
        with open(OUTPUT_FILENAME,'w') as outf:
            json.dump(rows,outf,indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line,end="")
