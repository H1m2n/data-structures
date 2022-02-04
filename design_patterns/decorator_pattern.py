class BaseRoomCharge:
    cost = 1000

    def get_cost(self):
        return self.cost


class RoomServiceCharge(BaseRoomCharge):
    cost = 50

    def __init__(self):
        self.base_room_charge = BaseRoomCharge

    def get_cost(self):
        return self.base_room_charge().get_cost() + self.cost


class InRoomPurchaseCharge(BaseRoomCharge):
    cost = 100

    def __init__(self):
        self.base_room_charge = BaseRoomCharge

    def get_cost(self):
        return self.base_room_charge().get_cost() + self.cost


room_service_charge = RoomServiceCharge()
print(room_service_charge.get_cost())

in_room_purchase_charge = InRoomPurchaseCharge()
print(in_room_purchase_charge.get_cost())

# if someone has used both RoomService and InRoomPurchase then we can calculate cost like this
