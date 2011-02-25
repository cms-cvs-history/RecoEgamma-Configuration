import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaElectronProducers.cosmicElectronSequence_cff import *
from RecoEgamma.EgammaPhotonProducers.cosmicPhotonSequence_cff import *
from RecoEgamma.EgammaPhotonProducers.cosmicConversionSequence_cff import *
from RecoEgamma.EgammaPhotonProducers.cosmicConversionTrackSequence_cff import *
from RecoEgamma.PhotonIdentification.photonId_cff import *

egammarecoGlobal_cosmics = cms.Sequence(cosmicConversionTrackSequence)
egammarecoCosmics_woConvPhotons = cms.Sequence(cosmicElectronSequence*cosmicPhotonSequence)
egammarecoCosmics = cms.Sequence(cosmicElectronSequence*cosmicConversionSequence*cosmicPhotonSequence*photonIDSequence)
egammarecoCosmics_woElectrons = cms.Sequence(cosmicConversionSequence*cosmicPhotonSequence*photonIDSequence)
