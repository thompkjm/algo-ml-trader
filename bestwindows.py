import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/thompkjm/algo-ml-trader/josh/resources/6mo%20of%2030min%20eur%20usd.csv"
data=pd.read_csv(url,index_col='Date',parse_dates=True,infer_datetime_format=True)

results = {"Small":[],"Big":[],"Profit":[]};
for small in range(1,100):
    for big in range(2,252):
        data['short_window']=data["Last Price"].rolling(small).mean()
        data['long_window']=data["Last Price"].rolling(big).mean()
        data["signal"]=np.where(data["short_window"]>data["long_window"],1,0)
        data["signal"]=data["signal"].diff()
        onlytrades=data[data['signal'].isin([1,-1])].reset_index()
        pnl=pd.DataFrame()
        maxpnl= []
        bestexitidx=[]
        for i in range(len(onlytrades['Date'])):
            try:
                attempt=data.loc[onlytrades['Date'][i]:onlytrades['Date'][i+1]]
                signal=float(attempt['signal'][0:1])
                if signal == 1:
                    attempt['PNL']=attempt['Last Price'][1:]-float(attempt['Last Price'][0:1])
                else:
                    attempt['PNL']=float(attempt['Last Price'][0:1])-attempt['Last Price'][1:]
                max=attempt['PNL'].max()
                bestexitindex=attempt['PNL'].idxmax()
                bestexitidx.append(bestexitindex)
                maxpnl.append(max)
                pnl=pd.concat([pnl,attempt])
                pnl=pnl.drop(columns=['short_window','long_window'])
            except:
                maxpnl.append(0)
                bestexitidx.append(0)
        onlytrades['best_pnl'] = maxpnl
        onlytrades['best_exit']=bestexitidx
        tradestaken=onlytrades[onlytrades['best_pnl']>=0]
        entry=[]
        for index, row in tradestaken.iterrows():
            try:
                trade=data.loc[row['Date']:row['best_exit']]
                signal=float(trade['signal'][0:1])
                if signal == 1:
                    trade['PNL']=trade['Last Price'][1:]-float(trade['Last Price'][0:1])
                else:
                    trade['PNL']=float(trade['Last Price'][0:1])-trade['Last Price'][1:]
                entry.append((trade['PNL'].idxmin()))
            except:
                entry.append(0)
        tradestaken['best_entry']=entry
        returns=[]
        for index, row in tradestaken.iterrows():
            try:
                trade=data.loc[row['best_entry']:row['best_exit']]
                signal=float(row['signal'])
                if signal == 1:
                    trade['PNL']=trade['Last Price'][1:]-float(trade['Last Price'][0:1])
                else:
                    trade['PNL']=float(trade['Last Price'][0:1])-trade['Last Price'][1:]
                cumureturns=float(trade[-1:]['PNL'])
                returns.append(cumureturns)
            except:
                entry.append(0)
                returns.append(0)
        tradestaken['Profit']=returns
        total=tradestaken['Profit'].sum()
        results['Small'].append(small)
        results['Big'].append(big)
        results['Profit'].append(total)


output=pd.DataFrame(results)
output.to_csv('results.csv')