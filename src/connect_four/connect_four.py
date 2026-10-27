import asyncio
from src.connect_four.menus.connect_four_menu import ConnectFourMenu
from src.connect_four.gamemodes.player_vs_computer import PlayerVsComputer
from src.connect_four.gamemodes.player_vs_player import PlayerVsPlayer


class ConnectFourGame:
    def __init__(self, screen):
        self.screen = screen
        
    async def main_loop(self):
        running = True
        game_screen = "connect four main menu"

        while running:
            match game_screen:
                case "connect four main menu":
                    game_screen = await self.connect_four_main_menu()
                
                case "player vs player":
                    game_screen = await self.player_vs_player()

                case "player vs computer":
                    game_screen = await self.player_vs_computer()
                
                case "exit":
                    running = False
                    break

        return "main menu"
    
    async def connect_four_main_menu(self):
        main_menu = ConnectFourMenu(self.screen)
        return await main_menu.main_loop()
    
    async def player_vs_player(self):
        player_vs_player = PlayerVsPlayer(self.screen)
        return await player_vs_player.main_loop()
    
    async def player_vs_computer(self):
        player_vs_computer = PlayerVsComputer(self.screen)
        return await player_vs_computer.main_loop()
    
    