import gspread


class Editor:
    def write_cell(self, cell: str) -> None:
        pass

    def read_cell(self, cell: str) -> None:
        pass


class Client(Editor):
    def __init__(self, index: int, name: str):
        self.index = index
        self.name = name
        self.worksheet = None
        self.player = None


class Server(Editor):
    def __init__(self):
        self.sa = gspread.service_account(filename='server_service_account.json')
        self.sh = self.sa.open("Poker")
        self.wks = self.sh.worksheet("Server")
        self.clients = []

    def handshake(self) -> bool:
        if self.wks.acell("A1") == "Server Handshake":
            return True
        return False

    def kick_client(self, client: Client) -> None:
        self.rm_worksheet(client.worksheet)
        del self.clients[client.index]

    def add_client(self, client: Client) -> gspread.worksheet:
        client.index = len(self.clients)
        self.clients.append(client)
        self.create_worksheet(f"Client {client.index}", 1, 3)

    def save_data(self) -> gspread.worksheet:
        pass

    def load_save(self, save: int) -> gspread.worksheet:
        pass

    def create_worksheet(self, worksheet_name: str, row: int, col: int) -> gspread.worksheet:
        self.sh.add_worksheet(worksheet_name, row, col)

    def rm_worksheet(self, worksheet: gspread.worksheet) -> None:
        self.sh.del_worksheet(worksheet)
