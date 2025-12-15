import os

def run():
	prnumber = os.environ['PR'].rstrip('\n')
	plugintxt = '' + \
		'name "' + prnumber + ' Plugin"\n' +\
		'about "This plugin contains the changes of Endless Sky pull request ' + prnumber + '."\n'
	with open("plugin.txt", 'a') as fh:
		fh.write(plugintxt)

if __name__ == '__main__':
	run()
