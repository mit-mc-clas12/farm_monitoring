import subprocess
import datetime
import re

currentDT = datetime.datetime.now()

a=subprocess.Popen("/site/scicomp/auger-slurm/bin/slurmHosts",stdout=subprocess.PIPE)
b= a.communicate()[0]
available=0
total=0
for i, content in enumerate(re.split('684|1563|771|308|332',b)):
	if i>0:
		state=content[i-1][-1]
		job=content[i][1]
		total=total+int(job.split('/')[1])
		if state=='IDLE' or state=='MIXED':
			available=available+int(job.split('/')[0])

file = open(r"Sample_script_result_jlab","w")
file.write("Updated on "+currentDT.strftime("%Y-%m-%d %H:%M:%S"))
file.write("\nTotal cores: "+str(total))
file.write("\nBusy cores: "+str(total-available))
file.write("\nIdle cores: "+str(available))
file.close()