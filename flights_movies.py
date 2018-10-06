def binarySearch(i, data):
    if len(data) == 0:
        return False
    else:
        midpoint = len(data) // 2
        if data[midpoint] == i:
            return True
        else:
            if i < data[midpoint]:
                return binarySearch(i, data[:midpoint])
            else:
                return binarySearch(i, data[midpoint+1:])

def getMoviesImprovedBinary(flight_length, movie_lengths):
    movie_lengths.sort()
    print movie_lengths
    for movie in movie_lengths:
        if binarySearch(flight_length - movie, movie_lengths):
            print movie, flight_length - movie
            return True
    return False


def getMoviesSetMethod(flight_length, movie_lengths):

    movies_seen = set()

    for movie_length in movie_lengths:
        second_length = flight_length - movie_length
        if second_length in movies_seen:
            print movie_length, second_length
            return True

        movies_seen.add(movie_length)


    # Never found any
    return False


if __name__ == "__main__":
    movies = [60,15,20,40,10, 30]
    flight_length = 90
    print getMoviesSetMethod(flight_length, movies)