
import os

class Player():
  def __init__(self, playerid, name, playersymbol):
    self.playerid = playerid
    self.name = name
    self.playersymbol = playersymbol
    self.movements = list()
    
  def player_win(self):
    all_movimientos_ganadores = tuple([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]])
    gano = False
    for movimientos_ganadores in all_movimientos_ganadores:
      movimientos_ganadores_ordenados = sorted(movimientos_ganadores)
      movimientos_ordenados = sorted(self.movements)
      if(movimientos_ganadores_ordenados == movimientos_ordenados):
        gano = True
        break
      
    return gano

class TableroPosicion():
  def __init__(self, posicionid, posicionx, posiciony):
    self.posicionid = posicionid
    self.posicionx = posicionx
    self.posiciony = posiciony
    self.playerid = None
    self.playersymbol = "/"
    
class Tablero():
  def __init__(self):
    self.finished = False
    self.posiciones = list()
    self.__add_posiciones()
    
  def __add_posiciones(self):
    self.posiciones.append(TableroPosicion(1, 0, 0))
    self.posiciones.append(TableroPosicion(2, 0, 1))
    self.posiciones.append(TableroPosicion(3, 0, 2))
    self.posiciones.append(TableroPosicion(4, 1, 0))
    self.posiciones.append(TableroPosicion(5, 1, 1))
    self.posiciones.append(TableroPosicion(6, 1, 2))
    self.posiciones.append(TableroPosicion(7, 2, 0))
    self.posiciones.append(TableroPosicion(8, 2, 1))
    self.posiciones.append(TableroPosicion(9, 2, 2))
    
  def get_position_by_coordinates(self, x, y):
    position_found = None
    
    for position in self.posiciones:
      if position.posicionx == x and position.posiciony == y:
        position_found = position
        break
    
    return position_found
    
  def turno_jugador(self, jugador):
    print('Jugador "' + jugador.name + '", es tu turno')
    
    valorx = int(input("Digite el valor de x: "))
    valory = int(input("Digite el valor de y: "))
    
    position_founded = self.get_position_by_coordinates(valorx, valory)
        
    if position_founded == None:
      raise Exception("Hay una posición que no existe, coordenada x: " + x + "y coordenada y: " + y)
    
    success = self.set_posicion_jugador(jugador.playerid, jugador.playersymbol, position_founded.posicionid)
    
    if success:
      jugador.movements.append(position_founded.posicionid)
      
    return success
    
  def set_posicion_jugador(self, playerid, playersymbol, posicionid):
    position_edited = False
    for posicion in self.posiciones:
      if posicion.posicionid == posicionid and posicion.playerid == None:
        posicion.playerid = playerid
        posicion.playersymbol = playersymbol
        position_edited = True
        break
    
    return position_edited

  def pintar_tablero(self):
    for i in range(3):
      
      tabla_fila = ""
      
      for j in range(3):
        
        position_founded = self.get_position_by_coordinates(j, i)
        
        if position_founded == None:
          raise Exception("Hay una posición que no existe, coordenada x: " + x + "y coordenada y: " + y)
        
        tabla_fila += position_founded.playersymbol
        
      print(tabla_fila)

def main():
  
  jugador1 = Player(1, "Rafael", "x")
  jugador2 = Player(2, "Juanito", "o")
  
  tablero = Tablero()
  
  flag_jugador = True
  primer_jugador_gano = True
  resultado_movimiento = None
  
  while(tablero.finished != True):
    os.system('cls' if os.name == 'nt' else 'clear')
    tablero.pintar_tablero()
    
    jugador_actual = None
    
    if flag_jugador:
      jugador_actual = jugador1
    else:
      jugador_actual = jugador2
      
    resultado_movimiento = tablero.turno_jugador(jugador_actual)
    
    if resultado_movimiento == False:
      continue
    
    success = jugador_actual.player_win()
    
    if success:
      tablero.finished = True
      primer_jugador_gano = flag_jugador
    else:
      flag_jugador = not flag_jugador
    
  os.system('cls' if os.name == 'nt' else 'clear')
  tablero.pintar_tablero()
  
  jugador_ganador = jugador1 if primer_jugador_gano else jugador2
  
  print('El jugador "' + jugador_ganador.name + '" ha ganado')
  print("Fin del juego")
  
main()