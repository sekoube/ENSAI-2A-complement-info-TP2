from business_object.statistic import Statistic
from business_object.Pokemon.AbstractPokemon import AbstractPokemon

Class AllRounderPokemon(AbstractPokemon):

 def _init_(
        self, stat_max=None, stat_current=None, level=0, name=None) -> None:

        # Calling the parent class constructor
        super()._init_(
            stat_max=stat_max,
            stat_current=stat_current,
            level=level,
            name=name      
        ) 
 

    def get_pokemon_attack_coef(self) -> float:
       return 1 + (self.sp_atk_current + self.sp_def_current) / 200