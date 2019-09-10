import os
from glob import glob
import re
import argparse

#parser = argparse.ArgumentParser(description='Run RHAnalyzer')
#parser.add_argument('-d','--decay', required=True, help='Decay:Single*Pt50',type=str)
#args = parser.parse_args()

cfg='RecHitAnalyzer/python/ConfFile_cfg.py'
#inputFiles_ = ['file:%s'%path for path in glob('%s/FEVTDEBUG/%s/*/*/step*root'%(eosDir,decay))]

#inputFiles_ = ['file:%s'%path for path in glob('/store/user/johnda/AODSIM/QCD_Pt_30_70_13TeV_TuneCUETP8M1_noPU_AODSIM/181019_231226/0000/step_*.root')]
inputFiles_ = ['file:%s'%path for path in glob('/eos/uscms/store/user/jda102/AODSIM/QCD_Pt_30_70_13TeV_TuneCUETP8M1_noPU_AODSIM/181019_231226/0000/step_AODSIM_*root')]
outputDir = "/eos/uscms/store/user/jda102/"

listname = 'list_B.txt'
with open(listname, 'w') as list_file:
    for inputFile in inputFiles_:
        list_file.write("%s\n" % inputFile)

maxEvents_=-1
skipEvents_=0

#cmd="cmsRun %s inputFiles=%s maxEvents=%d skipEvents=%d"%(cfg,inputFiles_,maxEvents_,skipEvents_)
cmd="cmsRun %s inputFiles_load=%s maxEvents=%d skipEvents=%d outputFile=%s/IMGs/%s_IMG.root"%(cfg,listname,maxEvents_,skipEvents_,outputDir,"BJetNew")
#print '%s'%cmd
os.system(cmd)

#os.system('mv cEB*.eps %s/'%(inputTag))
