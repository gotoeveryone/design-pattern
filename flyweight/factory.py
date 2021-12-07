from uuid import uuid4


# このクラスは本来外部から生成させないようにする
class Role:
    def __init__(self, name):
        self.id = uuid4()
        self.name = name


class RoleFactory:
    _roles = {}

    def __new__(cls):
        # Factory が複数作成されないよう Singleton にしておく
        if not hasattr(cls, "_instance"):
            cls._instance = super(RoleFactory, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_role(cls, name: str) -> Role:
        role = cls._roles.get(name)
        if role is None:
            role = Role(name)
            cls._roles[name] = role

        return role
