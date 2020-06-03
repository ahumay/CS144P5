// load in file
val lines = sc.textFile("twitter.edges")

// filter only userIDs that they are following
val following = lines.flatMap(line => line.split(" ")(1).split(","))

// add counter to each id
val following_numeric = following.map(id => (id, 1))

// reduce over each user id  
val follow_count = following_numeric.reduceByKey((a, b) => a + b)

// filter out any under 1000
val over_1000 = follow_count.filter(id => id._2 > 1000)

// save to output directory
over_1000.saveAsTextFile("output")

// exit
System.exit(0)