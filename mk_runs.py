#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-26"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["7968-12703"] = \
 [ 119188, 119189, 119190, 119439, 119440, 119441,  123894, 123895, 123896,]

on["8132-6101"] = \
 [ 121778, 121779, 121780, 121782, 121783, 121784, 121786, 121787, 121788, 
   122165, 122166, 122167,]   # nov 9

on["8243-12701"] = \
 [ 121791, 121792, 121793, 
   122170, 122171, 122172,]   # nov 9

on["8606-12701"] = \
 [ 119404, 119405, 119406, 119408, 119409, 119410, 119412, 119413, 119414, 119416, 119417, 119418,]

on["8725-9102"] = \
 [ 124202, 124203, 124204, 124206, 124207, 124208,
   124543, 124544, 124545, 124547, 124548, 124549, 124551, 124552, 124553, 124555, 124556, 124557,]


on["8938-12702"] = \
 [ 123927, 123928, 123929, 123931, 123932, 123933, 123935, 123936, 123937, 123939, 123940, 123941, 123945, 123946, 123947, 123949, 123950, 123951,
   124189, 124190, 124191, 124193, 124194, 124195,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["7968-12703"] = "speczoom=104,3 qagrade=3"
pars1["8132-6101"]  = "speczoom=104,3 qagrade=3"
pars1["8243-12701"] = "speczoom=108,3 qagrade=3"
pars1["8606-12701"] = "speczoom=108,3 qagrade=3"
pars1["8725-9102" ] = "speczoom=108,3 qagrade=3"
pars1["8938-12702"] = "speczoom=108,3 qagrade=3"


#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["7968-12703"] = ""
pars2["8132-6101"]  = ""
pars2["8243-12701"] = ""
pars2["8606-12701"] = ""
pars2["8938-12702"] = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, None, sys.argv)
