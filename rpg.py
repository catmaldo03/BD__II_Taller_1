from dataclasses import dataclass,field
@dataclass
class Entidad:
    nombre: str
    salud: int
    energia: int
    ataque_basico: int
    def valor_incial(self):
        self.salud_maxima=self.salud
        self.energia_maxima=self.energia
    def atacar(self,enemigo):
      if enemigo.salud>0:
        enemigo.recibir_dano(self.ataque_basico)
        if enemigo.salud <= 0:
            if type(enemigo)== Enemigo:
                self.experiencia_nivel(enemigo)
                if enemigo.drop != None:
                    self.agregar_objeto(enemigo.drop)
            else:
                self.experiencia_nivel(enemigo)
      else:
        print(f"{enemigo.nombre} esta muerto no se puede atacar")
    def recibir_dano(self,dano):
        self.salud-=dano
        if self.salud <= 0:
            self.salud=0
            print(f"{self.nombre} ha perdido {dano} de vida, tiene {self.salud} de vida")
            print(f"{self.nombre} ha muerto.")
        else:
            print(f"{self.nombre} ha perdido {dano} de vida, tiene {self.salud} de vida")#esto se hace porque sino sale que tiene -10 de vida
    def usar_habilidad(self, habilidad, objetivo):
      if objetivo.salud>0:
        if habilidad.energia_requerida <= self.energia:
            self.energia -= habilidad.energia_requerida
            print(f"{self.nombre} ha usado {habilidad.nombre}")
            objetivo.recibir_dano(habilidad.ataque)
            if objetivo.salud <= 0:
                self.experiencia_nivel(objetivo)
                if type(objetivo)== Enemigo:
                    if objetivo.drop != None:
                        self.agregar_objeto(objetivo.drop)
                else:
                    pass
        else:
           print(f"{self.nombre} no puede usar {habilidad.nombre}, no tiene suficiente energia")
      else:
        print(f"El {objetivo.nombre} esta muerto, no se puede ocupar la habilidad")
    def descansar(self):
        if self.salud > 0:
            energia_recuperada=self.energia_maxima*0.15
            salud_recuperada=self.salud_maxima*0.15
            if self.salud_maxima < salud_recuperada+self.salud:
                salud_recuperada=self.salud_maxima-self.salud
            if self.energia_maxima < energia_recuperada+self.energia:
                energia_recuperada=self.energia_maxima-self.energia
            self.salud+=salud_recuperada
            self.energia+=energia_recuperada
            print(f"{self.nombre} descanso y recupero 15% de su energia({self.energia}) y salud({self.salud})")
        else:
            print(f"{self.nombre}, esta muerto, no puede descansar")

@dataclass
class Personaje(Entidad):
    habilidades: list["Habilidad"]= field(default_factory=list)
    nivel: int = 1
    experiencia_total: int = 0
    inventario: list["Objeto"] = field(default_factory=list)
    def __post_init__(self):
        self.valor_incial()
    def aprender_habilidad(self, habilidad_aprender):
        if len(self.habilidades) < 3:
            self.habilidades.append(habilidad_aprender)
            print(f"{self.nombre} ha aprendido {habilidad_aprender.nombre}")
        else:
            print(f"{self.nombre} ya tiene 3 habilidades, no puede aprender mas")
    def olvidar_habilidad(self, habilidad_olvidar):
        if habilidad_olvidar in self.habilidades:
            self.habilidades.remove(habilidad_olvidar)
            print(f"{self.nombre} ha olvidado {habilidad_olvidar.nombre}") 
        else:
            print(f"{self.nombre} no posee esa habilidad, no la puede olvidar")
    def experiencia_nivel(self,enemigo):
        if type(enemigo)== Enemigo:
            self.experiencia_total += enemigo.experiencia
            print(f"{self.nombre} ha ganado {enemigo.experiencia}, tiene en total {self.experiencia_total} de experiencia")
            if self.experiencia_total >= self.nivel*50:
                self.subir_de_nivel()
        else:
            self.experiencia_total += enemigo.experiencia_total
            print(f"{self.nombre} ha ganado {enemigo.experiencia_total}, tiene en total {self.experiencia_total} de experiencia")
            if self.experiencia_total >= self.nivel*50:
                self.subir_de_nivel()
    def subir_de_nivel(self):
        self.nivel+=1
        self.salud_maxima+=20
        self.energia_maxima+=10
        self.ataque_basico+=10
        print(f"{self.nombre} ha subido a nivel {self.nivel}")
        print(f"{self.nombre} tiene {self.salud_maxima} de vida maxima,tiene {self.energia_maxima} de energia maxima,tiene {self.ataque_basico} de ataque")
    def agregar_objeto(self,objeto):
        if len(self.inventario) <10:
            self.inventario.append(objeto)
            print(f"{objeto.nombre} ha sido agregado al inventario")
        else:
            print(f"no se ha sido posible agregar {objeto.nombre}, el inventario esta lleno")
    def eliminar_objeto(self,objeto):
        if objeto in self.inventario:
            self.inventario.remove(objeto)
            print(f"{objeto.nombre} ha sido eliminado del inventario")
        else:
            print(f"{objeto.nombre} no esta en el invetario, no se puede eliminar")
    def tomar_pocion(self,pocion):
        if pocion in self.inventario and type(pocion)== Pocion:
            if pocion.tipo =='salud':
                if pocion.nivel ==1:
                    self.salud+=self.salud_maxima*0.2
                    if self.salud_maxima < self.salud:
                        self.salud = self.salud_maxima
                    print(f"{self.nombre} ha tomado una pocion de {pocion.tipo} de nivel {pocion.nivel}, ha recuperado 20% de su {pocion.tipo}, ahora tiene {self.salud} de vida")
                elif pocion.nivel == 2:
                    self.salud+=self.salud_maxima*0.35
                    if self.salud_maxima < self.salud:
                        self.salud = self.salud_maxima
                    print(f"{self.nombre} ha tomado una pocion de {pocion.tipo} de nivel {pocion.nivel}, ha recuperado 35% de su {pocion.tipo}, ahora tiene {self.salud} de vida")
                elif pocion.nivel == 3:
                    self.salud+=self.salud_maxima*0.5
                    if self.salud_maxima < self.salud:
                        self.salud = self.salud_maxima
                    print(f"{self.nombre} ha tomado una pocion de {pocion.tipo} de nivel {pocion.nivel}, ha recuperado 50% de su {pocion.tipo}, ahora tiene {self.salud} de vida")
                
            elif pocion.tipo == 'enegia':
                if pocion.nivel ==1:
                    self.energia+=self.energia_maxima*0.2
                    if self.energia_maxima < self.energia:
                        self.energia = self.energia_maxima
                    print(f"{self.nombre} ha tomado una pocion de {pocion.tipo} de nivel {pocion.nivel}, ha recuperado 20% de su {pocion.tipo}, ahora tiene {self.energia} de energia")
                elif pocion.nivel == 2:
                    self.energia+=self.energia_maxima*0.35
                    if self.energia_maxima < self.energia:
                        self.energia = self.energia_maxima
                    print(f"{self.nombre} ha tomado una pocion de {pocion.tipo} de nivel {pocion.nivel}, ha recuperado 35% de su {pocion.tipo}, ahora tiene {self.energia} de energia")
                elif pocion.nivel == 3:
                    self.energia+=self.energia_maxima*0.5
                    if self.energia_maxima < self.energia:
                        self.energia = self.energia_maxima
                    print(f"{self.nombre} ha tomado una pocion de {pocion.tipo} de nivel {pocion.nivel}, ha recuperado 50% de su {pocion.tipo}, ahora tiene {self.energia} de energia")
            self.eliminar_objeto(pocion)
        else:
            print(f"{self.nombre} no tiene esa pocion")

@dataclass
class Enemigo(Entidad):
    experiencia: int
    drop: "Objeto" or None

@dataclass
class Habilidad:
    nombre: str
    ataque: int
    energia_requerida: int

@dataclass
class Objeto:
    nombre: str
    descripcion: str
@dataclass
class Pocion(Objeto):
    tipo: str
    nivel: int
