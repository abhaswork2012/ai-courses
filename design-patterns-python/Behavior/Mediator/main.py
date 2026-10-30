from air import Airplane
from controlTower import ControlTower

control_tower = ControlTower()

airplane1 = Airplane("IND123", control_tower)
airplane2 = Airplane("AIR234", control_tower)
airplane3 = Airplane("IND456", control_tower)

control_tower.register(airplane1)
control_tower.register(airplane2)

airplane1.send_message()

control_tower.register(airplane3)
airplane2.send_message()