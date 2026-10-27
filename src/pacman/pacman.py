import asyncio
from src.pacman.gamemodes.pacman import Pacman
from src.pacman.menus.leaderboard import Leaderboard
from src.pacman.menus.pacman_menu import PacmanMenu

class PacmanGame:
    def __init__(self, screen):
        self.screen = screen

    async def main_loop(self):
        running = True
        game_screen = 'pacman main menu'

        while running:
            match game_screen:
                case 'pacman main menu':
                    game_screen = await self.pacman_main_menu()

                case 'pacman':
                    game_screen = await self.pacman()

                case 'pacman leaderboard':
                    game_screen = await self.leaderboard()
                    
                case 'exit':
                    running = False
                    break
                
        return 'main menu'
    
    async def pacman_main_menu(self):
        pacman_main_menu = PacmanMenu(self.screen)
        return await pacman_main_menu.main_loop()
    
    async def pacman(self):
        pacman = Pacman(self.screen)
        return await pacman.main_loop()
    
    async def leaderboard(self):
        leaderboard = Leaderboard(self.screen)
        return await leaderboard.main_loop()
    