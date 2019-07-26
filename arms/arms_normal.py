from arms.arms import Arms
from bullet.bullet import Bullet


class Arms_normal(Arms):

    def __init__(self):
        super.__init__(self)

    def shoot(self):
        if not super.shoot(self):
            return False
        if self.bullet_flag in self.bullet_list:
            bullet = Bullet.create_bullet(
                self.bullet_flag, self.bullet_list[self.bullet_flag])
            self.shoot_bullet_list.append(bullet)
        else:
            return False
