import os
from subprocess import call
from os import path

# Executables
executable = 'python'

# Paths
srcdir = '../..'
scriptname = 'run_avae.py'
cwd = os.path.dirname(os.path.abspath(__file__))
outdir = cwd
rootdir = srcdir

# Arguments
args = [
# Architecture
'--is-train',
'--image-size', '128',
'--output-size', '64',
'--c-dim', '3',
'--z-dim', '64',
'--z-dist', 'gauss',
'--cond-dist', 'gauss',
'--eps-dim', '128',
'--eps-nbasis', '32',
'--encoder', 'conv0',
'--decoder', 'conv0',
'--adversary', 'conv1',
'--is-01-range',
#'--is-ac',
# Training
'--nsteps', '2500000',
'--ntest', '100',
"--learning-rate", "1e-5",
"--learning-rate-adversary", "1e-4",
'--batch-size', '64',
'--log-dir', os.path.join(outdir, 'logs'),
'--sample-dir', os.path.join(outdir, 'samples'),
# Data set
'--dataset', 'celebA',
'--data-dir', 'datasets',
'--split-dir', 'datasets/splits',
# Test
'--eval-dir', os.path.join(outdir, 'eval'),
'--test-nite', '0',
'--test-nais', '20',
'--test-ais-nsteps', '2000', 
'--test-ais-nchains', '8',
'--test-ais-eps', '1e-2',
'--test-is-center-posterior',
]

# Set environment variables here
my_env = os.environ.copy()
# Run
call([executable, scriptname] + args, env=my_env, cwd=rootdir)

