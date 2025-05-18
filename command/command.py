

from app.command.config import CommandIdConfig,CommandConfigSecure


class CommandInterface:

    def fetch_info(self):
        pass




class command(CommandInterface):

    def __init__(self):
        pass

    def fetch_info(self, Command: CommandInterface):
        Command.fetch_info()
