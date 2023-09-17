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

@dataclass
class Personaje(Entidad):
    habilidades: list["Habilidad"]
    def aprender_habilidad(self, habilidad_aprender):
        if len(self.habilidades) <= 3:
            self.habilidades.append(habilidad_aprender)#falta el else
    def olvidar_habilidad(self, habilidad_olvidar):
        if habilidad_olvidar in self.habilidades:
            self.habilidades.remove(habilidad_olvidar) #falta el else

@dataclass
class Enemigo(Entidad):
    pass

@dataclass
class Habilidad:
    nombre: str
    ataque: int
    energia_requerida: int