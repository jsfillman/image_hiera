from urllib.request import urlopen
import re
import time


# Create our results file and add headers
outfile = open('docker_hiera.csv', 'w')
outfile.write("Name,Parent\n")

# Open list of repos to check
with open('docker_images.csv') as master_list:
	repo_list = master_list.read().splitlines()

# Iterate through list of repos and find parent images (only does one level atm)
for repo in repo_list:
	repo = repo.rstrip()
	outfile.write(repo)
	outfile.write(",")
	# outfile.write(repo)
	current_url = "https://raw.githubusercontent.com/{}/master/Dockerfile".format(repo)
	try:
		dockerfile = urlopen(current_url).read().decode("utf-8")
		results = re.findall(r'FROM.*\n',str(dockerfile))
		outfile.write(results[0][5:-1])
		outfile.write("\n")
		# outfile.write(results[5:-1])
	except:
		outfile.write("\n")
	# Pause for 1 second to avoid hitting GitHub read limits
	time.sleep(1)
