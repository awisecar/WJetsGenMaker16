import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(20) )

inputDir = '/store/user/awisecar/WJets_2018.02.26/GENoutput-NLO/'
fileDir = 'WJToLNu_MG5_NLO_FxFx_2j_as_0124/'
fileName = 'WJToLNu_2j_5f_NLO_FxFx_as_0124_GEN_2.root'

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        #'file:/afs/cern.ch/work/a/awisecar/MadGraph5Gen/genOutputTotal_NLO/WJToLNu_0j_5f_NLO_FxFx_as_0124_cff_py_LHE_GEN_tempEnd.root'
        #'file:/afs/cern.ch/user/a/awisecar/WJToLNu_1j_5f_NLO_FxFx_as_0108_GEN.root'
        #'file:/afs/cern.ch/user/a/awisecar/5MarchGENoutput/WJToLNu_0j_5f_NLO_FxFx_as_0108_GEN_cff_py_GEN.root'

        #'/store/user/awisecar/WJets_2018.02.26/GENoutput-NLO/WJToLNu_MG5_NLO_FxFx_0j_as_0124/WJToLNu_0j_5f_NLO_FxFx_as_0124_GEN_cff_py_GEN_1.root',
        #'/store/user/awisecar/WJets_2018.02.26/GENoutput-NLO/WJToLNu_MG5_NLO_FxFx_0j_as_0124/WJToLNu_0j_5f_NLO_FxFx_as_0124_GEN_cff_py_GEN_2.root',
        #'/store/user/awisecar/WJets_2018.02.26/GENoutput-NLO/WJToLNu_MG5_NLO_FxFx_0j_as_0124/WJToLNu_0j_5f_NLO_FxFx_as_0124_GEN_cff_py_GEN_3.root'

        #'/store/user/awisecar/WJets_2018.02.26/GENoutput-NLO/WJToLNu_MG5_NLO_FxFx_1j_as_0124/WJToLNu_1j_5f_NLO_FxFx_as_0124_GEN_cff_py_GEN_1.root'
	#'/store/user/awisecar/WJets_2018.02.26/GENoutput-NLO/WJToLNu_MG5_NLO_FxFx_1j_as_0124/WJToLNu_1j_5f_NLO_FxFx_as_0124_GEN_cff_py_GEN_2.root'

	#'/store/user/awisecar/WJets_2018.02.26/GENoutput-NLO/WJToLNu_MG5_NLO_FxFx_2j_as_0124/WJToLNu_2j_5f_NLO_FxFx_as_0124_GEN_2.root'								  
        inputDir + fileDir + fileName
    )
)

process.demo = cms.EDAnalyzer('WJets13TevAnalyzer')

process.printEventNumber = cms.OutputModule("AsciiOutputModule")

treeDir = '/eos/cms/store/user/awisecar/WJets_2018.02.26/GENtree-NLO/'
outputFileName = 'WJToLNu_MG5_NLO_FxFx_2j_as_0124_2.root'

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(
        #'wjets_amcnlo_gen_DATE.root'
        #'WJToLNu_2j_5f_NLO_FxFx_as_0124_GENtree_2.root'
        treeDir + outputFileName
    )
)

process.p = cms.Path(process.demo)
