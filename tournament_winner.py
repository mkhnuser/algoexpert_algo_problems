def tournamentWinner(competitions, results):
    score_table = {}

    for i in range(len(results)):
        point = results[i]
        competition = competitions[i]

        if point == 0:
            winner = competition[1]
        else:
            # NOTE: point == 1
            winner = competition[0]

        # NOTE: defaultdict from collections can help.
        if winner not in score_table:
            score_table[winner] = 3
        else:
            score_table[winner] += 3

    highest_score = 0
    winner_name = ""

    for item in score_table.items():
        name, score = item

        if score > highest_score:
            highest_score = score
            winner_name = name

    return winner_name


if __name__ == "__main__":
    print(
        tournamentWinner(
            competitions=[["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]],
            results=[0, 0, 1],
        )
    )
