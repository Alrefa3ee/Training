count = 12
items = [7, 3, 5, 12, 2, 1, 5, 3, 8, 4, 6, 4]
packet_count = 5
items.sort(reverse=True)

ability = int(sum(items) / packet_count)

def get_packet(items: list, ability: int) -> list:
    packet = []
    for item in items:
        if sum(packet) + item <= ability:
            packet.append(item)
    return packet

def get_packets(items: list, ability: int, packet_count: int) -> list:
    packets = []
    for i in range(packet_count):
        packet = get_packet(items, ability)
        packets.append(packet)
        for item in packet:
            items.remove(item)
    return packets

packets = get_packets(items, ability, packet_count)
packets.sort()

for index, packet in enumerate(packets, 1):
    print(f"Items in packet {index} are {' '.join([str(i) for i in packet])}")