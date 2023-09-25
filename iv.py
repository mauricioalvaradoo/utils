import pandas as pd
import numpy as np


''' Information Value (IV) '''
''' Estimación de poder predictivo de cada feature dentro de un dataset '''
''' Estimado en base a las distribuciones de non-events (0) y events (1) 
    de una variable target a través los cortes de los feautres '''


def get_iv(data, target, listvars, cuts=5):
    ''' Estimar IV de variable categórica o numérica

    Parameters
    ----------
    data : pd.DataFrame
        Tabla.
    target : str
        Nombre de variable target. Valores: (0/1). Default: event = 1
    list_vars: list
        Lista de 'features' a la cual estimar su IV.
    cuts: int
        Cortes que se aplican a 'features' numéricas. Default: 5. 
    
    Returns
    -------
    store_iv_stat : dict
        Almacenamiento de los IV estimados para cada 'feature'.
    store_iv_tables : dict
        Almacenamiento de los IV estimados por corte dentro de cada 'feature'.

    '''
    
    df = data.copy()
    
    # Set target format
    if df[target].dtype == 'int':
        pass
    else:
        df[target].astype('int')
    
    # Set features format
    for v in listvars:
        if (df[v].dtype == 'int64') or (df[v].dtype == 'float'):
            try:
                df[v] = pd.qcut(df[v], cuts, duplicates='drop')
            except:
                print(f'La variable {v} no se pudo generar rangos')
        else:
            pass
    
    
    store_iv_stat   = {}
    store_iv_tables = {}
    
    # Table IV
    for v in listvars:
        
        total      = pd.DataFrame(df[v].value_counts())
        non_events = pd.DataFrame(df[df[target]==0][v].value_counts())
        events     = pd.DataFrame(df[df[target]==1][v].value_counts())

        total.columns.values[0] = 'count'
        non_events.columns.values[0] = 'non-event'
        events.columns.values[0] = 'event'
    
        iv_table = pd.merge(pd.merge(total, non_events, left_index=True, right_index=True),
                      events, left_index=True, right_index = True)
        
        iv_table['% non-event'] = iv_table['non-event']/iv_table['non-event'].sum()
        iv_table['% event']     = iv_table['event']/iv_table['event'].sum()
        iv_table['woe']         = np.log(iv_table['% non-event']/iv_table['% event'])
        iv_table['iv']          = (iv_table['% non-event']-iv_table['% event'])*iv_table['woe']
        
        iv = iv_table['iv'].sum()
        
        iv_table.sort_index(inplace=True)
        iv_table = iv_table.reset_index()
        
        # Storage
        store_iv_stat[v] = iv
        store_iv_tables[v] = iv_table
    
    
    return store_iv_stat, store_iv_tables



# Testing
df = pd.read_csv('Objetos/UCI_Credit_Card.csv')

features = [
    'LIMIT_BAL',
    'SEX',
    'EDUCATION',
    'MARRIAGE',
    'AGE',
    'PAY_0',
    'PAY_2',
    'PAY_3',
    'PAY_4',
    'PAY_5',
    'PAY_6',
    'BILL_AMT1',
    'BILL_AMT2',
    'BILL_AMT3',
    'BILL_AMT4',
    'BILL_AMT5',
    'BILL_AMT6',
    'PAY_AMT1',
    'PAY_AMT2',
    'PAY_AMT3',
    'PAY_AMT4',
    'PAY_AMT5',
    'PAY_AMT6'
]

target = 'default.payment.next.month'


ivs, ivstab = get_iv(
    data=df,
    target=target,
    listvars=features,
    cuts=5
)

print(ivs)
print(ivstab['AGE'])