# TODO решите задачу
import json
def task() -> float:
    with open ('input.json','r') as f:
        data=json.load(f)
        final=0
        for item in data:
            final+=item.get('score')*item.get('weight')
    return round(weight,3)


print(task())
