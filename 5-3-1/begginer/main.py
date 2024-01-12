import pandas as pd


def create_531_for_beginners_template_corrected(max_lifts):
    """
    Corrected function to create a 5/3/1 for Beginners workout template using pd.concat.

    :param max_lifts: Dictionary with max lifts for squat, bench press, deadlift, and overhead press.
    :return: Pandas DataFrame representing the workout plan.
    """
    # Percentages for the 5/3/1 program
    percentages = [0.40, 0.50, 0.60, 0.65, 0.75, 0.85]

    # Workout days
    workouts = {
        "Day 1": ["pull up", "squat"],
        "Day 2": ["leg press", "dip"],
        "Day 3": ["squat", "pull up"]
    }

    # Create empty dataframe
    df = pd.DataFrame(columns=["Day", "Exercise", "Set", "Weight", "Reps"])
    rows = []

    for day, exercises in workouts.items():
        for exercise in exercises:
            max_weight = max_lifts.get(exercise.lower(), 0)
            for i, pct in enumerate(percentages):
                weight = max_weight * pct
                reps = 5 if i != 2 else 3  # 3 reps for the fourth set (90%)
                rows.append({
                    "Day": day,
                    "Exercise": exercise,
                    "Set": i + 1,
                    "Weight": round(weight, 2),
                    "Reps": reps
                })

            # Adding 5x5 FSL (First Set Last)
            fsl_weight = max_weight * percentages[3]  # 65% of RM

            rows.append({
                "Day": day,
                "Exercise": f"{exercise} 5x5 FSL",
                "Set": 5,
                "Weight": round(fsl_weight, 2),
                "Reps": 5
            })

    # Concatenate all rows to the dataframe
    df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)
    return df


# User's max lifts (example values)
max_lifts_example = {
    "squat": 80,
    "pull up": 130,
    "dip": 145,
    "overhead press": 75
}

if __name__ == '__main__':
    # Create the template
    template = create_531_for_beginners_template_corrected(max_lifts_example)
    csv_file_path = "531_for_beginners_workout_plan.csv"
    template.to_csv(csv_file_path, index=False)

    csv_file_path
    # Display the first 10 rows of the template
