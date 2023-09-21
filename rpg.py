from dataclasses import dataclass
@dataclass
class Entidad:
    nombre: str
    salud: int
    energia: int
    ataque_basico: int
    def valor_incial(self):
        self.salud_maxima=self.salud
        self.energia_maxima=self.energia
    def atacar(self,objetivo):
        objetivo.recibir_dano(self.ataque_basico)
    def recibir_dano(self):
        self.salud-=self.dano # falta indicar que el enemigo a muerto
        if self.salud <= 0:
            self.salud=0# falta "desactivar" a la entidad
    def usar_habilidad(self, habilidad, objetivo):
        if habilidad.energia_requerida < self.energia:
            self.energia -= habilidad.energia_requerida
            objetivo.recibir_dano(habilidad.ataque)
        else:
            pass #falta mensaje en caso de que no tenga energia
    def descansar(self):#fijarse si se puede optimizar
        if self.salud > 0:
            energia_recuperada=self.energia_maxima*0.15
            salud_recuperada=self.salud_maxima*0.15
            if self.salud_maxima < salud_recuperada+self.salud:
                pass# indicar que el personaje no puede tener mas que su salud maxima
            if self.energia_maxima < energia_recuperada+self.energia:
                pass# indicar que el personaje no puede tener mas que su energia
            self.salud+=salud_recuperada
            self.energia+=energia_recuperada
        else:
            pass #falta mensaje en el caso que no pueda descansar

@dataclass
class Personaje(Entidad):
    habilidades: list["Habilidad"]
    nivel: int = 1
    experiencia_total: int = 0
    inventario: list["Objeto"]
    def aprender_habilidad(self, habilidad_aprender):
        if len(self.habilidades) <= 3:
            self.habilidades.append(habilidad_aprender)#falta el else
    def olvidar_habilidad(self, habilidad_olvidar):
        if habilidad_olvidar in self.habilidades:
            self.habilidades.remove(habilidad_olvidar) #falta el else
    def experiencia_nivel(self,enemigo):
        self.experiencia_total += enemigo.experiencia
        if self.experiencia_total >= self.nivel*50:
            self.subir_de_nivel()
    def subir_de_nivel(self):
        self.nivel+=1
        self.salud_maxima+=20
        self.energia_maxima+=10
        self.ataque_basico+=10
    def agregar_objeto(self,objeto):
        if len(self.inventario) <=10:
            self.inventario.append(objeto)
        else:
            pass#falta indicacion si hay mas de 10 objeto
    def eliminar_objeto(self):
        pass#falta eliminacion de objeto

@dataclass
class Enemigo(Entidad):
    experiencia: int

@dataclass
class Habilidad:
    nombre: str
    ataque: int
    energia_requerida: int

@dataclass
class Objeto:
    nombre: str
    descripcion: str
