from arms.arms import Arms


class Arms_normal(Arms):

    def __init__(self):
        super.__init__(self)

    def shoot(self):
        if not super.shoot(self):
            return False
