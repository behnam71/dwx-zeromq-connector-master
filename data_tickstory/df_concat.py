import pandas as pd
import datetime
import os
import glob

Dir_Path = 'C:\\Users\\Administrator\\Documents\\M1\\forex_data'



def FileName(path):
    os.chdir(path)
    result = glob.glob('*.csv')
    return result

_result = FileName(Dir_Path)
_HIST_DATA_DF = pd.DataFrame()
_S = 0
for i in range(0, len(_result)):
    _df = pd.read_csv(_result[i], sep=',', low_memory=False)
    _F = _S + len(_df)
    _HIST_DATA_DF = _HIST_DATA_DF.append(_df)
    _HIST_DATA_DF = _HIST_DATA_DF.reset_index(drop=True)
    _HIST_DATA_DF.loc[_S:_F, "tic"] = _result[i].split(".")[0]
    _S += len(_df)

for i in range(0, len(_HIST_DATA_DF)):
    _HIST_DATA_DF.loc[i, 'date'] = datetime.datetime.strptime(_HIST_DATA_DF.loc[i, "date"], '%Y%m%d %H:%M:%S')
    _HIST_DATA_DF.loc[i, 'volume'] = '{:.1f}'.format(int(_HIST_DATA_DF.loc[i, 'volume']))

_HIST_DATA_DF = _HIST_DATA_DF.sort_values(by=['date','tic']).reset_index(drop=True)

_HIST_DATA_DF.to_csv("file.csv", float_format='%6.5f')
print(_HIST_DATA_DF)
