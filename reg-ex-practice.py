import re 
import operator

fh = open('mbox-short.txt')

confidence_list = []
for line in fh:
	line = line.strip()
	y = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
	if len(y) > 0:
		confidence_list.append(y)
confidence_max = max(confidence_list)
confidence_min = min(confidence_list)

print ("Maximum: " + str(confidence_max))
print ("Minimum: " + str(confidence_min))


