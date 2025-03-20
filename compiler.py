import pandas as pd

# Cargar el archivo CSV de entrada
input_file = "input.csv"  # Reemplaza con el nombre de tu archivo
output_file = "output.csv"

# Leer el CSV
df = pd.read_csv(input_file, usecols=["UserName", "AccountName"])

# Crear la matriz de acceso
pivot_table = df.pivot_table(index="UserName", columns="AccountName", aggfunc=lambda x: "✔", fill_value="")

# Renombrar el índice
pivot_table.index.name = "user"

# Guardar el resultado en un nuevo archivo CSV
pivot_table.to_csv(output_file)

print(f"Archivo generado: {output_file}")
