import pubchempy as pcp
import pandas as pd
properties = ['MolecularFormula', 'MolecularWeight', 'CanonicalSMILES', 'IUPACName']

result = pcp.get_properties(properties, '64-14-5', 'name')
properties = ['MolecularFormula','CanonicalSMILES', 'IUPACName']
cas_list = ['100-21','1002-62','1002-15-6']

print(result)
df = pd.DataFrame()
for cas in cas_list:
    try:
        temp = pcp.get_properties(properties, cas, 'name',as_dataframe=True)
        temp['CAS'] = cas
        df = pd.concat([df,temp],axis=0,join='outer',sort=True)
    except:
        pass