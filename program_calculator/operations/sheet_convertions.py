import pandas as pd

def toXlsx():
    # Paso 1: Leer el archivo CSV
    # Paso 2: Crear un archivo Excel
    with pd.ExcelWriter('../routines/rutina.xlsx', engine='xlsxwriter') as writer:
        df = pd.read_csv('../routines/output.csv')

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

        # Guardar cada segmento en una hoja de cálculo
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
    worksheet.set_column('C:C', 22)
    worksheet.set_column('D:D', 10)
    worksheet.set_column('F:F', 30)

    for i, row in df_modificado.iterrows():
        worksheet.set_row(i + 1, 20)


    formato = workbook.add_format({
        'border': 1,  # Grosor del borde (1 es el valor predeterminado)
        'border_color': 'black',  # Color del borde
        'text_wrap': True,  # Ajuste de texto
        'valign': 'vcenter',  # Alineación vertical
        'align': 'center'  # Alineación horizontal
    })

    num_rows, num_cols = df_modificado.shape
    for row in range(num_rows):
        for col in range(num_cols):
            value = df_modificado.iloc[row, col]
            if pd.isna(value):
                value = ''
            if filas_vacias.iloc[row]:
                worksheet.write(row + 1, col, ' ')
            else:
                if col < num_cols :
                    worksheet.write(row + 1, col, value, formato)
                else:
                    worksheet.write(row + 1, col, value)
