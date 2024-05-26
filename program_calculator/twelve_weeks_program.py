from program_calculator.operations.exercise_calculations import ceil_to_increment, calculate_plan_strength, \
    group_exercises


def twelve_weeks_strength(exercises):
    plan = []
    for exercise in exercises:
        plan.extend(
            calculate_plan_strength(exercise, 2.5))
    return group_exercises(plan)
