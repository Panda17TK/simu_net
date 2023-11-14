import networkx as nx
import matplotlib.pyplot as plt

import random

from components.packet import Packet
from components.router import Router

# ノードの実装
class Node:
    def __init__(self, id, router, graph, pos):
        self.id: int = id # ノードの識別ID
        self.router: Router = router # ルーター
        self.graph: nx.Graph = graph # グラフ
        self.pos: dict = pos # 座標

    def send_packet(self, destination, data):
        packet = Packet(self.id, destination, data)
        # グラフ上で送信ノードをハイライsト表示
        self.highlight_node(self.id, 'green')
        return self.router.forward_packet(packet, self)

    def receive_packet(self, packet):
        # グラフ上で受信ノードをハイライト表示
        self.highlight_node(self.id, 'blue')
        print(f"Node {self.id} received packet from Node {packet.source}: {packet.data}")

    def highlight_node(self, node_id, color):
        # グラフ上で特定のノードをハイライト表示する関数
        nx.draw_networkx_nodes(self.graph, self.pos, nodelist=[node_id], node_color=color)
        plt.draw()
        plt.pause(0.5)  # 描画のための一時停止