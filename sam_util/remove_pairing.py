__author__ = 'langmead'

"""
Goes through a SAM file with pairs and remove all the pairing info, from the
FLAGS field as well as the TLEN field.

E.g.:

samtools view -h XXX.bam | python remove_pairing.py | samtools view -bS -o YYY.bam -
"""

import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--just-flags', action='store_true', help='Just remove FLAGS; leave TLEN, RNEXT, PNEXT alone')
args = parser.parse_args()


for ln in sys.stdin:
    ln = ln.rstrip()
    if ln[0] == '@':
        print ln
        continue
    toks = ln.split('\t')
    toks[1] = '0'
    if not args.just_flags:
        toks[7] = toks[8] = '0'
        toks[6] = '*'
    print '\t'.join(toks)
