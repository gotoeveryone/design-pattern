from command import BaseCommand
from flyweight.factory import RoleFactory


class FlyweightCommand(BaseCommand):
    def run(self):
        admin1 = RoleFactory.get_role("管理者")
        print(f"admin1 の uuid: {admin1.id}")
        admin2 = RoleFactory.get_role("管理者")
        print(f"admin2 の uuid: {admin2.id}")

        assert admin1.id == admin2.id

        general = RoleFactory.get_role("一般")
        print(f"general の uuid: {general.id}")
