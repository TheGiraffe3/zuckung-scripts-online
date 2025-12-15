import os

def run():
	plugin = os.environ['PLUGIN']
	plugintxt = '' + \
		'name "' + plugin + ' ship.merging"\n' +\
		'about "This plugin provides a ship.merging mission for ' + plugin + '."\n' +\
		'about "Thanks to zuckung for creating the icon and the script to generate this."\n' +\
		'authors\n' +\
		'	Loymdayddaud\n' +\
		'	zuckung\n'
	with open("plugin.txt", 'a') as fh:
		fh.write(plugintxt)

if __name__ == '__main__':
	run()
