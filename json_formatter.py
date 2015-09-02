import sys
import json
import sys

try:
	if sys.argv[1] == 'help':
		print '*** JSON Formatter HELP ***'
		print "* Pass in a JSON file location as the first argument.  This is the file that will be pretty printed"
		print '* Pass in a second argument with a file name to be written to. If no second argument is present, it will just print to the screen.'
	else:
		f = open (sys.argv[1], 'r')
		j = json.loads(f.read())
		f.close()
		data = json.dumps(j, indent=4, sort_keys=True)
		try:
			with open(sys.argv[2], "w") as json_output:
				json_output.write(data)
		except:
			print data
			print ''
except:
	e = sys.exc_info()[1]
	print 'Error: ' + e[0]