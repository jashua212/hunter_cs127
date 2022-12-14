
# assignment 43

# import the folium and pandas packages
import folium
import pandas as pd


def main():
	# read after_school.csv with pandas
	afterSchools = pd.read_csv('after_school.csv')

	# create a map, centered on nyc:
	mapNYC = folium.Map(location=[40.768731, -73.964915])

	# get user's choice
	print('Enter 1 for Borough/Community,')
	print('2 for Grade Level / Age Group')
	choice = input('Your choice: ')

	# get column from user's choice
	if choice == '1':
		column = 'Borough/Community'
	elif choice == '2':
		column = 'Grade Level / Age Group'
	else:
		print('your choice is incorrect')
		quit()

	# get groupData from column
	groupData = afterSchools.groupby(column)

	# show user all possible selections from groupData
	print(groupData.groups.keys())

	# get user's pick
	pick = input('Enter ' + column + ' name: ')

	# get subgroupData from user's pick
	subgroupData = groupData.get_group(pick)

	# add markers to mapNYC based on subgroupData
	for index,row in subgroupData.iterrows():
		lat = row['Latitude']
		lon = row['Longitude']
		name = row['Name']

		if lat and lon:
			newMarker = folium.Marker([lat, lon], popup=name)
			newMarker.add_to(mapNYC)

	# create string for outFile name based on user's choice
	if choice == 1:
		words = pick.lower().split(' ')
	else:
		words = pick.lower().split('/')
	outFile = '_'.join(words) + '_after_school.html'

	# save mapNYC as outFile
	mapNYC.save(outfile=outFile)
	print('outFile:', outFile)


if __name__ == '__main__':
	main()
