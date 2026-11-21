#!/bin/bash
squeue > squeue.temp
echo 'Submitting proto0_coverage7/Ir39H3O83_0 (ID: jproto0_coverage7-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage7/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage7-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage7-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage7-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage7-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage0/Ir39O83_0 (ID: jproto0_coverage0-Ir39O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage0/Ir39O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage0-Ir39O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage0-Ir39O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage0-Ir39O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage0-Ir39O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage9/Ir39H2O83_0 (ID: jproto0_coverage9-Ir39H2O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage9/Ir39H2O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage9-Ir39H2O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage9-Ir39H2O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage9-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage9-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage8/Ir39H1O83_0 (ID: jproto0_coverage8-Ir39H1O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage8/Ir39H1O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage8-Ir39H1O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage8-Ir39H1O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage8-Ir39H1O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage8-Ir39H1O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage1/Ir39H1O83_0 (ID: jproto0_coverage1-Ir39H1O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage1/Ir39H1O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage1-Ir39H1O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage1-Ir39H1O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage1-Ir39H1O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage1-Ir39H1O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage6/Ir39H2O83_0 (ID: jproto0_coverage6-Ir39H2O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage6/Ir39H2O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage6-Ir39H2O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage6-Ir39H2O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage6-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage6-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage16/Ir39H2O83_0 (ID: jproto0_coverage16-Ir39H2O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage16/Ir39H2O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage16-Ir39H2O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage16-Ir39H2O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage16-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage16-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage29/Ir39H3O83_0 (ID: jproto0_coverage29-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage29/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage29-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage29-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage29-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage29-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage11/Ir39H3O83_0 (ID: jproto0_coverage11-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage11/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage11-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage11-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage11-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage11-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage27/Ir39H3O83_0 (ID: jproto0_coverage27-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage27/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage27-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage27-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage27-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage27-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage18/Ir39H3O83_0 (ID: jproto0_coverage18-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage18/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage18-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage18-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage18-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage18-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage20/Ir39H3O83_0 (ID: jproto0_coverage20-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage20/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage20-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage20-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage20-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage20-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage74/Ir39H5O83_0 (ID: jproto0_coverage74-Ir39H5O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage74/Ir39H5O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage74-Ir39H5O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage74-Ir39H5O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage74-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage74-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage73/Ir39H5O83_0 (ID: jproto0_coverage73-Ir39H5O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage73/Ir39H5O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage73-Ir39H5O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage73-Ir39H5O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage73-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage73-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage45/Ir39H4O83_0 (ID: jproto0_coverage45-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage45/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage45-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage45-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage45-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage45-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage42/Ir39H3O83_0 (ID: jproto0_coverage42-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage42/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage42-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage42-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage42-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage42-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage21/Ir39H4O83_0 (ID: jproto0_coverage21-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage21/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage21-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage21-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage21-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage21-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage26/Ir39H2O83_0 (ID: jproto0_coverage26-Ir39H2O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage26/Ir39H2O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage26-Ir39H2O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage26-Ir39H2O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage26-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage26-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage19/Ir39H4O83_0 (ID: jproto0_coverage19-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage19/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage19-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage19-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage19-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage19-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage10/Ir39H2O83_0 (ID: jproto0_coverage10-Ir39H2O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage10/Ir39H2O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage10-Ir39H2O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage10-Ir39H2O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage10-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage10-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage17/Ir39H3O83_0 (ID: jproto0_coverage17-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage17/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage17-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage17-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage17-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage17-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage28/Ir39H2O83_0 (ID: jproto0_coverage28-Ir39H2O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage28/Ir39H2O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage28-Ir39H2O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage28-Ir39H2O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage28-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage28-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage43/Ir39H4O83_0 (ID: jproto0_coverage43-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage43/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage43-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage43-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage43-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage43-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage44/Ir39H3O83_0 (ID: jproto0_coverage44-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage44/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage44-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage44-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage44-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage44-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage72/Ir39H4O83_0 (ID: jproto0_coverage72-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage72/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage72-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage72-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage72-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage72-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage75/Ir39H6O83_0 (ID: jproto0_coverage75-Ir39H6O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage75/Ir39H6O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage75-Ir39H6O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage75-Ir39H6O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage75-Ir39H6O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage75-Ir39H6O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage57/Ir39H3O83_0 (ID: jproto0_coverage57-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage57/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage57-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage57-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage57-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage57-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage68/Ir39H4O83_0 (ID: jproto0_coverage68-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage68/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage68-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage68-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage68-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage68-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage50/Ir39H4O83_0 (ID: jproto0_coverage50-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage50/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage50-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage50-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage50-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage50-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage66/Ir39H4O83_0 (ID: jproto0_coverage66-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage66/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage66-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage66-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage66-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage66-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage59/Ir39H4O83_0 (ID: jproto0_coverage59-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage59/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage59-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage59-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage59-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage59-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage61/Ir39H4O83_0 (ID: jproto0_coverage61-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage61/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage61-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage61-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage61-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage61-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage35/Ir39H4O83_0 (ID: jproto0_coverage35-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage35/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage35-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage35-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage35-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage35-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage32/Ir39H2O83_0 (ID: jproto0_coverage32-Ir39H2O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage32/Ir39H2O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage32-Ir39H2O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage32-Ir39H2O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage32-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage32-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage60/Ir39H3O83_0 (ID: jproto0_coverage60-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage60/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage60-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage60-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage60-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage60-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage67/Ir39H5O83_0 (ID: jproto0_coverage67-Ir39H5O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage67/Ir39H5O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage67-Ir39H5O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage67-Ir39H5O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage67-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage67-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage58/Ir39H3O83_0 (ID: jproto0_coverage58-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage58/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage58-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage58-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage58-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage58-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage51/Ir39H5O83_0 (ID: jproto0_coverage51-Ir39H5O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage51/Ir39H5O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage51-Ir39H5O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage51-Ir39H5O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage51-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage51-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage56/Ir39H2O83_0 (ID: jproto0_coverage56-Ir39H2O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage56/Ir39H2O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage56-Ir39H2O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage56-Ir39H2O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage56-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage56-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage69/Ir39H5O83_0 (ID: jproto0_coverage69-Ir39H5O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage69/Ir39H5O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage69-Ir39H5O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage69-Ir39H5O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage69-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage69-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage33/Ir39H3O83_0 (ID: jproto0_coverage33-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage33/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage33-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage33-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage33-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage33-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage34/Ir39H3O83_0 (ID: jproto0_coverage34-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage34/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage34-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage34-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage34-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage34-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage3/Ir39H2O83_0 (ID: jproto0_coverage3-Ir39H2O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage3/Ir39H2O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage3-Ir39H2O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage3-Ir39H2O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage3-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage3-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage4/Ir39H1O83_0 (ID: jproto0_coverage4-Ir39H1O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage4/Ir39H1O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage4-Ir39H1O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage4-Ir39H1O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage4-Ir39H1O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage4-Ir39H1O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage5/Ir39H2O83_0 (ID: jproto0_coverage5-Ir39H2O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage5/Ir39H2O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage5-Ir39H2O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage5-Ir39H2O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage5-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage5-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage2/Ir39H1O83_0 (ID: jproto0_coverage2-Ir39H1O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage2/Ir39H1O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage2-Ir39H1O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage2-Ir39H1O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage2-Ir39H1O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage2-Ir39H1O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage70/Ir39H5O83_0 (ID: jproto0_coverage70-Ir39H5O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage70/Ir39H5O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage70-Ir39H5O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage70-Ir39H5O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage70-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage70-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage48/Ir39H3O83_0 (ID: jproto0_coverage48-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage48/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage48-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage48-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage48-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage48-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage77/Ir39H6O83_0 (ID: jproto0_coverage77-Ir39H6O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage77/Ir39H6O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage77-Ir39H6O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage77-Ir39H6O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage77-Ir39H6O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage77-Ir39H6O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage41/Ir39H3O83_0 (ID: jproto0_coverage41-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage41/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage41-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage41-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage41-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage41-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage79/Ir39H7O83_0 (ID: jproto0_coverage79-Ir39H7O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage79/Ir39H7O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage79-Ir39H7O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage79-Ir39H7O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage79-Ir39H7O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage79-Ir39H7O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage46/Ir39H4O83_0 (ID: jproto0_coverage46-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage46/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage46-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage46-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage46-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage46-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage12/Ir39H2O83_0 (ID: jproto0_coverage12-Ir39H2O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage12/Ir39H2O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage12-Ir39H2O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage12-Ir39H2O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage12-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage12-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage15/Ir39H4O83_0 (ID: jproto0_coverage15-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage15/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage15-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage15-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage15-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage15-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage23/Ir39H5O83_0 (ID: jproto0_coverage23-Ir39H5O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage23/Ir39H5O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage23-Ir39H5O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage23-Ir39H5O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage23-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage23-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage24/Ir39H1O83_0 (ID: jproto0_coverage24-Ir39H1O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage24/Ir39H1O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage24-Ir39H1O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage24-Ir39H1O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage24-Ir39H1O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage24-Ir39H1O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage78/Ir39H6O83_0 (ID: jproto0_coverage78-Ir39H6O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage78/Ir39H6O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage78-Ir39H6O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage78-Ir39H6O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage78-Ir39H6O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage78-Ir39H6O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage47/Ir39H5O83_0 (ID: jproto0_coverage47-Ir39H5O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage47/Ir39H5O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage47-Ir39H5O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage47-Ir39H5O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage47-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage47-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage40/Ir39H2O83_0 (ID: jproto0_coverage40-Ir39H2O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage40/Ir39H2O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage40-Ir39H2O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage40-Ir39H2O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage40-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage40-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage49/Ir39H4O83_0 (ID: jproto0_coverage49-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage49/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage49-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage49-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage49-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage49-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage76/Ir39H5O83_0 (ID: jproto0_coverage76-Ir39H5O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage76/Ir39H5O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage76-Ir39H5O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage76-Ir39H5O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage76-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage76-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage71/Ir39H6O83_0 (ID: jproto0_coverage71-Ir39H6O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage71/Ir39H6O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage71-Ir39H6O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage71-Ir39H6O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage71-Ir39H6O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage71-Ir39H6O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage25/Ir39H2O83_0 (ID: jproto0_coverage25-Ir39H2O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage25/Ir39H2O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage25-Ir39H2O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage25-Ir39H2O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage25-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage25-Ir39H2O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage22/Ir39H4O83_0 (ID: jproto0_coverage22-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage22/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage22-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage22-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage22-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage22-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage14/Ir39H3O83_0 (ID: jproto0_coverage14-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage14/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage14-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage14-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage14-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage14-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage13/Ir39H3O83_0 (ID: jproto0_coverage13-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage13/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage13-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage13-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage13-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage13-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage31/Ir39H4O83_0 (ID: jproto0_coverage31-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage31/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage31-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage31-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage31-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage31-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage36/Ir39H3O83_0 (ID: jproto0_coverage36-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage36/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage36-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage36-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage36-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage36-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage38/Ir39H4O83_0 (ID: jproto0_coverage38-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage38/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage38-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage38-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage38-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage38-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage53/Ir39H5O83_0 (ID: jproto0_coverage53-Ir39H5O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage53/Ir39H5O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage53-Ir39H5O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage53-Ir39H5O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage53-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage53-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage54/Ir39H5O83_0 (ID: jproto0_coverage54-Ir39H5O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage54/Ir39H5O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage54-Ir39H5O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage54-Ir39H5O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage54-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage54-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage62/Ir39H4O83_0 (ID: jproto0_coverage62-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage62/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage62-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage62-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage62-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage62-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage65/Ir39H4O83_0 (ID: jproto0_coverage65-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage65/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage65-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage65-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage65-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage65-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage39/Ir39H5O83_0 (ID: jproto0_coverage39-Ir39H5O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage39/Ir39H5O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage39-Ir39H5O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage39-Ir39H5O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage39-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage39-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage37/Ir39H4O83_0 (ID: jproto0_coverage37-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage37/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage37-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage37-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage37-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage37-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage30/Ir39H3O83_0 (ID: jproto0_coverage30-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage30/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage30-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage30-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage30-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage30-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage64/Ir39H3O83_0 (ID: jproto0_coverage64-Ir39H3O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage64/Ir39H3O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage64-Ir39H3O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage64-Ir39H3O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage64-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage64-Ir39H3O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage63/Ir39H5O83_0 (ID: jproto0_coverage63-Ir39H5O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage63/Ir39H5O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage63-Ir39H5O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage63-Ir39H5O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage63-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage63-Ir39H5O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage55/Ir39H6O83_0 (ID: jproto0_coverage55-Ir39H6O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage55/Ir39H6O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage55-Ir39H6O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage55-Ir39H6O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage55-Ir39H6O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage55-Ir39H6O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

echo 'Submitting proto0_coverage52/Ir39H4O83_0 (ID: jproto0_coverage52-Ir39H4O83_0) via bp.h100.vasp.relax.1.pbs [slurm]...' 
cd './proto0_coverage52/Ir39H4O83_0'
if [ -s submit_script.sh ]
then
	grep 'jobjproto0_coverage52-Ir39H4O83_0eof' ../../delete_all_jobs_bp_h100.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjproto0_coverage52-Ir39H4O83_0eof" ../../delete_all_jobs_bp_h100.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage52-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjproto0_coverage52-Ir39H4O83_0eof" >> ../../delete_all_jobs_bp_h100.sh
	fi
fi
cd ../../ 

