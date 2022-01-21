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

m = Chem.MolFromSmiles('CC(C)CC')
view = rdMolDraw2D.MolDraw2DSVG(300, 300)
option = view.drawOptions()
option.addAtomIndices=True
view.DrawMolecule(m)
view.FinishDrawing()
svg = view.GetDrawingText()
SVG(svg)
molecule = Chem.MolFromSmiles('CC(N)CCCCC')
Chem.MolToMolBlock(molecule)


Draw.MolsToGridImage(mols[:10], molsPerRow=5, subImgSize=(200,200))

m = Chem.MolFromSmiles('C1=C(N=C(C(=O)N1)C(=O)N)CN')
view = rdMolDraw2D.MolDraw2DSVG(300, 300)
option = view.drawOptions()
option.addAtomIndices=True
view.DrawMolecule(m)
view.FinishDrawing()
svg = view.GetDrawingText()
SVG(svg)

m = Chem.MolFromSmiles('OCC3OC(OCC2OC(OC(C#N)c1ccccc1)C(O)C(O)C2O)C(O)C(O)C3O ')
Draw.MolToFile(m, 'Chem1.png')