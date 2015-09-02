import sys
import json

try:
	if sys.argv[1] == 'help':
		print '*** JSON Formatter HELP ***'
		print "** Usage:"
		print '> python json_formatter.py foo.json bar.json'
		print '* This will the file foo.json and output it pretty-printed to bar.json'
		print '* Or you can leave out the second argument and just output to stdout'
		print '> python json_formatter.py foo.json'
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
