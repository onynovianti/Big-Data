# Get the lines from the textfile, create 4 partitions
access_log = sc.textFile("file:///home/cloudera/Documents/test.txt")

#Filter Lines with map only
error_log = access_log.filter(lambda x: "map" in x)

# Cache error log in memory
cached_log = error_log.cache()

# Now perform an action -  count
print "Total number of error records are %s" % (cached_log.count())

# Now find the number of lines with 
print "Number of product pages visited that have Errors is %s" % (cached_log.filter(lambda x: "product" in x).count()) 
