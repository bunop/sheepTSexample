# sheepTSexample

## Setup
1. (Optional) To run the simulation script, you need to set up [scrm](https://scrm.github.io/)
2. For the simulation script and data analysis, you need an environment with tsinfer and numpy, e.g. `conda create -n tsinfer -conda-forge tsinfer numpy ipython`

## Data
The is a simulated data set of 105 sheep (i.e. 210 haploid genomes) along 1Mbp of sequence:
* 5 mouflon
* 50 Iranian
* 50 Border

Demography (N - effective population size, sampled - number of diplopids sampled)
<img src="https://github.com/HighlanderLab/sheepTSexample/assets/10515056/270c1061-a9d5-464a-9627-ea30e962ee88" width=50%>

## VCF vs TS
Both files have the same variant data, but the TS is only half the size. This ratio becomes even more beneficial for larger data sets. The TS file also contains richer information (trees).
```
-rw------- 1 hbecher datastore_eb_groups_HighlanderLab_admin 2.5M Feb 20 11:58 test1M.out.inf.ts
-rw------- 1 hbecher datastore_eb_groups_HighlanderLab_admin 5.6M Feb 20 11:58 test1M.out.inf.vcf
```

## Analysing data in TS format
Open ipython, Jupyter notebook or similar
```
import tskit
# load the TS file
ts = tskit.load("test1M.out.inf.ts")

# how amny sample are there?
ts.num_samples

# samples 0 to 9 are mouflon genomes, 10 to 109 are Iranian, 110 to 209 are Border, mind the python indexing below
# compute nucleatide diversity in mouflon, Iranian, and Border
ts.diversity([range(10), range(10,110), range(110, 210)])

# Fst mouflon-Iranian
ts.Fst([range(10), range(10,110)])
> 0.0474287776006701

# Fst mouflon-Border
ts.Fst([range(10), range(110,210)])
> 0.3863240194680754

# Fst Iranian-Border
ts.Fst([range(10,110), range(110,210)])
> 0.344373582032233

# Based on gene trees and looking at the mouflon samples (first argument) who are the closest relatives (second argument = list of ranges)
ts.genealogical_nearest_neighbours(range(10), [range(10),range(10, 110), range(110, 210)])
> array([[0.59771033, 0.36771007, 0.0345796 ],
>        [0.48813082, 0.48295405, 0.02891513],
>        [0.51328397, 0.44918785, 0.03752818],
>        [0.74977978, 0.23451288, 0.01570734],
>        [0.63255684, 0.35004292, 0.01740025],
>        [0.48170299, 0.49188582, 0.02641118],
>        [0.51438889, 0.43455347, 0.05105764],
>        [0.65187813, 0.32764667, 0.0204752 ],
>        [0.46132971, 0.48903879, 0.0496315 ],
>        [0.60860476, 0.35239091, 0.03900433]])
# The columns are mouflon, Irania, Border
# The rows correspond to the mouflon genomes
# Mouflon genomes are most similar to mouflon, also simlar to Iranian, but very different to Border
# This is useful when there are unlabelled samples
```
See [here](https://tskit.dev/tskit/docs/stable/stats.html) for other stats and inspiration.
