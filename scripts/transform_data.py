from extract_and_save_data import connect_mongo, create_connect_db, create_connect_collection
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
print("Mongo URI:", os.getenv("MONGODB_URI"))
def visualize_collection(col):
    for i in col.find():
        print(i)

def rename_column(col, col_name, new_name):
    col.update_many({}, {'$rename': {f'{col_name}':f'{new_name}'}})

def select_category(col, category):
    query = {'Categoria do Produto': f'{category}'}
    lista_categoria = []

    for doc in col.find(query):
        lista_categoria.append(doc)

    return lista_categoria

def make_regex(col, regex):
    lista_produtos_regex = []

    for doc in col.find(regex):
        lista_produtos_regex.append(doc)
    
    return lista_produtos_regex

def create_dataframe(lista):
    df = pd.DataFrame(lista)
    return df

def format_date(df):
    df["Data da Compra"] = pd.to_datetime(df["Data da Compra"], format="%d/%m/%Y")
    df['Data da Compra'] = df['Data da Compra'].dt.strftime('%Y-%m-%d')

def save_csv(df, path):
    df.to_csv(f'{path}', index= False)
    print(f'O arquvi {path} foi salvo')


if __name__ == "__main__":
    client = connect_mongo(os.getenv("MONGODB_URI"))
    db = create_connect_db(client, "db_produtos_desafio_pt2")
    col = create_connect_collection(db, "produtos")
    visualize_collection(col)

    rename_column(col, 'lon', 'longitude')

    lst_categoria = select_category(col, 'brinquedos')

    regex = {'Data da Compra': {'$regex':'/2021'}}
    lst_regex = make_regex(col, regex)

    # Salvando csv categoria
    df_categoria = create_dataframe(lst_categoria)
    format_date(df_categoria)
    save_csv(df_categoria, '../data/csv_categoria.csv')

    #Salvando csv regex
    df_regex = create_dataframe(lst_regex)
    format_date(df_regex)
    save_csv(df_regex, '../data/csv_regex.csv')


    # Desliga conexão
    client.close()



