airports = ["BCN", "Barcelona International"], ["DUB","Dublin"]

airportCode = input("Enter the airport code: ")
airportCode = airportCode.upper()

for i in range(0,int(len(airports))):
    if airportCode == airports[i][0]:
        print(airports[i][1])
