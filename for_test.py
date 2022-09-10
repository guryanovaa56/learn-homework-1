classes = [
    {'name': '3А', 'scores': [3,4,4,5,2]},
    {'name': '3Б', 'scores': [5,5,3,2,2]},
    {'name': '3В', 'scores': [4,5,3,5,4]},
]
def count_average(students_scores):
    scores_sum = 0
    for score in students_scores:
        scores_sum += score
    scores_avg = scores_sum / len(students_scores)
    return scores_avg
for one_class in classes:
    class_score_avg = count_average(one_class['scores'])
    print(f"Средняя оценка для класса {one_class['name']}: {class_score_avg}")