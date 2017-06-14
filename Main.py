from RiotAPI import RiotAPI

def main():
	api = RiotAPI('f4da4502-1335-45ab-97dd-593325120b1d')
	r = api.get_summoner_by_name('Raznick')
	print r

if __name__ == "__main__":
	main()
