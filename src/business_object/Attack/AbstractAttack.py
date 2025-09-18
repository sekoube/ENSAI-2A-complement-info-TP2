from abc import ABC, abstractmethod


class AbstractAttack(ABC):
    def init(self, power, name, description):
        self.name = name
        self.power = power
        self.description = description
        
    @abstractmethod
    def compute_damage(self, attacker: "AbstractPokemon", defender: "AbstractPokemon") -> int:
        """
         Return the damage of the attack.
         It's an abstract method because some attack will
         have variable damages, others have fixed damages

        Returns:
            int : the damage of the attack
        """
        pass