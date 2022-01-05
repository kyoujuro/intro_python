import pubchempy as pcp

properties = ['MolecularFormula', 'MolecularWeight', 'CanonicalSMILES', 'IUPACName']

result = pcp.get_properties(properties, '64-14-5', 'name')

print(result)