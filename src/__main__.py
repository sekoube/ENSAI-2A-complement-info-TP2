from business_object.pokemon.AttackerPokemon import AttackerPokemon
from business_object.statistic import Statistic

# Create statistics for the following pokemon
stats_pk1 = Statistic(100, 40, 10, 10, 10, 10)

# Create a pokemon
pk1 = AttackerPokemon(name="pika", stat_current=stats_pk1)

# Print the pokemon (call __str__() method)
print(pk1)
