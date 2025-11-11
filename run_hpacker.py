from hpacker import HPacker
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--pdb_file", type=str, help="PDB file to reconstruct sidechains of")
parser.add_argument("--num_refinement_iterations", type=int, help="Number of refinement iterations")
parser.add_argument("--output_file", type=str, help="Output PDB file")
args = parser.parse_args()

hpacker = HPacker(args.pdb_file) # backbone-only input
hpacker.reconstruct_sidechains(num_refinement_iterations=args.num_refinement_iterations)
hpacker.write_pdb(args.output_file) # output PDB with reconstructed sidechains