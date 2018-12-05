val input = sc.textFile("twitter.edges")
val input_in_line = input.map(line => line.split(": "))
val user_followers_in_one = input_in_line.flatMap(arr => {
	val users = arr(1)
	val users_array = users.split(",")
	users_array.map(user => (user, 1))
})
val user_followers_in_total = user_followers_in_one.reduceByKey((a,b) => a+b)
val filtered_users = user_followers_in_total.filter(user => user._2 > 1000)
filtered_users.saveAsTextFile("output")
System.exit(0)
