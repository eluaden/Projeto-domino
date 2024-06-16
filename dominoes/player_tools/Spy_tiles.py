# serve pra manter controle das peças no jogo, tanto na mao dos jogadores quanto na propria mesa,

class Spy_tiles: 

    def __init__(self,player_position,player_tiles) -> None:
        #todas as peças do jogo
        self._all_tiles = [(i,k) for i in range(10) for k in range(i,10)]

        #peças de cada jogador, ja jogadas(e no caso  do player, as peças na sua mão)
        self._player_plays = {i:[] for i in range(4)}
        self._player_plays[player_position] = player_tiles


        #posição do jogador
        self._player_position = player_position

        #dicionarios com as peças que os jogadores x:provavelmente tem/ nao tem
        self._probably_dont = {0:[],1:[],2:[],3:[]}

    


    #propriedades
    @property
    def probably_dont(self):
        return self._probably_dont

    #metodos
            
    def turn_update(self,play): #função que a cada turno do player monitora tudo que aconteceu na mesa
        #adiciona as jogadas dos players
        if play[0] != self._player_position:
            self._player_plays[play[0]].append(play[3])
        
        if play[3] is None:
            self.update_probably_dont(play)
            return
        

        if play[3] in self._probably_dont[play[0]]:
            self.update_probably_dont(play)

        

    def update_probably_dont(self,play): #funcao que identifica e atualiza quais peças um jogador provavelmente nao tem
        for extremidade in play[1]:
            for tile in self._all_tiles:
                if extremidade  in tile:
                    self._probably_dont[play[0]] += tile                


                    
