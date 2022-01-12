from rdkit import rdBase, Chem
from rdkit.Chem import AllChem, Draw, rdMolDescriptors
from rdkit.Chem.Draw import SimilarityMaps
print('rdkit version: ', rdBase.rdkitVersion)
import pubchempy as pcp
taxol = pcp.get_compounds('Paclitaxel', 'name')
taxol = taxol[0]
sm = taxol.canonical_smiles
taxol_mol = Chem.MolFromSmiles(sm)