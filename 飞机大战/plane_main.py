# -*- coding: utf-8 -*-

"""
@project: 飞机大战
@author: EricNiu
@file: plane_main.py
@ide: PyCharm
"""

import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主程序"""

    def __init__(self):

        print("游戏初始化")
        self.game_over_flag = False

        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT_1, 1000)
        pygame.time.set_timer(CREATE_ENEMY_EVENT_2, 4000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 200)
        pygame.time.set_timer(ENEMY_FIRE_EVENT, 2500)

    def __create_sprites(self):

        bg1 = BackGround()
        bg2 = BackGround(True)
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.elite_enemy_group = pygame.sprite.Group()
        self.enemy_bullets_group = pygame.sprite.Group()
        self.blast_group = pygame.sprite.Group()
        self.game_over_group = pygame.sprite.Group()

    def start_game(self):

        print("游戏开始")

        while True:

            self.clock.tick(60)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()

            pygame.display.update()

    def __event_handler(self):
        if not self.game_over_flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__game_over()

                if event.type == CREATE_ENEMY_EVENT_1:
                    enemy1 = Enemy(ENEMY_IMAGE_1, 3)
                    self.enemy_group.add(enemy1)

                if event.type == CREATE_ENEMY_EVENT_2:
                    enemy2 = EnemyElite(ENEMY_IMAGE_2, 2)
                    print(enemy2)
                    self.elite_enemy_group.add(enemy2)

                if event.type == HERO_FIRE_EVENT:
                    self.hero.fire()

                if event.type == ENEMY_FIRE_EVENT:
                    for enemy in self.elite_enemy_group.sprites():
                        enemy.fire(self.enemy_bullets_group)

                if event.type == ELITE_ENEMY_CRASH_EVENT:
                    print(event.__dict__)
                    blast = Blast(event.__dict__["loc"], ENEMY_CRASH_IMAGE_2, 4)
                    self.blast_group.add(blast)

            key_pressed = pygame.key.get_pressed()

            if key_pressed[pygame.K_RIGHT]:
                self.hero.speed_x = HERO_MOVE_SPEED

            elif key_pressed[pygame.K_LEFT]:
                self.hero.speed_x = -HERO_MOVE_SPEED

            else:
                self.hero.speed_x = 0

            if key_pressed[pygame.K_UP]:
                self.hero.speed_y = -HERO_MOVE_SPEED

            elif key_pressed[pygame.K_DOWN]:
                self.hero.speed_y = HERO_MOVE_SPEED

            else:
                self.hero.speed_y = 0

        else:
            for event in pygame.event.get():
                # 游戏结束 按任意键退出
                if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                    self.__game_over()

    def __check_collide(self):
        # 1.处理普通敌机与英雄子弹的碰撞
        enemy_collided_dict = pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        if enemy_collided_dict:
            for bullet in enemy_collided_dict:
                if bullet in enemy_collided_dict: # 少用 if dict[key]:... 这样的
                    for enemy_collided in enemy_collided_dict[bullet]:
                        blast = Blast(enemy_collided.rect, ENEMY_CRASH_IMAGE_1, 4)  # 生成敌机爆炸精灵
                        self.blast_group.add(blast)

        # 2.处理精英敌机与英雄子弹的碰撞
        elite_enemy_collided_dict = pygame.sprite.groupcollide(self.hero.bullets, self.elite_enemy_group, True, False)
        if elite_enemy_collided_dict:
            for bullet in elite_enemy_collided_dict:
                if bullet in elite_enemy_collided_dict:
                    for enemy_collided in elite_enemy_collided_dict[bullet]:
                        enemy_collided.get_hit()  # 被击中的精英敌人调用更改击中状态的函数

        # 3.双方的子弹碰撞后会消失
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_bullets_group, True, True)

        # 4.处理英雄与敌机或者敌机子弹间的碰撞
        enemy_collide = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        elite_enemy_collide = pygame.sprite.spritecollide(self.hero, self.elite_enemy_group, True)
        enemy_bullet_collide = pygame.sprite.spritecollide(self.hero, self.enemy_bullets_group, True)
        # 被普通敌机撞毁
        if len(enemy_collide):
            for enemy in enemy_collide:
                blast = Blast(enemy.rect, ENEMY_CRASH_IMAGE_1, 4)
                self.blast_group.add(blast)
                self.__hero_crash()
        # 被精英敌机撞毁
        if len(elite_enemy_collide):
            for enemy in elite_enemy_collide:
                blast = Blast(enemy.rect, ENEMY_CRASH_IMAGE_2, 4)
                self.blast_group.add(blast)
            self.__hero_crash()
        # 被敌机子弹击毁
        if len(enemy_bullet_collide):
            for bullet in enemy_bullet_collide:
                bullet.kill()
            self.__hero_crash()

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.elite_enemy_group.update()
        self.elite_enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

        self.enemy_bullets_group.update()
        self.enemy_bullets_group.draw(self.screen)

        self.blast_group.update()
        self.blast_group.draw(self.screen)

        self.game_over_group.update()
        self.game_over_group.draw(self.screen)

    def __hero_crash(self):
        # 处理英雄坠毁的动画，并生成游戏结束精灵类
        self.game_over_flag = True

        blast_hero = Blast(self.hero.rect, HERO_CRASH_IMAGE, 4)
        self.blast_group.add(blast_hero)
        self.hero.kill()

        self.enemy_group.empty()
        self.elite_enemy_group.empty()
        game_over = GameOver()
        self.game_over_group.add(game_over)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
    pygame.quit()
