from business_object.pokemon.AllRounderPokemon import AllRounderPokemon
from business_object.statistic import Statistic

class TestAllrounder():

    def test_get_pokemon_attack_coef(self):

        # Donné
        sp_atk_current = 100
        sp_def_current = 100
        operation = AllRounderPokemon(
            stat_current=Statistic(sp_atk_current=sp_atk_current, sp_def_current=sp_def_current)
        )
    # Operation
        coef_attack_alllrounder = operation.get_pokemon_attack_coef()

    # resultat attendu
        assert coef_attack_alllrounder == 1.005