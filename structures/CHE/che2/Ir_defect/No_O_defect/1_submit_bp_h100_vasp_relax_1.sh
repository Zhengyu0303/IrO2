#!/bin/bash
squeue > squeue.temp
echo 'Submitting proto0_coverage54/Ir39H3O84_0 (ID: jproto0_coverage54-Ir39H3O84_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage54/Ir39H3O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage54-Ir39H3O84_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage54-Ir39H3O84_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage54-Ir39H3O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage54-Ir39H3O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage62/Ir39H3O84_0 (ID: jproto0_coverage62-Ir39H3O84_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage62/Ir39H3O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage62-Ir39H3O84_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage62-Ir39H3O84_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage62-Ir39H3O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage62-Ir39H3O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage65/Ir39H5O84_0 (ID: jproto0_coverage65-Ir39H5O84_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage65/Ir39H5O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage65-Ir39H5O84_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage65-Ir39H5O84_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage65-Ir39H5O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage65-Ir39H5O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage39/Ir39H5O84_0 (ID: jproto0_coverage39-Ir39H5O84_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage39/Ir39H5O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage39-Ir39H5O84_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage39-Ir39H5O84_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage39-Ir39H5O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage39-Ir39H5O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage37/Ir39H5O84_0 (ID: jproto0_coverage37-Ir39H5O84_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage37/Ir39H5O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage37-Ir39H5O84_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage37-Ir39H5O84_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage37-Ir39H5O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage37-Ir39H5O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage30/Ir39H3O84_0 (ID: jproto0_coverage30-Ir39H3O84_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage30/Ir39H3O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage30-Ir39H3O84_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage30-Ir39H3O84_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage30-Ir39H3O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage30-Ir39H3O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage64/Ir39H4O84_0 (ID: jproto0_coverage64-Ir39H4O84_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage64/Ir39H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage64-Ir39H4O84_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage64-Ir39H4O84_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage64-Ir39H4O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage64-Ir39H4O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage63/Ir39H4O84_0 (ID: jproto0_coverage63-Ir39H4O84_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage63/Ir39H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage63-Ir39H4O84_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage63-Ir39H4O84_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage63-Ir39H4O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage63-Ir39H4O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage55/Ir39H4O84_0 (ID: jproto0_coverage55-Ir39H4O84_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage55/Ir39H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage55-Ir39H4O84_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage55-Ir39H4O84_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage55-Ir39H4O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage55-Ir39H4O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage52/Ir39H2O84_0 (ID: jproto0_coverage52-Ir39H2O84_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage52/Ir39H2O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage52-Ir39H2O84_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage52-Ir39H2O84_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage52-Ir39H2O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage52-Ir39H2O84_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

