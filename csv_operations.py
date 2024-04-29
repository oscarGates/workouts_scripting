import csv

def createCsv(grupos):
    with open('routines/output.csv', 'w', newline='', encoding='utf-8') as file:
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
    with open('routines/output.csv', 'w', newline='', encoding='utf-8') as file:
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
