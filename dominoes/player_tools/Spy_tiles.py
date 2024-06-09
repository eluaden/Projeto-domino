# serve pra manter controle das peças no jogo, tanto na mao dos jogadores quanto na propria mesa,

class Spy_tiles: 

    def __init__(self,player_position,player_tiles) -> None:
        # todos as peças do domino cubano
        self._tiles = [(i,j) for i in range(10) for j in range(i,10)] 

        #peças de cada jogador, ja jogadas(e no caso  do player, as peças na sua mão)
        self._player_plays = {i:[] for i in range(4)}
        self._player_plays[player_position] = player_tiles

        #peças ordenadas por numeros, vai facilitar a contagem de peças 
        self._numbered_tiles = {i:[tile for tile in self._tiles if i in tile] for i in range(10)}

        #posição do jogador
        self._player_position = player_position

        #dicionarios com as peças que os jogadores x:provavelmente tem/ nao tem
        self._probably_dont = {0:[],1:[],2:[],3:[]}
        self._probably_have = {0:[],1:[],2:[],3:[]}
    


    #propriedades
    @property
    def tiles(self):
        return self._tiles
    
    @property
    def numbered_tiles(self):
        return self._numbered_tiles
    
    @property
    def player_plays(self):
        return self._player_plays
    
    @property
    def numbered_tiles(self):
        return self._numbered_tiles
    
    @property
    def player_position(self):
        return self._player_position
    
    @property
    def probably_dont(self):
        return self._probably_dont

    @property
    def probably_have(self):
        return self._probably_have


    #metodos 
    def turn_update(self,play_hist): #função que a cada turno do player monitora tudo que aconteceu na mesa
        for play in play_hist: 
 
            #adiciona as jogadas dos players
            if play[0] != self._player_position:
                self._player_plays[play[0]].append(play[3])
            
            if play[3] is None:
                self.update_probably_dont(play)
                continue
            if play[3] in self._probably_dont[play[0]]:
                self.update_probably_dont(play)

            #risca das peças que podem ser jogadas, as peças ja jogadas  
            for i in play[3]:
                self._numbered_tiles[i].remove(play[3]) 

        self.update_probably_have()        
         


    def update_probably_have(self): #funçao pra identifica e atualiza peças que um jogador provavelmente tem
        repeticoes = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

        for player in self._player_plays:
            if player != self._player_position:
                for play in self._player_plays[player]:
                    if play != None:
                        repeticoes[play[0]] += 1
                        repeticoes[play[1]] += 1
                        if repeticoes[play[0]] > 2:
                            self._probably_have[player] += [i for i in self._numbered_tiles[play[0]]]
                        if repeticoes[play[1]] > 2:
                            self._probably_have[player] += [i for i in self._numbered_tiles[play[1]]]
                

    def update_probably_dont(self,play): #funcao que identifica e atualiza quais peças um jogador provavelmente nao tem

        if play[3] in self._probably_dont[play[0]]:
            for i in play[3]:
                for tile in self._numbered_tiles[i]:
                    if tile in self._probably_dont[play[0]]:
                        self._probably_dont[play[0]].remove(tile)
        else:
            for ext in play[1]:
    
                self._probably_dont[play[0]] += self._numbered_tiles[ext]


#testagem 


teste = Spy_tiles(1,[(1,2)])

teste.turn_update([(0,(0,2),0,(0,5)),(0,(0,1),0,(0,7)),(0,(0,4),0,(0,6))])

print(teste.probably_have)