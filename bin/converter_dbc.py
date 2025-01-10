import os
import pandas as pd
from dbfread import DBF

# Caminhos das pastas
input_folder = "./dados/DBC"  # Ajuste para o caminho da sua pasta de arquivos .dbc
output_file = "./dados/saida.csv"  # Local onde o arquivo consolidado será salvo

try:
    # Lista para armazenar os DataFrames
    dataframes = []

    # Itera sobre os arquivos na pasta
    for filename in os.listdir(input_folder):
        if filename.endswith(".dbc"):
            file_path = os.path.join(input_folder, filename)
            print(f"Convertendo arquivo: {file_path}")

            # Lê o arquivo .dbc diretamente com dbfread
            try:
                dbf = DBF(file_path, encoding="latin1")
                df = pd.DataFrame(iter(dbf))
                dataframes.append(df)
            except Exception as e:
                print(f"Erro ao processar {file_path}: {e}")

    # Concatena todos os DataFrames em um só
    if dataframes:
        final_df = pd.concat(dataframes, ignore_index=True)

        # Salva o DataFrame final em um arquivo CSV
        final_df.to_csv(output_file, index=False, encoding="utf-8")
        print(f"Arquivo CSV gerado com sucesso em: {output_file}")
    else:
        print("Nenhum arquivo .dbc foi processado com sucesso.")

except Exception as e:
    print(f"Erro durante a conversão: {e}")
