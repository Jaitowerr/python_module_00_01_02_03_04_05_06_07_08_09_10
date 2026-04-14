from typing import cast
from ex0.creature import Creature
from .battle_strategy import BattleStrategy
from ex1.capability import TransformCapability, HealCapability


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        return creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise ValueError(f'Invalid Creature \'{creature.name}\' '
                             'for this aggressive strategy')
        creature_cast = cast(TransformCapability, creature)
        return (f'{creature_cast.transform()}\n'
                f'{creature.attack()}\n'
                f'{creature_cast.revert()}')

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise ValueError(f'Invalid Creature \'{creature.name}\' '
                             'for this defensive strategy')
        crtr_cast = cast(HealCapability, creature)
        return f'{creature.attack()}\n{crtr_cast.heal()}'

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
