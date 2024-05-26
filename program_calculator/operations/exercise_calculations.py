import math
from collections import defaultdict

weeks_reps = [12, 10, 8, 8, 6, 5, 4, 4, 3, 2, 1, 1]
weeks_load = [0.6, 0.65, 0.7, 0.65, 0.75, 0.8, 0.85, 0.8, 0.88, 0.92, 1, 0.9]
weeks_load_access = [0.6, 0.6, 0.6, 0.6, 0.65, 0.65, 0.65, 0.65, 0.7, 0.7, 0.7, 0.7]
weeks_sets = [4, 4, 4, 3, 4, 4, 4, 3, 3, 3, 1, 3]
has_plus_set = [True, True, True, False, True, True, True, False, False, False, True, False]


def ceil_to_increment(number, increment):
    cil = math.ceil(number / increment) * increment
    flr = math.floor(number / increment) * increment
    if abs(number - cil) < abs(number - flr):
        return cil
    else:
        return flr


def calculate_nRM(one_rm, n):
    percentages = {1: 100, 2: 95, 3: 93, 4: 90, 5: 87, 6: 85, 7: 83, 8: 80, 9: 77, 10: 75, 11: 73, 12: 71, 13: 70,
                   14: 68, 15: 67}
    return one_rm * (percentages.get(n, 75) / 100)


def calculate_load_strength(rm, bw, weeks_load, ceil):
    return ceil_to_increment((rm + bw) * weeks_load - bw, ceil)


def calculate_plan_strength(exercise, ceil):
    weeks_reps_access = ['12-15', '12-15', '12-15', '12-15', '8-12', '8-12', '8-12', '8-12', '5-8', '5-8', '5-8', '5-8']
    plan = []
    rm = 0
    if exercise.get('rm') is not None:
        rm = exercise['rm']
    if exercise.get('unit') is not None:
        unit = exercise['unit']
    day = exercise['day']
    name = exercise['name']
    is_accessory = exercise['reg']
    if exercise.get('ceil') is not None:
        ceil = exercise['ceil']
    bw = 0
    if (exercise.get('bw') is not None):
        bw = exercise['bw']
    sets = '3-4'
    if exercise.get('sets') is not None:
        sets = exercise['sets']
    for i in range(12):
        if not is_accessory and rm != 0:
            load = calculate_load_strength(rm, bw, weeks_load_access[i], ceil)
            plan.append(
                {'sets': sets, 'reps': weeks_reps_access[i], 'load': load, 'unit': unit, 'name': name, 'week': (i + 1),
                 'day': day, 'reg': is_accessory})
            continue
        if not is_accessory:
            plan.append({'sets': sets, 'reps': weeks_reps_access[i], 'name': name, 'week': (i + 1), 'day': day,
                         'reg': is_accessory})
            continue
        if i == 10:
            load = calculate_load_strength(rm, bw, .8, ceil)
            plan.append({'sets': str(weeks_sets[i]), 'reps': weeks_reps[i], 'load': load, 'name': name, 'week': (i + 1),
                         'unit': unit, 'day': day, 'reg': is_accessory})
            load = calculate_load_strength(rm, bw, .9, ceil)
            plan.append({'sets': str(weeks_sets[i]), 'reps': weeks_reps[i], 'load': load, 'name': name, 'week': (i + 1),
                         'unit': unit, 'day': day, 'reg': is_accessory})
        load = calculate_load_strength(rm, bw, weeks_load[i], ceil)
        plan.append({'sets': str(weeks_sets[i]), 'reps': weeks_reps[i], 'load': load, 'week': (i + 1), 'name': name,
                     'unit': unit, 'day': day, 'reg': is_accessory})
        if has_plus_set[i]:
            plan.append({'sets': '1+', 'reps': weeks_reps[i], 'load': load, 'name': name, 'week': (i + 1), 'unit': unit,
                         'day': day, 'reg': is_accessory})
    return plan


def group_exercises(plan):
    grupos = defaultdict(list)
    for d in plan:
        clave = (d['week'], d['day'])
        grupos[clave].append(d)
    return dict(grupos)
