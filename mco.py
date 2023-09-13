import pandas as pd
import numpy as np
from scipy.stats import t
from statsmodels.datasets import webuse
import warnings
warnings.filterwarnings('ignore')

''' Estimación por Mínimos Cuadrados Ordinarios (MCO) '''


def mco(y, X, const=True, alpha=0.05):
    
    '''
    Parameters
    ----------
    y: pd.Series
    X: pd.DataFrame
    const: bool
    alpha: int
    
    Returns
    ----------
    Beta: pd.DataFrame
    R2: float
    '''   
    
    if const:
        X['const'] = 1
    
    
    names = list(X.columns)
    y_name = y.name
    n, k  = X.shape
    
    
    X = np.asarray(X)
    y = np.asarray(y)
    
    Beta = np.linalg.inv(X.T @ X) @ (X.T @ y) # np.dot == @

    # Residuos
    y_hat  = X @ Beta
    resids = y - y_hat
    
    # Ajuste
    SSR = np.sum((y_hat - np.mean(y))**2)
    SST = np.sum((y     - np.mean(y))**2)
    R2 = SSR / SST

    # Varianza
    s2 = (resids.T @ resids) / (n-k)
    cov_Beta = s2 * np.linalg.inv(X.T @ X)
    V_Beta   = np.diagonal(cov_Beta)
    SD_Beta = np.sqrt(V_Beta)

    # p-value
    H0 = 0
    t_stats = (Beta-H0)/SD_Beta
    p_values = 2 * ( 1 - t.cdf( np.abs(t_stats), df=n-k ) )

    # Intervalos de confianza
    t_critico = t.ppf(1 - alpha / 2, df=n - k)
    conf_low = Beta - t_critico * SD_Beta
    conf_up  = Beta + t_critico * SD_Beta

    # Results
    df = pd.DataFrame(
        {
            y_name: names,
            'Coef.': np.round(Beta, 5),
            'Std. Err.': np.round(SD_Beta, 5),
            't': np.round(t_stats, 4),
            'P>|t|': np.round(p_values, 4),
            f'[{int((1-alpha)*100)}% Conf. Interval]':
                zip(np.round(conf_low, 5), np.round(conf_up, 5))
        }
    )
    
    df.set_index(y_name, inplace=True)

    return df, R2



# testing
df = webuse('auto')

y  = df['price']
X  = df[['mpg', 'headroom', 'displacement']]

df, R2 = mco(y, X)

print(df)
print('')
print('R-cuadrado:', np.round(R2, 4))

