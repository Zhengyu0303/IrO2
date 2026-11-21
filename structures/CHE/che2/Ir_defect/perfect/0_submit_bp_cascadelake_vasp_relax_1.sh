#!/bin/bash
squeue > squeue.temp
echo 'Submitting perfect_coverage24/Ir40H4O84_0 (ID: jperfect_coverage24-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage24/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage24-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage24-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage24-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage24-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage23/Ir40H5O84_0 (ID: jperfect_coverage23-Ir40H5O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage23/Ir40H5O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage23-Ir40H5O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage23-Ir40H5O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage23-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage23-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage15/Ir40H4O84_0 (ID: jperfect_coverage15-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage15/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage15-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage15-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage15-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage15-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage12/Ir40H3O84_0 (ID: jperfect_coverage12-Ir40H3O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage12/Ir40H3O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage12-Ir40H3O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage12-Ir40H3O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage12-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage12-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage46/Ir40H5O84_0 (ID: jperfect_coverage46-Ir40H5O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage46/Ir40H5O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage46-Ir40H5O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage46-Ir40H5O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage46-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage46-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage41/Ir40H3O84_0 (ID: jperfect_coverage41-Ir40H3O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage41/Ir40H3O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage41-Ir40H3O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage41-Ir40H3O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage41-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage41-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage48/Ir40H5O84_0 (ID: jperfect_coverage48-Ir40H5O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage48/Ir40H5O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage48-Ir40H5O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage48-Ir40H5O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage48-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage48-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage4/Ir40H2O84_0 (ID: jperfect_coverage4-Ir40H2O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage4/Ir40H2O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage4-Ir40H2O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage4-Ir40H2O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage4-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage4-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage3/Ir40H2O84_0 (ID: jperfect_coverage3-Ir40H2O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage3/Ir40H2O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage3-Ir40H2O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage3-Ir40H2O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage3-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage3-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage13/Ir40H4O84_0 (ID: jperfect_coverage13-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage13/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage13-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage13-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage13-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage13-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage14/Ir40H3O84_0 (ID: jperfect_coverage14-Ir40H3O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage14/Ir40H3O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage14-Ir40H3O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage14-Ir40H3O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage14-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage14-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage22/Ir40H4O84_0 (ID: jperfect_coverage22-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage22/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage22-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage22-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage22-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage22-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage25/Ir40H5O84_0 (ID: jperfect_coverage25-Ir40H5O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage25/Ir40H5O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage25-Ir40H5O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage25-Ir40H5O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage25-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage25-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage2/Ir40H2O84_0 (ID: jperfect_coverage2-Ir40H2O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage2/Ir40H2O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage2-Ir40H2O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage2-Ir40H2O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage2-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage2-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage49/Ir40H6O84_0 (ID: jperfect_coverage49-Ir40H6O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage49/Ir40H6O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage49-Ir40H6O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage49-Ir40H6O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage49-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage49-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage5/Ir40H3O84_0 (ID: jperfect_coverage5-Ir40H3O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage5/Ir40H3O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage5-Ir40H3O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage5-Ir40H3O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage5-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage5-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage40/Ir40H6O84_0 (ID: jperfect_coverage40-Ir40H6O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage40/Ir40H6O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage40-Ir40H6O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage40-Ir40H6O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage40-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage40-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage47/Ir40H6O84_0 (ID: jperfect_coverage47-Ir40H6O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage47/Ir40H6O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage47-Ir40H6O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage47-Ir40H6O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage47-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage47-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage54/Ir40H6O84_0 (ID: jperfect_coverage54-Ir40H6O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage54/Ir40H6O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage54-Ir40H6O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage54-Ir40H6O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage54-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage54-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage53/Ir40H6O84_0 (ID: jperfect_coverage53-Ir40H6O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage53/Ir40H6O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage53-Ir40H6O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage53-Ir40H6O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage53-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage53-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage38/Ir40H4O84_0 (ID: jperfect_coverage38-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage38/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage38-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage38-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage38-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage38-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage36/Ir40H4O84_0 (ID: jperfect_coverage36-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage36/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage36-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage36-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage36-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage36-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage31/Ir40H4O84_0 (ID: jperfect_coverage31-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage31/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage31-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage31-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage31-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage31-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage52/Ir40H5O84_0 (ID: jperfect_coverage52-Ir40H5O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage52/Ir40H5O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage52-Ir40H5O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage52-Ir40H5O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage52-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage52-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage55/Ir40H6O84_0 (ID: jperfect_coverage55-Ir40H6O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage55/Ir40H6O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage55-Ir40H6O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage55-Ir40H6O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage55-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage55-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage30/Ir40H4O84_0 (ID: jperfect_coverage30-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage30/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage30-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage30-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage30-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage30-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage37/Ir40H4O84_0 (ID: jperfect_coverage37-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage37/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage37-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage37-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage37-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage37-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage39/Ir40H5O84_0 (ID: jperfect_coverage39-Ir40H5O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage39/Ir40H5O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage39-Ir40H5O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage39-Ir40H5O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage39-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage39-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage42/Ir40H4O84_0 (ID: jperfect_coverage42-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage42/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage42-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage42-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage42-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage42-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage9/Ir40H3O84_0 (ID: jperfect_coverage9-Ir40H3O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage9/Ir40H3O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage9-Ir40H3O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage9-Ir40H3O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage9-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage9-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage45/Ir40H5O84_0 (ID: jperfect_coverage45-Ir40H5O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage45/Ir40H5O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage45-Ir40H5O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage45-Ir40H5O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage45-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage45-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage0/Ir40O84_0 (ID: jperfect_coverage0-Ir40O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage0/Ir40O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage0-Ir40O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage0-Ir40O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage0-Ir40O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage0-Ir40O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage7/Ir40H1O84_0 (ID: jperfect_coverage7-Ir40H1O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage7/Ir40H1O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage7-Ir40H1O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage7-Ir40H1O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage7-Ir40H1O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage7-Ir40H1O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage20/Ir40H3O84_0 (ID: jperfect_coverage20-Ir40H3O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage20/Ir40H3O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage20-Ir40H3O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage20-Ir40H3O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage20-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage20-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage27/Ir40H2O84_0 (ID: jperfect_coverage27-Ir40H2O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage27/Ir40H2O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage27-Ir40H2O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage27-Ir40H2O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage27-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage27-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage18/Ir40H3O84_0 (ID: jperfect_coverage18-Ir40H3O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage18/Ir40H3O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage18-Ir40H3O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage18-Ir40H3O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage18-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage18-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage11/Ir40H3O84_0 (ID: jperfect_coverage11-Ir40H3O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage11/Ir40H3O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage11-Ir40H3O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage11-Ir40H3O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage11-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage11-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage16/Ir40H5O84_0 (ID: jperfect_coverage16-Ir40H5O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage16/Ir40H5O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage16-Ir40H5O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage16-Ir40H5O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage16-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage16-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage29/Ir40H4O84_0 (ID: jperfect_coverage29-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage29/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage29-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage29-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage29-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage29-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage6/Ir40H4O84_0 (ID: jperfect_coverage6-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage6/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage6-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage6-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage6-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage6-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage1/Ir40H1O84_0 (ID: jperfect_coverage1-Ir40H1O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage1/Ir40H1O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage1-Ir40H1O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage1-Ir40H1O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage1-Ir40H1O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage1-Ir40H1O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage8/Ir40H2O84_0 (ID: jperfect_coverage8-Ir40H2O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage8/Ir40H2O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage8-Ir40H2O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage8-Ir40H2O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage8-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage8-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage44/Ir40H4O84_0 (ID: jperfect_coverage44-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage44/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage44-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage44-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage44-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage44-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage43/Ir40H5O84_0 (ID: jperfect_coverage43-Ir40H5O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage43/Ir40H5O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage43-Ir40H5O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage43-Ir40H5O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage43-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage43-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage17/Ir40H2O84_0 (ID: jperfect_coverage17-Ir40H2O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage17/Ir40H2O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage17-Ir40H2O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage17-Ir40H2O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage17-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage17-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage28/Ir40H3O84_0 (ID: jperfect_coverage28-Ir40H3O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage28/Ir40H3O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage28-Ir40H3O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage28-Ir40H3O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage28-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage28-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage10/Ir40H2O84_0 (ID: jperfect_coverage10-Ir40H2O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage10/Ir40H2O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage10-Ir40H2O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage10-Ir40H2O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage10-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage10-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage26/Ir40H6O84_0 (ID: jperfect_coverage26-Ir40H6O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage26/Ir40H6O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage26-Ir40H6O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage26-Ir40H6O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage26-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage26-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage19/Ir40H4O84_0 (ID: jperfect_coverage19-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage19/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage19-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage19-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage19-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage19-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage21/Ir40H4O84_0 (ID: jperfect_coverage21-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage21/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage21-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage21-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage21-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage21-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage32/Ir40H5O84_0 (ID: jperfect_coverage32-Ir40H5O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage32/Ir40H5O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage32-Ir40H5O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage32-Ir40H5O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage32-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage32-Ir40H5O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage35/Ir40H3O84_0 (ID: jperfect_coverage35-Ir40H3O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage35/Ir40H3O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage35-Ir40H3O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage35-Ir40H3O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage35-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage35-Ir40H3O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage50/Ir40H7O84_0 (ID: jperfect_coverage50-Ir40H7O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage50/Ir40H7O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage50-Ir40H7O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage50-Ir40H7O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage50-Ir40H7O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage50-Ir40H7O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage57/Ir40H8O84_0 (ID: jperfect_coverage57-Ir40H8O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage57/Ir40H8O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage57-Ir40H8O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage57-Ir40H8O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage57-Ir40H8O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage57-Ir40H8O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage34/Ir40H2O84_0 (ID: jperfect_coverage34-Ir40H2O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage34/Ir40H2O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage34-Ir40H2O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage34-Ir40H2O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage34-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage34-Ir40H2O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage33/Ir40H6O84_0 (ID: jperfect_coverage33-Ir40H6O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage33/Ir40H6O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage33-Ir40H6O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage33-Ir40H6O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage33-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage33-Ir40H6O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage56/Ir40H7O84_0 (ID: jperfect_coverage56-Ir40H7O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage56/Ir40H7O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage56-Ir40H7O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage56-Ir40H7O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage56-Ir40H7O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage56-Ir40H7O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

echo 'Submitting perfect_coverage51/Ir40H4O84_0 (ID: jperfect_coverage51-Ir40H4O84_0) via bp.cascadelake.vasp.relax.1.pbs [slurm]...' 
cd './perfect_coverage51/Ir40H4O84_0'
if [ -s submit_script.sh ]
then
	grep 'jobjperfect_coverage51-Ir40H4O84_0eof' ../../delete_all_jobs_bp_cascadelake.sh > /dev/null
	if [ $? -eq 0 ]
	then
		LASTJOB=`grep "jobjperfect_coverage51-Ir40H4O84_0eof" ../../delete_all_jobs_bp_cascadelake.sh | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="scancel") print $(i+1)}'`
		echo "Found dependency: $LASTJOB"
		JOBID=`sbatch --dependency=afterany:$LASTJOB submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage51-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	else
		JOBID=`sbatch submit_script.sh --parsable | tail -n 1 | awk '{print $NF}'`
		echo "scancel $JOBID #jobjperfect_coverage51-Ir40H4O84_0eof" >> ../../delete_all_jobs_bp_cascadelake.sh
	fi
fi
cd ../../ 

