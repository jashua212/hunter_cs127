
# assignment 42

# import the folium and pandas packages
import folium
import pandas as pd


def main():
	# get outFile name from user
	outFile = input('Enter output file: ')

	# for testing only - overwrite user input
	outFile = 'nyc_hospitals.html'

	# read nyc_hospitals.csv with pandas
	hospitals = pd.read_csv('nyc_hospitals.csv')

	# create a map, centered on nyc:
	mapNYC = folium.Map(location=[40.768731, -73.964915])

	# add marker on map for each hospital:
	for index,row in hospitals.iterrows():
		lat = row['Latitude']
		lon = row['Longitude']
		name = row['Facility Name']

		if lat and lon:
			newMarker = folium.Marker([lat, lon], popup=name)
			newMarker.add_to(mapNYC)

	# save map as html
	mapNYC.save(outfile=outFile)


if __name__ == '__main__':
	main()
