def greet_users(names):
	for name in names:
		msg = f"Hello, {name.title()}!"
		print(msg)
greet_users(['hannah', 'ty', 'margot'])