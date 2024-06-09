#possiveis estrategias a serem tomadas durante a partida pelos players(que podem trocar de estrategia a qualquer momento)

class Strategy:
    def __init__(self) -> None:
        pass
    
    def choose_tile(playable_tiles,board_extremes):
        return 0,None


class Greedy (Strategy): #estrategia bota gorda
    def __init__(self) -> None:
        super().__init__()

    def choose_tile(self,playable_tiles, board_extremes):

        tile_sum = -1
        for tile in playable_tiles: # seleciona o maior dos tiles e joga ele
            if tile[0] + tile[1] > tile_sum:
                greater_tile = tile
                tile_sum = tile[0] + tile[1]

        for i in range(2):
            for j in range(2): # verifica o lado a ser jogado(talvez possa ser descartado pq o juiz pode corrigir o lado)
                if greater_tile[j] == board_extremes[i]:
                    return i,greater_tile


class FirstPlay (Strategy): #estrategia que escolhe a melhor das suas peças a ser jogada NA PRIMEIRA JOGADA!!
    def __init__(self) -> None:
        super().__init__()
    
    def choose_tile(playable_tiles, board_extremes):
        return 
