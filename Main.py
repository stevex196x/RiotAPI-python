from RiotAPI import RiotAPI

def main():
	api = RiotAPI('f4da4502-1335-45ab-97dd-593325120b1d')
	#region = input("Please enter your region")
	summoner_name = input("Please enter your summoner name\n")
	r = api.get_summoner_by_name(summoner_name)
	print(r)

if __name__ == "__main__":
	main()
