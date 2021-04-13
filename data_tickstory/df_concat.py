import pandas as pd
import datetime
import os
import glob

Dir_Path = 'C:\\Users\\BEHNAMH721AS.RN\\Documents'



def FileName(path):
    os.chdir(path)
    result = glob.glob('*.csv')
    return result

result = FileName(Dir_Path)
_start = 0
_HIST_DATA_DF = pd.DataFrame()
for i in range(0, len(result)):
	df = pd.read_csv(result[i], sep=',', low_memory=False)
	_HIST_DATA_DF = _HIST_DATA_DF.append(df)
	_HIST_DATA_DF = _HIST_DATA_DF.reset_index(drop=True)
	_HIST_DATA_DF.loc[_start:len(_HIST_DATA_DF), "tic"] = result[i].split(".")[0]
	_start += len(_HIST_DATA_DF)

for i in range(0, len(_HIST_DATA_DF)):
    _HIST_DATA_DF.loc[i, 'date'] = datetime.datetime.strptime(str(_HIST_DATA_DF.loc[i, "date"]), '%Y%m%d %H:%M:%S')
    _HIST_DATA_DF.loc[i, 'volume'] = '{:.1f}'.format(int(_HIST_DATA_DF.loc[i, 'volume']))

#_HIST_DATA_DF = _HIST_DATA_DF.sort_values(by=['date','tic']).reset_index(drop=True)

_HIST_DATA_DF.to_csv("file.csv", float_format='%6.5f')
print(_HIST_DATA_DF)


