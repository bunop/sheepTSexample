# sheepTSexample

# Setup
1. To run the simulation script (not required) you need to set up [scrm](https://scrm.github.io/)
2. For the simulation script and data analysis, you need an environment with tsinfer and numpy, e.g. `conda create -n tsinfer -conda-forge tsinfer numpy ipython`

# Data
The is a simulated data set of 105 sheep (i.e. 210 haploid genomes):
* 5 mouflon
* 50 Iranian
* 50 Border

Demography (N - effective population size, sampled - number of diplopids sampled)
<img src="https://github.com/HighlanderLab/sheepTSexample/assets/10515056/270c1061-a9d5-464a-9627-ea30e962ee88" width=50%>

# VCF vs TS
Both files have the same variant data, but the TS is only half the size. The TS file also contains richer information (trees).
```
-rw------- 1 hbecher datastore_eb_groups_HighlanderLab_admin 2.5M Feb 20 11:58 test1M.out.inf.ts
-rw------- 1 hbecher datastore_eb_groups_HighlanderLab_admin 5.6M Feb 20 11:58 test1M.out.inf.vcf
```

# Analysing data in TS format
