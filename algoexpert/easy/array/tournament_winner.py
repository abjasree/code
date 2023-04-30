def tournamentWinner(competitions, results):
    # Write your code here.
    points_dict = {}
    for i in range(len(competitions)):
        if competitions[i][0] not in points_dict.keys():
            points_dict[competitions[i][0]] = 0
        if competitions[i][1] not in points_dict.keys():
            points_dict[competitions[i][1]] = 0
        if results[i] == 0:
            points_dict[competitions[i][1]] += 3
        else:
            points_dict[competitions[i][0]] += 3

    max = 0
    for k in points_dict:
        if points_dict[k] > max:
            winner = k
            max = points_dict[k]
    return winner
