from dao.attack_dao import AttackDao
from business_objet.attack.attack_factory import AttackFactory


class TestAttackDao:
    def test_find_attack_by_id_ok(self):
        # GIVEN
        existing_id_attack = 1

        # WHEN
        attack = AttackDao().find_attack_by_id(existing_id_attack)

        # THEN
        assert attack is not None
        assert attack.id == existing_id_attack

    # Test pour la méthode add_attack()

    def test_add_attack_ok(self):
        # Donné
        attack_a_ajouter = PhysicalFormulaAttack(
                id = 8000,
                power=10,
                name=="pokemon_random",
                description="Pokemon random parce que j'y connais rien ",
                accuracy=10,
                element="eau",)
            
        
        # Opération
        attack = AttackDao().add_attack(attack_a_ajouter)
    
        # Résultat attendu
        assert attack.id is not None  # on peut tester une valeur ?
        assert attack.id == 8000
        assert attack
