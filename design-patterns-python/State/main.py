from bike_mode import BikeMode
from walk_mode import WalkMode
from transport_mode import TransportMode
from transport_service import TransportService

b = BikeMode()
trs = TransportService(b)
trs.eta()
trs.directions()

