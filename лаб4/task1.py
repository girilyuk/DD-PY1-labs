# TODO решите задачу
import json

def task(file_path):
    with open(file_path) as f:
        data = json.load(f)
    total_sum = sum(item['score'] * item['weight'] for item in data)
    return round(total_sum, 3)


print(task('input.json'))
