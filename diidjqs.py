import random


class Character:
    def __init__(self, name, health, attack, defense, level=1):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = level

    def take_damage(self, damage):
        self.health -= max(damage - self.defense, 0)
        if self.health < 0:
            self.health = 0

    def attack_enemy(self, enemy):
        # 몬스터에게 공격
        damage = max(self.attack - enemy.defense, 0)
        enemy.take_damage(damage)
        print(f"{self.name} 공격! {enemy.name}에게 {damage}의 피해를 입혔습니다.")

    def is_alive(self):
        return self.health > 0


class Monster:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= max(damage - self.defense, 0)
        if self.health < 0:
            self.health = 0

    def attack_player(self, player):
        # 플레이어에게 반격
        damage = max(self.attack - player.defense, 0)
        player.take_damage(damage)
        print(f"{self.name} 공격! {player.name}에게 {damage}의 피해를 입혔습니다.")

    def is_alive(self):
        return self.health > 0


def battle(player, monster):
    print(f"{player.name}과(와) {monster.name}의 전투 시작!")

    while player.is_alive() and monster.is_alive():
        # 플레이어의 공격
        player.attack_enemy(monster)

        if not monster.is_alive():
            print(f"{monster.name}가 처치되었습니다!")
            break

        # 몬스터의 공격
        monster.attack_player(player)

        if not player.is_alive():
            print(f"{player.name}가 처치되었습니다. 게임 오버!")
            break

        # 상태 출력
        print(f"\n{player.name}의 체력: {player.health} / {monster.name}의 체력: {monster.health}")
        print("-" * 30)


# 게임 시작
def game():
    player = Character(name="용사", health=100, attack=20, defense=5)
    monster = Monster(name="고블린", health=50, attack=10, defense=3)

    battle(player, monster)


if __name__ == "__main__":
    game()
