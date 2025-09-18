from business_objet.Attack.AbstractAttack import AbstractAttack
from business_objet.pokemon.AbstractPokemon import AbstractPokemon


class FixedDamageAttack(AbstractAttack):
    def compute_damage(
        self, attacker: AbstractPokemon, defender: AbstractPokemon
    ) -> int:
        return self.power