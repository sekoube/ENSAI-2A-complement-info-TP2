from business_object.pokemon.AttackerPokemon import AttackerPokemon
from business_object.statistic import Statistic


class TestAttackerPokemon:
    def test_get_pokemon_attack_coef(self):
        # Donné
        speed_current = 100
        attack_current = 100
        # Operation
        operation = AttackerPokemon(stat_current=Statistic(attack_current=attack_current, speed_current=speed_current))
        # resultat attendu
        assert operation.get_pokemon_attack_coef() == 1.005