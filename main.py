def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . 7 7 . . . 
                    . . . 7 7 . . . 
                    . . . 7 7 . . . 
                    . . . 7 7 . . .
        """),
        ship,
        0,
        -140)
    projectile.start_effect(effects.cool_radial, 100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite2, otherSprite2):
    scene.camera_shake(4, 500)
    otherSprite2.destroy(effects.disintegrate)
    sprite2.start_effect(effects.fire, 200)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy(effects.disintegrate)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

projectile: Sprite = None
ship: Sprite = None
game.splash("SPACE DESTROYER")
game.splash("CREATE BY SAMAR")
asteroids = [sprites.space.space_small_asteroid1,
    sprites.space.space_small_asteroid0,
    sprites.space.space_asteroid0,
    sprites.space.space_asteroid1,
    sprites.space.space_asteroid4,
    sprites.space.space_asteroid3]
ship = sprites.create(sprites.space.space_red_ship, SpriteKind.player)
ship.set_stay_in_screen(True)
ship.bottom = 120
controller.move_sprite(ship, 100, 100)
info.set_life(3)
effects.star_field.start_screen_effect()

def on_update_interval():
    global projectile
    projectile = sprites.create_projectile_from_side(asteroids[randint(0, len(asteroids) - 1)], 0, 75)
    projectile.set_kind(SpriteKind.enemy)
    projectile.x = randint(10, 150)
game.on_update_interval(500, on_update_interval)
