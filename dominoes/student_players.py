from basic_players import Player
from player_tools import strategies
from player_tools import Spy_tiles

class Super_Greedy(Player):

    def __init__(self):
        super().__init__(0, "Super_Greedy")
        

    def play(self, board_extremes, play_hist):
        if len(play_hist) == 0:
            playable_tiles = self._tiles
            
        else:
            playable_tiles = [tile for tile in self._tiles if tile[0] in board_extremes or tile[1] in board_extremes]
        

        playable_tiles = strategies.super_greedy(playable_tiles,self._tiles) # chama a estrategia supergreedy

        if len(playable_tiles) == 0:
            return 0,None
        else:
            return 0, playable_tiles[-1]

class Blocker(Player):

    def __init__(self):
        super().__init__(0, "Blocker")
        #inicialisa o espião, uma classe que cuida das possibilidades de peças com outros jogadores
        self._spy = Spy_tiles.Spy_tiles(self.position, self.tiles)

        #verifica o jogador seguinte para que ele seja o alvo do bloqueio
        if self._position < 3:
            self._target = self._position + 1
        else:
            self._target = 0
        

    def play(self, board_extremes, play_hist):
        
        if len(play_hist) == 0:
            playable_tiles = self._tiles
        else:
            self._spy.turn_update(play_hist[-1])
            playable_tiles = [tile for tile in self._tiles if tile[0] in board_extremes or tile[1] in board_extremes]
        
        playable_tiles = strategies.blocker(playable_tiles,self._spy.probably_dont[self._target])
        playable_tiles = strategies.super_greedy(playable_tiles,self._tiles)

        if len(playable_tiles) == 0:
            return 0,None
        else:
            return 0, playable_tiles[-1]
        

# Função que define o nome da dupla:
def pair_name():
    return "Avoid and Block"

# Função que cria a dupla:
def create_pair():
    return (Super_Greedy(), Blocker())
