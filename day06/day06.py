

def main():
    filename = "input.txt"
    #filename = "test.txt"

    with open(filename, "r") as file:
        input_read = file.readlines()


    races = {}

    race_time, distance = input_read

    # part 1
    times_str = race_time.split()[1:] # exclude "Time: "
    distances_str = distance.split()[1:] # exclude "Distance: "
    
    for i in range(len(times_str)):
        races[int(times_str[i])] = int(distances_str[i])

        


    number_of_ways_of_wining_races = []
    for race_time in races.keys():
        distance_to_beat = races[race_time]
        
        possible_distances = getDistancesByTime(race_time)
        record_breaker_distances = getRecordBreakerDistances(possible_distances, distance_to_beat)
        number_of_ways_of_wining_races.append(len(record_breaker_distances))


    margin_of_error_part1 = getMarginOfError(number_of_ways_of_wining_races)
    

    # part 2
    big_race_time = int("".join(times_str))
    big_race_distance = int("".join(distances_str))

    possible_distances_2 = getDistancesByTime(big_race_time)
    record_breaker_distances_2 = getRecordBreakerDistances(possible_distances_2, big_race_distance)
    margin_of_error_part2 = len(record_breaker_distances_2)

    


    print("part 1:", margin_of_error_part1)
    print("part 2:", margin_of_error_part2)
        

def getDistancesByTime(race_time):
    distances = []
    for t in range(race_time + 1):
        time_left = race_time - t
        distance_traveled = time_left * t
        distances.append(distance_traveled)

    return distances


def getRecordBreakerDistances(candidates, record):
    """ Brute Force -   could be optimized by starting in the middle and goind left and right 
                        until the time is smaller than the record, 
                        but the input is not that big so this runs fast enough (~8s)"""
                        
    races_won = []
    for candidate in candidates:
        if candidate > record:
            races_won.append(candidate)
    return races_won


def getMarginOfError(number_of_ways_of_winning_races):
    total = 1
    for number in number_of_ways_of_winning_races:
        total *= number
    return total






if __name__ == "__main__":
    main()