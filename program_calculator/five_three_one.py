from program_calculator.operations.csv_operations import createCsvXlsFormat
from program_calculator.operations.exercise_calculations import ceil_to_increment, calculate_plan_strength, \
    group_exercises


def five_three_one(exercises):
    plan = []

    for exercise in exercises:
        if exercise.get('rm') is not None:
            rm = exercise['rm']
        if exercise.get('unit') is not None:
            unit = exercise['unit']
        day = exercise['day']
        name = exercise['name']
        is_accessory = exercise['reg']
        ceil = 2.5
        if exercise.get('ceil') is not None:
            ceil = exercise['ceil']
        elif ceil == 'lbs':
            ceil = 5
        bw = 0
        if (exercise.get('bw') is not None):
            bw = exercise['bw']
        ratio = 0.65
        increase = 0.1
        weeks_reps = [[5, 5, 5], [3, 3, 3], [5, 3, 1]]
        rm = rm + bw
        rm = rm * .9
        for i in range(3):
            for j in range(3):
                load = ceil_to_increment(rm * (ratio + increase * j) - bw, ceil)
                week_rep = str(weeks_reps[i][j])
                if j == 2:
                    week_rep = week_rep + '+'
                plan.append({'sets': '1', 'reps': week_rep,
                             'load': load, 'week': (i + 1), 'name': name,
                             'unit': unit, 'day': day, 'reg': is_accessory})
            ratio = ratio + 0.05

    return plan
