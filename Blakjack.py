import random as R
class Carta:
    def __init__(self,numero,palo):
        self.numero=numero
        self.palo=palo
    
    def elPalo(self):
        losPalos = ["","♥","♦","♣","♠"]
        return losPalos [self.palo]

    def elNumero(self):
        losNumeros = ["","A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        return losNumeros[self.numero]
    
    def __str__(self):
        return "[" + self.elNumero() + " "+self.elPalo() + "]"


class Mazo:
    def __init__(self):
        self.lasCartas=[]
    
    def llenar(self):
        for mazo in range(0,10):
            for numero in range(1,14):
                for palo in range(1,5):
                    self.lasCartas.append(Carta(numero,palo)) 

    def __len__(self):
        return len(self.lasCartas)

    def to_list(self):
        return self.lasCartas


    def __str__(self):
        cad = ""
        for carta in self.lasCartas:
            cad += str(carta)+","
        return cad

    def sacar(self):
        return self.lasCartas.pop(0)
    
    def poner(self,carta):
        self.lasCartas.append(carta)

    def mezclar(self):
        R.shuffle(self.lasCartas)
    
    def mezclarr(self):

        for i in range(500):
            p = R.randint(0,len(self.lasCartas)-1)
            u = R.randint(0,len(self.lasCartas)-1)
            aux = self.lasCartas[p]
            self.lasCartas[p] = self.lasCartas[u]
            self.lasCartas[u] = aux
    def laSuma(self):
        sum = 0
        con = 0
        for car in self.lasCartas:
            if car.numero == 1:
                con += 1
            else:
                if car.numero < 10:
                    sum +=  car.numero
                else:
                    sum += 10
        
        while (con > 0) and (sum + 11 + (con-1) <= 21):
            con -= 1
            sum += 11
        return sum + con 
    def hayCartas(self):
        return len(self.lasCartas) > 0


class JugadorH:#HUMANO

    def __init__(self,fichas,nombre):
        self.nombre = nombre
        self.mano = Mazo()
        self.fichas = fichas

    def sePlanta(self):
        
        suma =  self.mano.laSuma() 
        if suma > 21:
            print(self.nombre,"  ",str(self.mano) , " ",suma," SE PASO!!!")
            print("-------------")    
            return True
        
        print(self.nombre,"  ",str(self.mano) , " ",suma)
        respuesta = input("SE PLANTA ? (S/N)").upper()
        print("-------------")
        if respuesta == 'S':
            print(respuesta)
            print(self.nombre," SE PLANTO CON ", suma)
            print("--------------------------------")
            return True
        return False

    def apuesta(self):
        suApuesta = int(input("HAGA SU APUESTA:"))
        if suApuesta > int(self.fichas):
            suApuesta = self.fichas
            self.fichas -= suApuesta
            print("FICHAS RESTANTES: ",self.fichas)
            return suApuesta
            
        else:
            self.fichas -= suApuesta
            print("FICHAS RESTANTES: ",self.fichas)
            return suApuesta
        # if suApuesta > self.fichas:
        #     suApuesta = self.fichas
            
        #return suApuesta
    
    # def retirarse(self):
    #     input("DESEA RETIRARSE (S/N): ").upper
        

    def retirar():
        pass  
        
class JugadorC:#CROUPIER

    def __init__(self,nombre="SR. CROUPIER"):
        self.nombre = nombre
        self.mano = Mazo()

    def sePlanta(self):
        suma = self.mano.laSuma()

        if suma > 21:
            print(self.nombre,"  ",str(self.mano) , " ",suma," SE PASO!!!")
            print("-------------")    
            return True
        else:
            if suma >= 16:
                print(self.nombre,"  ",str(self.mano) , " ",suma," SE PLANTA!!!")
                print("-------------") 
                return True   
        return False


class BlackJack:

    def __init__(self):
        self.croupier = JugadorC()
        self.losJugadores = []
        self.elMazo = Mazo()
        self.pozo = {}

    def agregarJugadorH(self,nombreJugador,fichas):
        jugador = JugadorH(fichas,nombreJugador)
        self.losJugadores.append(jugador)

    def quitarJugadorH(self,nombreJugador,fichas):
        jugador = JugadorH(fichas,nombreJugador)
        self.losJugadores.remove(jugador)

    # def agregarJugadorB(self,nombreJugador,fichas):
    #     self.losJugadores.append(JugadorB(fichas,nombreJugador))
    
    def hayJugadores(self):
        
        return len(self.losJugadores) > 0

    def apuestas(self):
         for jug in self.losJugadores:
            print(str(jug.nombre))            
            self.pozo.update({jug.nombre:str(jug.apuesta())})

    def repartirCartas(self):        
        for jug in self.losJugadores:
            jug.mano.poner(self.elMazo.sacar())           
        for jug in self.losJugadores:
            jug.mano.poner(self.elMazo.sacar())
        self.croupier.mano.poner(self.elMazo.sacar())
        self.croupier.mano.poner(self.elMazo.sacar())

    def descartar(self):
        for jug in self.losJugadores:
            while jug.mano.hayCartas():
                self.elMazo.poner(jug.mano.sacar())
        
        while self.croupier.mano.hayCartas():
                self.elMazo.poner(self.croupier.mano.sacar())

    def retirarse(self):
        for jug in self.losJugadores:
            JugadorH.retirar()
            respuesta = input(jug.nombre + " DESEA RETIRARSE (S/N):").upper()
            print("-------------")
            if respuesta == 'S':
                print(jug.nombre, "SE RETIRO CON", jug.fichas, "FICHAS")
                self.losJugadores.remove(jug)
                print(len(self.losJugadores))
                


    def jugar(self):
        self.elMazo.llenar()
        self.elMazo.mezclar()
        while self.hayJugadores():
            self.pozo={}
            print("------------------")
            print("HAGAN SUS APUESTAS")
            print("------------------")
            self.apuestas()
            print("------------------")
            print("REPARTIENDO CARTAS")
            print("------------------")
            self.repartirCartas()
            for jug in self.losJugadores:
                print(jug.nombre,"  ",str(jug.mano) , " " ,jug.mano.laSuma())
            print(self.croupier.nombre,"  ",str(self.croupier.mano)," ",self.croupier.mano.laSuma())
            print (self.pozo)
            for jug in self.losJugadores:
                while not jug.sePlanta():
                    jug.mano.poner(self.elMazo.sacar())
            while not self.croupier.sePlanta():
                self.croupier.mano.poner(self.elMazo.sacar())            
            self.ganar()
            self.descartar()
            self.retirarse()
        if self.hayJugadores is not True:
            print("---------------")
            print("JUEGO TERMINADO")
            
    def ganar(self):
        blackjack = 0
        sj = 0
        sc = self.croupier.mano.laSuma()
        for jug in self.losJugadores:
            sj = jug.mano.laSuma()
            if sj > 21:
                    print("-------------")
                    print(jug.nombre ," PIERDE Y LE QUEDAN ", jug.fichas, " FICHAS" )
                    print("-------------")
                    if jug.fichas <= 0:
                        seguir = input(jug.nombre +" ¿DESEA PEDIR MAS FICHAS PARA SEGUIR JUGANDO? S/N" ).upper
                        if seguir == "N":
                            print(jug.nombre ," GRACIAS POR PARTICIPAR")
                            self.losJugadores.remove(jug)
                        else:
                            recarga = input("¿CUANTAS FICHAS?(MAXIMA 1000)" )
                            jug.fichas = recarga
            else:
                if sc > 21:
                    
                    print(jug.nombre ," GANA: ",int(self.pozo[jug.nombre])*2)
                    print("-------------")
                    jug.fichas += int(self.pozo[jug.nombre])*2
                else:
                    if  sj < sc:
                        print("-------------")
                        print(jug.nombre ," PIERDE Y LE QUEDAN ", jug.fichas, " FICHAS" )
                        print("-------------")
                        if jug.fichas <= 0:
                            seguir = input(jug.nombre +" ¿DESEA PEDIR MAS FICHAS PARA SEGUIR JUGANDO? S/N" ).upper
                            if seguir == "N":
                                print(jug.nombre ," GRACIAS POR PARTICIPAR")
                                self.losJugadores.remove(jug)
                            else:
                                recarga = input("¿CUANTAS FICHAS?(MAXIMA 1000)" )
                                jug.fichas = recarga
                    else:
                        if sj > sc:
                            
                            print(jug.nombre," GANA: ",int(self.pozo[jug.nombre])*2)
                            print("-------------")
                            jug.fichas += int(self.pozo[jug.nombre])*2
                        else:
                            
                            print(jug.nombre," EMPATA CON CROUPIER Y SE QUEDA CON SU APUESTA DE: " ,int(self.pozo[jug.nombre])*1)
                            print("-------------")
                            jug.fichas += int(self.pozo[jug.nombre])*1
            

def main():
    """
    m = Mazo()
    m.llenar()
    print(str(m))
    m.mezclar()
    print(str(m))
    """
    print("BIENVENIDOS A LA MESA DE BLACKJACK")
    print("----------------------------------")
    mesa = int(input("¿CUANTOS JUGADORES DESEAN JUGAR? (hasta 7) :"))
    
    

    juego = BlackJack()

    for m in range(0,mesa):
        juego.agregarJugadorH(input("NOMBRE DEL JUGADOR: "),int(input("CONTIDAD DE FICHAS CON LAS QUE INGRESA (maximo 1000) :")))

    # juego.agregarJugadorH("juan",100)
    # juego.agregarJugadorH("pinchame",100)
    juego.jugar()


main()

