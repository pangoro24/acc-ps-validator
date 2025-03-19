import csv

# Nombres de los archivos
input_csv = "input.csv"  # Reemplázalo con el nombre real de tu archivo CSV
output_txt = "output.txt"

# Abrir el archivo CSV y procesarlo
with open(input_csv, mode="r", encoding="utf-8") as csv_file, open(output_txt, mode="w", encoding="utf-8") as txt_file:
    reader = csv.reader(csv_file)
    headers = next(reader)  # Leer la primera fila como encabezados
    
    # Índices de las columnas basados en los headers
    account_name_index = headers.index("AccountName")
    new_permission_set_index = headers.index("NewPermission set")

    # Iterar sobre cada fila del CSV
    for row_number, row in enumerate(reader, start=2):  # Comienza desde la segunda línea del archivo (después de headers)
        account_name = row[account_name_index].strip()
        permission_set = row[new_permission_set_index].strip()

        # Verificar condiciones
        if (account_name.startswith("0") or account_name.startswith("5")) and permission_set.endswith("-Dev"):
            txt_file.write(f"{row_number}, {account_name}, {permission_set}\n")

print(f"Archivo '{output_txt}' generado con éxito.")
