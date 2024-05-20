#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-26"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["7968-12703"] = \
 [ 119188, 119189, 119190, 119439, 119440, 119441,]

on["8606-12701"] = \
 [ 119404, 119405, 119406, 119408, 119409, 119410, 119412, 119413, 119414, 119416, 119417, 119418,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["7968-12703"] = ""
pars1["8606-12701"] = ""


#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["7968-12703"] = ""
pars2["8606-12701"] = ""


#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}
pars3["7968-12703"] = ""
pars3["8606-12701"] = ""


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
