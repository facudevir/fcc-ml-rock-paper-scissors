# RPS.py
#
# Función player para el proyecto Rock Paper Scissors de freeCodeCamp.
# Estrategia:
#  - Guarda el historial del oponente.
#  - Usa cadenas de longitud 3 para predecir la siguiente jugada
#    como un modelo de tipo "Markov" muy simple.
#  - Juega el movimiento que gana contra la predicción.
#
# Esta versión está pensada para ganar consistentemente
# contra los bots de RPS_game.py (quincy, abbey, kris, mrugesh).

# Mapa de qué vence a qué
# R vence a S, P vence a R, S vence a P
counter_move = {"R": "P", "P": "S", "S": "R"}


def player(prev_play, opponent_history=[]):
    """
    prev_play: última jugada del oponente ("R", "P" o "S"),
               o "" en la primera ronda.
    Debe devolver: "R", "P" o "S".
    """

    # Registrar la jugada anterior del oponente
    if prev_play in ["R", "P", "S"]:
        opponent_history.append(prev_play)

    # Jugada por defecto (primeras rondas)
    if len(opponent_history) < 3:
        # Empezamos con algo neutro
        return "R"

    # Longitud de la ventana para buscar patrones
    window_size = 3

    # Tomamos el último patrón de longitud 3 del oponente
    recent_pattern = "".join(opponent_history[-window_size:])

    # Diccionario de transiciones:
    # clave: patrón de 3 jugadas, valor: dict de frecuencias de siguiente jugada
    # Ej: patterns["RPS"]["R"] = cuántas veces después de "RPS" jugó "R"
    patterns = {}

    # Construimos el modelo de patrones recorriento el historial
    for i in range(len(opponent_history) - window_size):
        pattern = "".join(opponent_history[i : i + window_size])
        next_move = opponent_history[i + window_size]

        if pattern not in patterns:
            patterns[pattern] = {"R": 0, "P": 0, "S": 0}
        patterns[pattern][next_move] += 1

    # Predecimos la próxima jugada del oponente según el patrón reciente
    if recent_pattern in patterns:
        move_stats = patterns[recent_pattern]
        # Elegimos la jugada más frecuente luego de este patrón
        predicted_opponent_move = max(move_stats, key=move_stats.get)
    else:
        # Si no tenemos datos para este patrón, usamos la última jugada
        predicted_opponent_move = opponent_history[-1]

    # Devolvemos la jugada que gana contra la predicción
    return counter_move[predicted_opponent_move]
