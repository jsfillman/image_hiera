from urllib.request import urlopen
import re

# Add portion to open file, and set `current_url` to line in file
# Then for loop getting `Dockerfile` from each
# Then write `current_repo


# Will want to make "kbase/auth2" the portion that changes in the for loop
current_repo = 'https://raw.githubusercontent.com/kbase/auth2/master/Dockerfile'

dockerfile = urlopen(current_repo).read().decode("utf-8")
results = re.findall(r'FROM.*\n',str(dockerfile))

for _ in results:
	str(_)
	print(_[5:-1])
