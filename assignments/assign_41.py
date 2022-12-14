
# assignment 41

# import the folium package for making maps
import folium


def main():
	# create a nyc map, centered (0,0):
	mapNYC = folium.Map(location=[40.75, -74.125])

	# add marker for central park
	folium.Marker(location=[40.7812, -73.9665], popup = "Central Park").add_to(mapNYC)

	# save as html
	mapNYC.save(outfile='nyc_Central_Park.html')


if __name__ == '__main__':
	main()
