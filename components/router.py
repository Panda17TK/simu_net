import random
import networkx as nx
import matplotlib.pyplot as plt


# ルーター
class Router:
    def __init__(self, routing_algorithm, graph, pos):
        self.connections = {} # 各ノードIDに対応するNodeインスタンスを格納する辞書
        self.routing_algorithm = routing_algorithm # パケットをルーティングするためのアルゴリズム関数
        self.graph: nx.Graph = graph # ネットワークトポロジーを表すNetworkXのグラフオブジェクト
        self.pos: dict = pos # 各ノードの位置情報を格納する辞書

    def connect(self, node):
        self.connections[node.id] = node

    def forward_packet(self, packet, source_node):
        if self.routing_algorithm(self, packet):
            # パケットが正常に送信された場合、エッジをハイライト表示
            self.highlight_edge(source_node.id, packet.destination, 'green')
            return True
        else:
            # パケット送信に失敗した場合、エッジをハイライト表示
            self.highlight_edge(source_node.id, packet.destination, 'red')
            return False
    def forward_packet_central(self, packet):
        # コントローラーから経路を取得してパケットを転送
        route = self.controller.get_route(packet.source, packet.destination)
        # ルートに従ってパケットを次のノードに転送するロジック
        pass

    def direct_routing(self, packet):
        if packet.destination in self.connections:
            self.connections[packet.destination].receive_packet(packet)
            return True
        else:
            print(f"No route to destination {packet.destination}")
            return False

    def random_routing(self, packet):
        # ランダムルーティングはランダムな目的地を選びます。
        destination = random.choice(list(self.connections.keys()))
        self.connections[destination].receive_packet(packet)
        return True

    def highlight_edge(self, source, destination, color):
        # グラフ上で特定のエッジをハイライト表示する関数
        nx.draw_networkx_edges(self.graph, self.pos, edgelist=[(source, destination)], edge_color=color, width=2)
        plt.draw()
        plt.pause(0.5)  # 描画のための一時停止
