scrm=~/HighlanderLab/share/scrm-1.7.4/scrm

$scrm 210 1 -r 4e-2 1e6  `# 210 haploid genomes, 1 rep, GS of 10M with overall rec prob of .4 (=4/100_000_000 per bp) `\
  -l 0  `# SMC'`\
  -I 3 10 100 100 ` # 3 pops with 10, 50, 50 haploid samples each `\
  -n 1 67000 -n 2 170000 -n 3 850  `# set pop sizes `\
  -t 23.48e-3  `# mutations rate overall (u=5.87e-9 per bp)` \
  -ej 5000 2 1 -ej 3000 3 2 ` # splits `\
  -p 15 --transpose-segsites > $1
