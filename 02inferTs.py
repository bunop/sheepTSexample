# USAGE: python 02inferTs.py infile genomeLength nDiploids

import tsinfer
import sys
import numpy as np
import logging

log = logging.getLogger('logger')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
log.addHandler(ch)


infi = sys.argv[1]
log.info("Infile is %s" % infi)

ll   = int(sys.argv[2])
log.info("Genome size set ot %d" % ll)

nInd   = int(sys.argv[3])
log.info("Expecting %d diploid individuals" % nInd)


log.info("Adding site data to samples object")
samp = tsinfer.SampleData(sequence_length=ll)

for i in range(nInd):
    samp.add_individual(ploidy=2)

c = 0
last=-1

with open(infi) as f:
    for line in f:
        c+=1
        if c % 50000 == 0: log.info("Processed %d variant sites." % c)
        if c > 6:
            a = line.strip().split(" ")
            if int(float(a[0])*ll) != last:
                samp.add_site(float(a[0])*ll, np.array(a[2:], dtype=np.int16))
                last=int(float(a[0])*ll)
samp.finalise()

log.info("Running inference...")
ts = tsinfer.infer(samp)


log.info("Writing TS and VCF...")
ts.dump(infi + ".inf.ts")
with open(infi + ".inf.vcf", "w") as f:
    ts.write_vcf(f)

log.info("Done.")
