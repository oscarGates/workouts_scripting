from program_calculator.five_three_one import five_three_one
from program_calculator.operations.csv_operations import createCsvXlsFormat
from program_calculator.operations.sheet_convertions import toXlsx
from program_calculator.twelve_weeks_program import twelve_weeks_strength

exercises = [
    {'name': 'pull ups', 'rm': 42.5, 'unit': 'kg', 'bw': 85, 'day': 2, 'reg': True},
    {'name': 'one arm row', 'sets': 4, 'unit': 'kg', 'day': 2, 'reg': False, 'ceil': 5},
    {'name': 'one arm lat pull down', 'bw': 85, 'day': 2, 'reg': False},
    {'name': 'preacher curl', 'bw': 85, 'day': 2, 'reg': False},
    {'name': 'reverse curl', 'bw': 85, 'day': 2, 'reg': False},

    {'name': 'over head press', 'rm': 175, 'unit': 'lbs', 'day': 1, 'reg': True, 'ceil': 5},
    {'name': 'lateral raises', 'sets': 4, 'bw': 85, 'day': 1, 'reg': False},
    {'name': 'dumbbell press', 'bw': 85, 'day': 1, 'reg': False},
    {'name': 'one arm over head press', 'bw': 85, 'day': 1, 'reg': False},
    {'name': 'shoulder rotation', 'bw': 85, 'day': 1, 'reg': False},

    {'name': 'dips', 'rm': 75, 'unit': 'kg', 'bw': 85, 'day': 4, 'reg': True},
    {'name': 'bench press', 'sets': 4, 'unit': 'kg', 'day': 4, 'reg': False},
    {'name': 'dumbbell press', 'bw': 85, 'day': 4, 'reg': False},
    {'name': 'triceps extension', 'bw': 85, 'day': 4, 'reg': False},
    {'name': 'face pulls', 'bw': 85, 'day': 4, 'reg': False},

    {'name': 'squat', 'rm': 225, 'unit': 'lbs', 'day': 3, 'reg': True, 'ceil': 5},
    {'name': 'bulgarian', 'sets': 5, 'unit': 'kg', 'day': 3, 'reg': False, 'ceil': 5},
    {'name': 'barbell romanian dead lift', 'unit': 'kg', 'day': 3, 'reg': False, 'ceil': 5},
    {'name': 'hamstring curls', 'bw': 85, 'day': 3, 'reg': False},

]

exercises_2 = [
    {'name': 'pull ups', 'rm': 0, 'unit': 'lbs', 'bw': 110, 'day': 1, 'reg': True, 'ceil': 5},
    {'name': 'barbel row', 'day': 1, 'reg': False, 'ceil': 5},
    {'name': 'biceps curl', 'bw': 85, 'day': 1, 'reg': False},
    {'name': 'running', 'day': 1, 'reg': False},

    {'name': 'dips', 'rm': 45, 'unit': 'lbs', 'bw': 121, 'day': 3, 'reg': True, "ceil": 5},
    {'name': 'bench press', 'day': 3, 'reg': False},
    {'name': 'tricep extension', 'day': 3, 'reg': False},
    {'name': 'face pulls', 'day': 3, 'reg': False},
    {'name': 'running', 'day': 3, 'reg': False},

    {'name': 'squat', 'rm': 62.5, 'unit': 'kg', 'day': 2, 'reg': True, 'ceil': 2.5},
    {'name': 'hip thrust', 'unit': 'kg', 'day': 2, 'reg': False, 'ceil': 5},
    {'name': 'hamstring curls', 'day': 2, 'reg': False},
    {'name': 'plank', 'day': 2, 'reg': False},

    {'name': 'leg press', 'rm': 210, 'unit': 'kg', 'day': 4, 'reg': True, 'ceil': 10},
    {'name': 'hip thrust', 'unit': 'kg', 'day': 4, 'reg': False, 'ceil': 5},
    {'name': 'hip extension', 'day': 4, 'reg': False},
    {'name': 'plank', 'day': 4, 'reg': False},
]


if __name__ == '__main__':
    grupos = twelve_weeks_strength(exercises)
    createCsvXlsFormat(grupos)
    toXlsx()
