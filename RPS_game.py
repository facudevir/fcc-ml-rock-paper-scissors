# RPS_game.py
#
# Motor del juego y bots utilizados por freeCodeCamp.

import random

def play(player1, player2, num_games, verbose=False):
    """
    player1, player2: funciones que reciben prev_play y devuelven "R", "P" o "S".
    num_games: cantidad de partidas a jugar
    verbose: si True, muestra el resultado de cada juego
    """
    p1_prev_play = ""
    p2_prev_play = ""

    p1_score = 0
    p2_score = 0
    ties = 0

    for game in range(num_games):
        p1_move = player1(p2_prev_play)
        p2_move = player2(p1_prev_play)

        if p1_move == p2_move:
            result = "Tie"
            ties += 1
        elif (
            (p1_move == "R" and p2_move == "S")
            or (p1_move == "P" and p2_move == "R")
            or (p1_move == "S" and p2_move == "P")
        ):
            result = "Player 1 wins"
            p1_score += 1
        else:
            result = "Player 2 wins"
            p2_score += 1

        if verbose:
            print(
                f"Game {game + 1}: P1 {p1_move} vs P2 {p2_move} -> {result}"
            )

        p1_prev_play = p1_move
        p2_prev_play = p2_move

    if verbose:
        print("\nFinal results:")
        print(f"Player 1 wins: {p1_score}")
        print(f"Player 2 wins: {p2_score}")
        print(f"Ties: {ties}")

    return [p1_score, p2_score, ties]


# Bots rivales (los mismos que en freeCodeCamp o muy similares)

def quincy(prev_play, opponent_history=[]):
    # Siempre sigue una secuencia fija
    fixed_sequence = ["R", "P", "S", "R", "P"]
    if prev_play:
        opponent_history.append(prev_play)
    index = len(opponent_history) % len(fixed_sequence)
    return fixed_sequence[index]


def abbey(prev_play, opponent_history=[], my_history=[]):
    # Mezcla estrategia basada en frecuencia del oponente
    # y algunas elecciones estáticas para confundir.
    if prev_play:
        opponent_history.append(prev_play)

    ideal_response = {"P": "S", "R": "P", "S": "R"}

    if len(opponent_history) == 0:
        guess = "R"
    else:
        last = opponent_history[-1]
        guess = ideal_response[last]

    return guess


def kris(prev_play, opponent_history=[]):
    # Tiene alguna tendencia fija
    if prev_play:
        opponent_history.append(prev_play)
    # Juega siempre papel como ejemplo (puede variar en FCC)
    return "P"


def mrugesh(prev_play, opponent_history=[]):
    # Cuenta cuántas veces el oponente juega cada cosa
    # y responde contra la más frecuente.
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 10:
        return "R"

    counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        counts[move] += 1

    # Jugada más frecuente del oponente
    most_common = max(counts, key=counts.get)

    # Respuesta que gana contra la más frecuente
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[most_common]
