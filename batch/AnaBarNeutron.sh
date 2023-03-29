#!/bin/bash
#PBS -N CDetOptical
#PBS -m n
#PBS -M root@jlabdaq.cnuadmin.cnu.edu
#PBS -l walltime=40:00:00
#PBS -V

export homedir=$HOME

export nevents=100
export tempdir=$homedir/CDetOptical/batch

export MACRO_PATH=$homedir/CDetOptical/macros/
export MCMACRO=$tempdir/AnaBarMC_$RUN_NUMBER.mac

echo "/control/macroPath $MACRO_PATH"	 	                         >   $MCMACRO
echo "/AnaBarMC/physics/addPhysics standard_opt3"                        >>   $MCMACRO
echo "/AnaBarMC/physics/optical 1"	                                 >>  $MCMACRO
echo "/AnaBarMC/physics/hadronic 1"	                                 >>  $MCMACRO
echo "/AnaBarMC/detector/AnaBarXpos 37.50"	                         >>  $MCMACRO
echo "/AnaBarMC/detector/AnaBarYpos 0.00"	                         >>  $MCMACRO
echo "/AnaBarMC/detector/AnaBarZpos 150.00"	                         >>  $MCMACRO
echo "/AnaBarMC/detector/NumberOfLayers 14"	                         >>  $MCMACRO
echo "/AnaBarMC/detector/NumberOfBars 14"	                         >>  $MCMACRO
echo "/AnaBarMC/detector/NumberOfSides 2"	                         >>  $MCMACRO
echo "/AnaBarMC/detector/NumberOfModules 3"	                         >>  $MCMACRO
echo "/AnaBarMC/detector/NumberOfPlanes 2"	                         >>  $MCMACRO
echo "/run/initialize"                                                   >>  $MCMACRO
echo "/AnaBarMC/generator/Mode 1"                              >>  $MCMACRO
echo "/AnaBarMC/generator/InputFile $tempdir/data/AnaBarMC_Gen_$RUN_NUMBER.root" >>  $MCMACRO
echo "/AnaBarMC/analysis/setOutputFile $tempdir/rootfiles/AnaBarMC_$RUN_NUMBER.root" >>  $MCMACRO

cd $tempdir

export PATH=$ROOTSYS/bin:$PATH
AnaBarMC $MCMACRO #>& /dev/null
echo "****************** AnaBarMC Finished"

cp    ${tempdir}/rootfiles/"AnaBarMC_$RUN_NUMBER.root"   ${OUTPUT_DIR}/
rm -f ${tempdir}/rootfiles/"AnaBarMC_$RUN_NUMBER.root"
rm -f $MCMACRO
