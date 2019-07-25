from base.base import Base


class Arms(Base):
    """武器类"""

    def __init__(self):
        super().__init__()
        setting = self.get_config()
        # 基础伤害量
        self.damage = setting['damage']
        # 弹药上限
        self.ammo_limit = setting['ammo_limit']
        # 剩余弹药数量
        self.ammo_count = setting['ammo_count']
        # 使用者
        self.owner = None
        # 可使用的子弹列表
        self.bullet_list = setting['bullet_list']
        # 当前使用的子弹
        self.bullet_flag = ''
        pass

    def shoot(self):
        # 无子弹，不能发射
        if self.ammo_count <= 0:
            return False
        else:
            return True

    def install(self, owner):
        self.owner = owner

    # @typeassert(bullet=Bullet)
    def fill_bullet(self, bulletClass, count):
        flag = bulletClass.getFlag()
        if flag not in self.bullet_list:
            return False
        self.bullet_flag = flag
        if self.ammo_limit <= (self.ammo_count + count):
            self.ammo_count = self.ammo_limit
        else:
            self.ammo_count += count
        return True
