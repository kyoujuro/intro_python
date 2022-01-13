from rdkit import rdBase, Chem
from rdkit.Chem import AllChem, Draw
from rdkit.Chem.Draw import IPythonConsole, rdMolDraw2D
from IPython.display import SVG

from matplotlib.colors import ColorConverter
import numpy as np
print('rdkit: ', rdBase.rdkitVersion)
print('numpy: ', np.__version__)
mol = Chem.MolFromSmiles('CC(C)CCC')
print(Chem.GetAdjacencyMatrix(mol))
print(Chem.GetDistanceMatrix(mol))