from abc import ABC, abstractmethod
from random import uniform
from 

class AbstractFormulaAttack(ABC):
    
     def compute_damage(
        self, attacker: AbstractPokemon, defender: AbstractPokemon, random
    ) -> int:
        random = uniform(0.85,1)
        level = 
        power = 
        att = 
        defe = 
        return ((((2*level/5+2)*power*att)/defe *50) +2)*random

    @abstractmethod
    def get_attack_stat():
        pass

    @abstractmethod
    def get_defender_stat():
        pass