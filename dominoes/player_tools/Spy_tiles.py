# serve pra manter controle das peças no jogo, tanto na mao dos jogadores quanto na propria mesa,

class Spy_tiles: 

    def __init__(self,player_position,player_tiles) -> None:
        # todos as peças do domino cubano
        self._tiles = [(i,j) for i in range(10) for j in range(i,10)] 

        #peças de cada jogador, ja jogadas(e no caso  do player, as peças na sua mão)
        self._player_tiles = {i:[] for i in range(4)}
        self._player_tiles[player_position] = player_tiles

        #peças ordenadas por numeros, vai facilitar a contagem de peças 
        self._numbered_tiles = {i:[tile for tile in self._tiles if i in tile] for i in range(10)}

        #posição do jogador
        self._player_position = player_position


    #propriedades
    @property
    def tiles(self):
        return self._tiles
    
    @property
    def numbered_tiles(self):
        return self._numbered_tiles
    
    @property
    def player_tiles(self):
        return self._player_tiles
    
    @property
    def numbered_tiles(self):
        return self._numbered_tiles
    
    @property
    def player_position(self):
        return self._player_position

    #metodos 
    def turn_update(self,play_hist): #função que a cada turno do player monitora tudo que aconteceu na mesa
        for play in play_hist: 

            #remove as peças do player caso ele tenha jogado, e adiciona nos outros players caso eles tenham jogado
            if play[0] != self._player_positionplayer_position:
                self._player_tiles[play[0]].append(play[3])
            elif play[0] == self._player_position:
                self._player_tiles.remove(play[3])

            #risca das peças que podem ser jogadas, as peças ja jogadas  
            for i in play[3]:
                self._numbered_tiles[i].remove(play[3])      
            

    def update_probably_have(): #funçao pra identifica e atualiza peças que um jogador provavelmente tem
        pass
    def update_probably_dont(): #funcao que identifica e atualiza quais peças um jogador provavelmente nao tem
        pass


#testagem 


teste = Spy_tiles(1,[(1,2)])

teste.turn_update([(0,0,0,(1,2)),(0,0,0,(2,3))])

for tile in teste.numbered_tiles:
    print(tile, teste.numbered_tiles[tile])