import pandas as pd

exercises = [
    {'name': 'pull ups', 'rm': 37.5, 'unit': 'kg', 'bw': 85, 'day': 2, 'reg': True },
    {'name': 'one arm row', 'sets':4,'unit': 'kg', 'day': 2, 'reg': False, 'ceil':5},
    {'name': 'one arm lat pull down', 'bw': 85, 'day': 2, 'reg': False},
    {'name': 'preacher curl', 'bw': 85, 'day': 2, 'reg': False},
    {'name': 'reverse curl', 'bw': 85, 'day': 2, 'reg': False},

    {'name': 'over head press', 'rm': 165, 'unit': 'lbs',  'day': 1, 'reg': True, 'ceil':5},
    {'name': 'lateral raises', 'sets':4,'bw': 85, 'day': 1, 'reg': False},
    {'name': 'dumbbell press', 'bw': 85, 'day': 1, 'reg': False},
    {'name': 'one arm over head press', 'bw': 85, 'day': 1, 'reg': False},
    {'name': 'shoulder rotation', 'bw': 85, 'day': 1, 'reg': False},

    {'name': 'dips', 'rm': 67.5, 'unit': 'kg', 'bw': 85, 'day': 4, 'reg': True},
    {'name': 'bench press', 'sets':4, 'unit': 'kg', 'day': 4, 'reg': False},
    {'name': 'dumbbell press','bw': 85, 'day': 4, 'reg': False},
    {'name': 'triceps extension', 'bw': 85, 'day': 4, 'reg': False},
    {'name': 'face pulls', 'bw': 85, 'day':4, 'reg': False},

    {'name': 'squat', 'rm': 210, 'unit': 'lbs',  'day': 3, 'reg': True, 'ceil': 5},
    {'name': 'bulgarian', 'sets':5,'unit': 'kg', 'day': 3, 'reg': False, 'ceil': 5},
    {'name': 'barbell romanian dead lift', 'unit': 'kg', 'day': 3, 'reg': False, 'ceil':5},
    {'name': 'hamstring curls', 'bw': 85, 'day': 3, 'reg': False},
    ]
exercises_2 = [
    {'name': 'pull ups', 'rm': 12, 'unit': 'lbs', 'bw': 121, 'day': 1, 'reg': True, 'ceil':5},
    {'name': 'barbel row',  'day': 1, 'reg': False, 'ceil':5},
    {'name': 'biceps curl', 'bw': 85, 'day': 1, 'reg': False},
    {'name': 'running',  'day': 1, 'reg': False},

    {'name': 'dips', 'rm': 25, 'unit': 'lbs', 'bw': 121, 'day': 3, 'reg': True, "ceil":5},
    {'name': 'bench press', 'day': 3, 'reg': False},
    {'name': 'tricep extension', 'day': 3, 'reg': False},
    {'name': 'face pulls', 'day': 3, 'reg': False},
    {'name': 'running', 'day': 3, 'reg': False},

    {'name': 'squat', 'rm': 65.0, 'unit': 'kg', 'day': 2, 'reg': True, 'ceil': 2.5},
    {'name': 'hip thrust', 'unit': 'kg', 'day': 2, 'reg': False, 'ceil': 5},
    {'name': 'hamstring curls',  'day': 2, 'reg': False},
    {'name': 'plank', 'day': 2, 'reg': False},

    {'name': 'leg press', 'rm': 180, 'unit': 'kg', 'day': 4, 'reg': True, 'ceil': 10},
    {'name': 'hip thrust',  'unit': 'kg', 'day': 4, 'reg': False, 'ceil': 5},
    {'name': 'hip extension', 'day': 4, 'reg': False},
    {'name': 'plank','day': 4, 'reg': False},
]

import math
from collections import defaultdict
import csv


def ceil_to_increment(number, increment):
    cil = math.ceil(number / increment) * increment
    flr = math.floor(number / increment) * increment
    if abs(number - cil) < abs(number - flr):
        return cil
    else:
        return flr
    #return math.ceil(number / increment) * increment


def calculate_nRM(one_rm, n):
    percentages = {1: 100, 2: 95, 3: 93, 4: 90, 5: 87, 6: 85, 7: 83, 8: 80, 9: 77, 10: 75, 11: 73, 12: 71, 13: 70,
                   14: 68, 15: 67}
    return one_rm * (percentages.get(n, 75) / 100)


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
        weeks_reps=[[5, 5, 5], [3,3,3], [5,3,1]]
        rm = rm + bw
        rm = rm * .9
        for i in range(3):
            for j in range(3):
                load = ceil_to_increment(rm * (ratio + increase * j) - bw, ceil)
                week_rep = str(weeks_reps[i][j])
                if j == 2:
                    week_rep = week_rep +'+'
                plan.append({'sets': '1', 'reps': week_rep,
                             'load': load, 'week': (i + 1), 'name': name,
                             'unit': unit, 'day': day, 'reg': is_accessory})
            ratio = ratio + 0.05

    return plan


def twelve_weeks_strength(exercises):
    plan = []
    weeks_reps = [12, 10, 8, 8, 6, 5,4, 4, 3, 2, 1, 1]
    weeks_load = [0.6,0.65,0.7, 0.65,0.75, 0.8, 0.85, 0.8, 0.88, 0.92, 1, 0.9]
    weeks_load_access = [0.6,0.6,0.6, 0.6,0.65, 0.65, 0.65, 0.65, 0.7, 0.7, 0.7, 0.7]
    weeks_sets = [4, 4, 4,3,4,4,4,3, 3,3,1,3]
    weeks_reps_access = ['12-15', '12-15', '12-15', '12-15', '8-12', '8-12', '8-12', '8-12', '5-8', '5-8','5-8', '5-8']
    has_plus_set = [True, True, True, False, True, True, True,False, False, False, True, False]
    for exercise in exercises:
        rm = 0
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
        if(exercise.get('bw') is not None):
            bw = exercise['bw']

        sets = '3-4'
        if exercise.get('sets') is not None:
            sets = exercise['sets']

        for i in range(12):
            if not is_accessory and rm != 0:
                plan.append(
                    {'sets': sets, 'reps': weeks_reps_access[i], 'load': ceil_to_increment((rm+bw)*weeks_load_access[i]-bw, ceil), 'unit': unit,
                      'name': name, 'week': (i + 1),'day': day, 'reg': is_accessory})
                continue
            if not is_accessory:
                plan.append(
                    {'sets': sets, 'reps': weeks_reps_access[i],
                      'name': name, 'week': (i + 1),'day': day, 'reg': is_accessory})
                continue
            if i == 10:
                plan.append(
                    {'sets': str(weeks_sets[i]), 'reps': weeks_reps[i],
                     'load': ceil_to_increment((rm+bw) * .8-bw, ceil), 'name': name, 'week': (i + 1), 'unit': unit,
                     'day': day,  'reg': is_accessory})
                plan.append(
                    {'sets': str(weeks_sets[i]), 'reps': weeks_reps[i],
                     'load': ceil_to_increment((rm+bw) * .9-bw, ceil), 'name': name, 'week': (i + 1), 'unit': unit,
                     'day': day, 'reg': is_accessory})

            plan.append({'sets': str(weeks_sets[i]), 'reps': weeks_reps[i],
                         'load': ceil_to_increment((rm+bw)*weeks_load[i]-bw, ceil), 'week': (i + 1), 'name': name, 'unit': unit,'day': day, 'reg': is_accessory})

            if has_plus_set[i]:
                plan.append(
                    {'sets': '1+', 'reps': weeks_reps[i],
                     'load': ceil_to_increment((rm+bw) * weeks_load[i]-bw, ceil), 'name': name,'week': (i + 1), 'unit': unit,'day': day, 'reg': is_accessory})
    return plan

def createCsv(grupos):
    with open('output.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        old_week = 0
        # Escribir los datos
        for key in sorted(grupos):
            week = key[0]
            day = key[1]
            values = grupos[key]
            if (week != old_week):
                writer.writerow(['Week ' + str(week)])
                old_week = week

            writer.writerow(['Day ' + str(day)])
            for value in values:
                row = [value['name'], str(value['sets']) + 'x' + str(value['reps'])]
                if value.get('load'):
                    row.append(str(value['load']) + str(value['unit']))
                if value.get('bar_load') is not None:
                    row.append('load without bar')
                    row.append(str(value['bar_load']) + str(value['unit']))

                writer.writerow(row)

            writer.writerow([])
    print("Archivo CSV creado con éxito.")


def createCsvXlsFormat(grupos):
    with open('output.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['week', 'day', 'exercise', 'sets-reps', 'weight', 'comment'])

        old_week = 0
        h_set = set([])
        for key in sorted(grupos):
            week = key[0]
            day = key[1]
            values = grupos[key]
            if (week != old_week):
                old_week = week

            for value in values:
                row = ['','',value['name'], str(value['sets']) + 'x' + str(value['reps'])]
                if str(week)+","+str(day) not in h_set:
                    h_set.add(str(week)+","+str(day))
                    row = ['Week ' + str(week),'Day ' + str(day),value['name'], str(value['sets']) + 'x' + str(value['reps'])]

                if value.get('load'):
                    row.append(str(value['load']) + str(value['unit']))
                if value.get('bar_load') is not None:
                    row.append('load without bar')
                    row.append(str(value['bar_load']) + str(value['unit']))

                writer.writerow(row)

            writer.writerow([])
    print("Archivo CSV creado con éxito.")

def calculatePlan(mapExercises):
   # complete_plan = []
   # for exercise in mapExercises:
   #     complete_plan.append(calculateWeeks(exercise))
    plan_compresses = twelve_weeks_strength(mapExercises) #[objeto for sublista in complete_plan for objeto in sublista]


    grupos = defaultdict(list)

    for d in plan_compresses:
        clave = (d['week'], d['day'])
        grupos[clave].append(d)

    grupos = dict(grupos)
    createCsvXlsFormat(grupos)



def toXlsx():
    # Paso 1: Leer el archivo CSV
    # Paso 2: Crear un archivo Excel
    with pd.ExcelWriter('rutina.xlsx', engine='xlsxwriter') as writer:
        df = pd.read_csv('output.csv')

        # Definir el tamaño de cada segmento
        tamaño_segmento = 21
        sizes = []
        # Crear una lista para almacenar los DataFrames segmentados
        segmentos = []
        pos = []
        current = 1
        cnt = 0
        for index, row in df.iterrows():
            val = row['week']
            cnt+= 1
            if val == "Week " + str(current):
                current = current + 1
                pos.append(index)
        pos.append(cnt)
        for i in range(1, len(pos)):
            sizes.append(pos[i] - pos[i-1])
        i = 0
        # Dividir el DataFrame en segmentos
        inicio = 0
        for tamaño in sizes:
            fin = inicio + tamaño
            segmento_df = df[inicio:fin]
            segmentos.append(segmento_df)
            inicio = fin  # Actualizar el inicio para la próxima iteración

        # Verificar los segmentos creados


        for i, segmento in enumerate(segmentos):
            saveSheet(writer, segmento, "week "+str(i+1))
    writer._save()


def saveSheet(writer, df, sheet):
    df_modificado = pd.DataFrame(columns=df.columns)

    # Iterar a través del DataFrame original e insertar filas
    for index, row in df.iterrows():
        # Si se encuentra la cadena deseada, insertar una fila vacía
        if pd.notna(row['week']):
            df_modificado = df_modificado._append(pd.Series(), ignore_index=True)
            df_modificado = df_modificado._append(pd.Series([None] * 5 + ["comment"], index=df_modificado.columns),
                                                  ignore_index=True)
        df_modificado = df_modificado._append(row, ignore_index=True)

    filas_vacias = df_modificado.isna().all(axis=1)

    df_modificado.to_excel(writer, sheet_name=sheet, index=False, header=False)

    workbook = writer.book
    worksheet = writer.sheets[sheet]
    worksheet.set_column('C:C', 22)  # Establecer el ancho de la Columna1 a 20
    worksheet.set_column('D:D', 10)
    worksheet.set_column('F:F', 30)

    formato = workbook.add_format({
        'border': 1,  # Grosor del borde (1 es el valor predeterminado)
        'border_color': 'black',  # Color del borde
        'text_wrap': True,  # Ajuste de texto
        'valign': 'vcenter',  # Alineación vertical
        'align': 'center'  # Alineación horizontal
    })

    num_rows, num_cols = df_modificado.shape
    cnt = 0
    for row in range(num_rows):
        for col in range(num_cols):
            value = df_modificado.iloc[row, col]
            if pd.isna(value):
                value = ''  # Reemplazar NaN con un string vacío o el valor que prefieras

            if filas_vacias.iloc[row]:
                # Si la fila está vacía, escribe sin formato

                worksheet.write(row + 1, col, ' ')
            else:
                worksheet.write(row + 1, col, value, formato)


# Guardar el archivo
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculatePlan(exercises_2)
    toXlsx()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


