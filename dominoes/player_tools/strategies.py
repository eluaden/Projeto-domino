#possiveis estrategias a serem tomadas durante a partida pelos players(que podem trocar de estrategia a qualquer momento)

def super_greedy(playable_tiles, player_tiles):
    # Primeiro, seleciona as peças com a maior soma
    tile_sum = -1
    greater_tiles = []
    for tile in playable_tiles:
        current_sum = tile[0] + tile[1]
        if current_sum > tile_sum:
            greater_tiles = [tile]
            tile_sum = current_sum
        elif current_sum == tile_sum:
            greater_tiles.append(tile)

    # Se houver mais de uma peça com a maior soma, desempate baseado na variedade
    if len(greater_tiles) > 1:
        # Conta a frequência de cada face nas peças do jogador
        face_count = {i: 0 for i in range(10)}
        for tile in player_tiles:
            face_count[tile[0]] += 1
            face_count[tile[1]] += 1

        # Escolhe a peça que possui a face mais comum
        best_tile = max(greater_tiles, key=lambda tile: face_count[tile[0]] + face_count[tile[1]])
    elif len(greater_tiles) == 1:
        best_tile = greater_tiles[0]
    else:
        best_tile = None

    return [best_tile]

def blocker(playable_tiles,probably_dont):
    block = []
    for tile in playable_tiles:
        if tile in probably_dont:
            block.append(tile)
    if len(block) == 0:
        block = playable_tiles
    return block
    