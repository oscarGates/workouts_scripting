from twelve_weeks_program.operations.exercise_calculations import ceil_to_increment, calculate_plan_strength, \
    group_exercises
from twelve_weeks_program.operations.csv_operations import createCsvXlsFormat
from twelve_weeks_program.operations.sheet_convertions import toXlsx

exercises = [
    {'name': 'pull ups', 'rm': 37.5, 'unit': 'kg', 'bw': 85, 'day': 2, 'reg': True},
    {'name': 'one arm row', 'sets': 4, 'unit': 'kg', 'day': 2, 'reg': False, 'ceil': 5},
    {'name': 'one arm lat pull down', 'bw': 85, 'day': 2, 'reg': False},
    {'name': 'preacher curl', 'bw': 85, 'day': 2, 'reg': False},
    {'name': 'reverse curl', 'bw': 85, 'day': 2, 'reg': False},

    {'name': 'over head press', 'rm': 165, 'unit': 'lbs', 'day': 1, 'reg': True, 'ceil': 5},
    {'name': 'lateral raises', 'sets': 4, 'bw': 85, 'day': 1, 'reg': False},
    {'name': 'dumbbell press', 'bw': 85, 'day': 1, 'reg': False},
    {'name': 'one arm over head press', 'bw': 85, 'day': 1, 'reg': False},
    {'name': 'shoulder rotation', 'bw': 85, 'day': 1, 'reg': False},

    {'name': 'dips', 'rm': 72, 'unit': 'kg', 'bw': 85, 'day': 4, 'reg': True},
    {'name': 'bench press', 'sets': 4, 'unit': 'kg', 'day': 4, 'reg': False},
    {'name': 'dumbbell press', 'bw': 85, 'day': 4, 'reg': False},
    {'name': 'triceps extension', 'bw': 85, 'day': 4, 'reg': False},
    {'name': 'face pulls', 'bw': 85, 'day': 4, 'reg': False},

    {'name': 'squat', 'rm': 210, 'unit': 'lbs', 'day': 3, 'reg': True, 'ceil': 5},
    {'name': 'bulgarian', 'sets': 5, 'unit': 'kg', 'day': 3, 'reg': False, 'ceil': 5},
    {'name': 'barbell romanian dead lift', 'unit': 'kg', 'day': 3, 'reg': False, 'ceil': 5},
    {'name': 'hamstring curls', 'bw': 85, 'day': 3, 'reg': False},
]

exercises_2 = [
    {'name': 'pull ups', 'rm': 12, 'unit': 'lbs', 'bw': 121, 'day': 1, 'reg': True, 'ceil': 5},
    {'name': 'barbel row', 'day': 1, 'reg': False, 'ceil': 5},
    {'name': 'biceps curl', 'bw': 85, 'day': 1, 'reg': False},
    {'name': 'running', 'day': 1, 'reg': False},

    {'name': 'dips', 'rm': 25, 'unit': 'lbs', 'bw': 121, 'day': 3, 'reg': True, "ceil": 5},
    {'name': 'bench press', 'day': 3, 'reg': False},
    {'name': 'tricep extension', 'day': 3, 'reg': False},
    {'name': 'face pulls', 'day': 3, 'reg': False},
    {'name': 'running', 'day': 3, 'reg': False},

    {'name': 'squat', 'rm': 65.0, 'unit': 'kg', 'day': 2, 'reg': True, 'ceil': 2.5},
    {'name': 'hip thrust', 'unit': 'kg', 'day': 2, 'reg': False, 'ceil': 5},
    {'name': 'hamstring curls', 'day': 2, 'reg': False},
    {'name': 'plank', 'day': 2, 'reg': False},

    {'name': 'leg press', 'rm': 180, 'unit': 'kg', 'day': 4, 'reg': True, 'ceil': 10},
    {'name': 'hip thrust', 'unit': 'kg', 'day': 4, 'reg': False, 'ceil': 5},
    {'name': 'hip extension', 'day': 4, 'reg': False},
    {'name': 'plank', 'day': 4, 'reg': False},
]


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


def twelve_weeks_strength(exercises):
    weeks_reps = [12, 10, 8, 8, 6, 5, 4, 4, 3, 2, 1, 1]
    weeks_load = [0.6, 0.65, 0.7, 0.65, 0.75, 0.8, 0.85, 0.8, 0.88, 0.92, 1, 0.9]
    weeks_load_access = [0.6, 0.6, 0.6, 0.6, 0.65, 0.65, 0.65, 0.65, 0.7, 0.7, 0.7, 0.7]
    weeks_sets = [4, 4, 4, 3, 4, 4, 4, 3, 3, 3, 1, 3]
    has_plus_set = [True, True, True, False, True, True, True, False, False, False, True, False]
    plan = []
    for exercise in exercises:
        plan.extend(
            calculate_plan_strength(exercise, weeks_reps, weeks_load, weeks_load_access, weeks_sets, has_plus_set, 2.5))
    grupos = group_exercises(plan)
    createCsvXlsFormat(grupos)


# Guardar el archivo
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    twelve_weeks_strength(exercises)
    toXlsx()
