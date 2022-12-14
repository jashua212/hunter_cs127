
# assignment 39

# import pandas library for data processing csv
import pandas as pd

def main():
	# read the csv file and store in movie_locations
	movie_locations = pd.read_csv('movie_locations.csv')

	# get user input for neighborhood
	hoods = input('order of most popular neighborhoods in movies: ')
	hoods = '3'			# for testing only - overwrite user input
	integerHoods = int(hoods)

	# get list of movie_locations sorted by 'Neighborhood' and slice it
	hoodsList = movie_locations['Neighborhood'].value_counts()

	# show sliced list to user
	print(hoodsList[:integerHoods])

	# get user input for director
	directors = input('order of directors/filmmakers making most movies in NYC: ')
	directors = '5'		# for testing only - overwrite user input
	integerDirectors = int(directors)

	# get list of movie_locations sorted by 'Director/Filmmaker Name' and slice it
	hoodsList = movie_locations['Director/Filmmaker Name'].value_counts()

	# show sliced list to user
	print(hoodsList[:integerDirectors])


if __name__ == '__main__':
	main()
