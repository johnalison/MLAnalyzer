import os
from glob import glob
import re
import argparse

#parser = argparse.ArgumentParser(description='Run RHAnalyzer')
#parser.add_argument('-d','--decay', required=True, help='Decay:Single*Pt50',type=str)
#args = parser.parse_args()

eosDir='/eos/cms/store/user/mandrews/ML'
#decay='%s_FEVTDEBUG'%args.decay
decay='T7WgStealth_800_112_FEVTDEBUG_noPU'

cfg='RecHitAnalyzer/python/ConfFile_cfg.py'
inputFiles_ = ['file:%s'%path for path in glob('%s/FEVTDEBUG/%s/*/*/step*root'%(eosDir,decay))]

listname = 'list_%s.txt'%decay
with open(listname, 'w') as list_file:
    for inputFile in inputFiles_:
        list_file.write("%s\n" % inputFile)

maxEvents_=-1
skipEvents_=0

#cmd="cmsRun %s inputFiles_load=%s maxEvents=%d skipEvents=%d outputFile=%s/IMGs/%s_IMG.root"%(cfg,listname,maxEvents_,skipEvents_,eosDir,decay)
cmd="cmsRun %s inputFiles_load=%s maxEvents=%d skipEvents=%d outputFile=%s/IMGs/test_%s_IMG.root"%(cfg,listname,maxEvents_,skipEvents_,eosDir,decay)
print '%s'%cmd
#os.system(cmd)

#os.system('mv cEB*.eps %s/'%(inputTag))
