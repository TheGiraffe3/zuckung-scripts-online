import os

def run():
	repository = os.environ['PLUGIN_REPOSITORY']
	reposplitted = repository.split('\n')
	if reposplitted[0] == '### Repository':
		print('SUCCESS: Newly created issue is a compatibility request.')
		print()
	print('REPOSITORY TO DOWNLOAD:')
	repofull = reposplitted[2]
	reponamesplit = repofull.split('/')
	repo = reponamesplit[0] + '/' + reponamesplit[1]
	repo = repo.rstrip('\n')
	print(repo)
	print()
	with open("repository", 'a') as fh:
		print(f'{repo}', file=fh)
	print(f"Created repository file with value of {repo}")
	print()
	reponame = reponamesplit[1]
	with open("repository_name", 'a') as fh:
		fh.write(reponame)
	print(f"Created repository_name file with value of {reponame}")
	print()
	datapath = ''
	for i in range(1, len(reponamesplit)):
		datapath += reponamesplit[i] + '/'
	datapath += 'data'
	with open("datapath", 'a') as fh:
		fh.write(datapath)
	print(f"Created datapath file with value of {datapath}")
	print()
	if len(reponamesplit) > 3:
		multipluginname = reponamesplit[3]
		print(f"Created multipluginname file with value of {multipluginname}")
		with open("multipluginname", 'a') as fh:
			fh.write(multipluginname)
	else:
		multipluginname = reponame
		print(f"Created multipluginname file with value of {multipluginname} (which is the same as {reponame})")
		with open("multipluginname", 'a') as fh:
			fh.write(multipluginname)

if __name__ == '__main__':
	run()
