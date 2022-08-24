# mysoftware

## Motivation

Short description of
- problem in field (e.g. cancer)
- what is current solution (handdrawn segmentation)
- what this software does to solve it (sota segmentation)
- proposed impact (accelerated/accurate diagnosis)
![](images/motivation.png)

## Status
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/bencardoen/SubPrecisionContactDetection.jl/tree/main.svg?style=svg&circle-token=d2c0a7c1eee273587c424008dc38e74692253787)](FIXME) [![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
## Installation
### Local
```bash
git clone <thisrepo>
# build instructions
```
#### Pip
```bash
pip install mysoftware
```
#### Conda
```bash
conda install mysoftware
```
### Container
#### Singularity
##### Building from recipes
```bash
sudo singularity build container/singularityrecipe.def
```
##### Released images
```bash
singularity pull repo:image.version
```
## Test
To run the tests ensuring the installation is valid, please run
```
python mysoftware/modulextest.py
```



## Usage
### Example snippets
Example inference on in silico data

```python
import seaborn as sns
import mysoftware.preprocessing as stk
import numpy as np
np.random.seed(42)
silico_data = stk.generate_insilico(args)
q = stk.infer(silico_data)
sns.boxplot(x='method', y='accuracy', data=q)
```

### Notebooks
See [notebooks/example.ipynb](notebooks/example.ipynb) for an example interactive workflow.

### API

See TODO for the complete API documentation

### Cite
```bibtext
[your citation here]
```

### Reproducing our published results
#### Data
##### In silico
See [mysoftware/insilico] on how to generate our in silico datasets.
For your convenience, this can be downloaded as well:
```bash
mkdir insilico && cd insilico
wget -O insilico.hdf5 https://mydatarepo/insilico.hdf5
```

##### Real world
```bash
mkdir mydata
wget -O dataset.hdf5 https://mydatarepo/dataset.hdf5
```
Ensure the checksums match
```bash
md5sum dataset.hdf5
```
should produce
```bash
4a4f224c7b7c871855fd307ae323be93 dataset.hdf5
```

#### Pre/post processing code
See [scripts/preprocessing.py](scripts/preprocessing.py) for the preprocessing scripts that configure the dataset and generate the plots

### FAQ
#### Help I can't figure out how function5 works
Please create a [new issue](https://github.com/bencardoen/mial-hamarneh-repository-template/issues/new/choose) detailing concisely, yet complete what issue you encountered, in a reproducible way.
