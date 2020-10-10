import os
import subprocess
import shlex
from tqdm import tqdm

# Download ET files based on links generated in Appears. Supporting textfiles in this dir 

txtfiles = [x for x in os.listdir(os.getcwd()) if x.endswith(".txt")]
txtfiles.sort()

def fetch(link, outdir):
	outfn = os.path.join(outdir,os.path.split(link)[1]).rstrip('\r\n')
	cmd = '''curl {} -o {} '''.format(link.strip(),outfn)
	subprocess.call(shlex.split(cmd), stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
	return 

def main():

	for f in txtfiles[:]:
	    print("Downloading Links in {} =====================".format(f))

	    with open(f) as file:

	        lines = file.readlines()
	        petfiles = [x for x in lines if "PET" in x]
	        aetfiles = [x for x in lines if not any(i in x for i in ['PET', "QC"])]

	        # print(petfiles)

	        print("Fetching PET data")

	        # for file in tqdm(petfiles[:]):
	        #     petdir = "MODIS_PET"
	        #     if not os.path.exists(petdir):
	        #         os.mkdir(petdir)				
	        #     fetch(file, petdir)

	        print("Fetching AET data")

	        for file in tqdm(aetfiles[:]):
	            aetdir = "MODIS_AET"
	            if not os.path.exists(aetdir):
	                os.mkdir(aetdir)		
	            fetch(file, aetdir)

	    print("Finished Processing {} =================== ".format(f))

if __name__ == '__main__':
    main()
