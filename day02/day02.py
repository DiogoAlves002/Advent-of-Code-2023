
def main():
    input_file = "input.txt"
    #input_file = "test.txt"


    with open(input_file, "r") as file:

        games = {} # {
                    # game_id: {
                    #           green: n, 
                    #           red: n, 
                    #           blue: n
                    #            }
                    # }

        for line in file: 
            # line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

            game_dict = {
                "green": 0,
                "red": 0,
                "blue": 0
            }

            game_id, game = line.split(": ")
            # game_id = "Game 1"
            # game = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

            game_id = int(game_id.split(" ")[1])
            # game_id = 1

            game_sets = game.split("; ")
            # game_sets = ["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"]

            for game_set in game_sets:
                # game_set = "3 blue, 4 red"

                cubes = game_set.split(", ")
                for cube in cubes:
                    # cube = "3 blue"

                    number_of_cubes, color = cube.split(" ")
                    number_of_cubes = int(number_of_cubes)
                    color = color.replace("\n", "")

                    game_dict[color] = max(game_dict[color], number_of_cubes)

            games[game_id] = game_dict


    valid_games = getValidGames(games)
    all_powers = getAllPowers(games)

    total_part1 = sum(valid_games)
    total_part2 = sum(all_powers)


    print(total_part1)
    print(total_part2)



def getValidGames(games, possible_game_rules):

    possible_game_rules = {
        "green" : 13,
        "red" : 12,
        "blue": 14
    }

    valid_games = list(games.keys())

    for game_id in games.keys():
        for color in games[game_id].keys():
            if games[game_id][color] > possible_game_rules[color]:
                valid_games.remove(game_id)
                break

    return valid_games


def getAllPowers(games):
    all_powers = []

    for colors in games.values():
        power = 1
        for number_of_color in tuple(colors.values()):
            power *= number_of_color

        all_powers.append(power)

    return all_powers
        


if __name__ == "__main__":
    main()