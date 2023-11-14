# パケットの定義
class Packet:
    def __init__(self, source, destination, data):
        self.source = source # 送信元
        self.destination = destination # 宛先
        self.data = data # データ
