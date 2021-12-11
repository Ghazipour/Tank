import tank
import enemy
tankfired = False
print('Game started.  ')
tankfired = tank.fire()
if tankfired:
    enemy.dead()
