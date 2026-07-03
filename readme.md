# ArcadeFSE

A self-contained Python arcade that bundles three classic games into a single launcher: Chess, Pac-Man, and Connect Four. Built with pygame as a solo project to practice game architecture, real-time rendering, and writing competitive game-playing AI from scratch.

## What it is and why

ArcadeFSE is a desktop arcade collection. One launcher opens a main menu, and from there you pick a game. The point of the project was to go beyond following a tutorial: each game ships its own engine, its own menus, and its own game modes, with shared infrastructure (rendering, input, persistence) layered underneath. The Chess engine in particular is the centerpiece, featuring a real evaluation function, search, and an opening book rather than a rules-only implementation.

## Features by game

### Chess
- Full legal-move generation, check, checkmate, and stalemate handling.
- Two modes: Player vs Player and Player vs Computer.
- A from-scratch engine with:
  - Phase-aware Piece-Square Table (PSQT) evaluation that interpolates between opening and endgame tables, so piece placement is scored correctly across the whole game.
  - Move scoring using MVV-LVA-style victim and agressor heuristics, plus history and check bonuses for better move ordering.
  - An opening book loaded from a condensed openings file so games do not always start the same way.
  - An engine-suggestion overlay that draws the best move on the board.
- Puzzles support, puzzle file loading, and sound effects for move, capture, castle, check, promotion, and game over.
- Per-game settings menu.

### Connect Four
- A heuristic AI engine with alpha-beta search, a transposition table (LRU-bounded) for memoization, threat detection (strong and weak threats), and a center-control heuristic.
- A positions-per-second benchmark harness (`positions_per_second.py`) that traverses the game tree to a fixed depth and reports node counts and throughput, useful for profiling the engine.

### Pac-Man
- Classic maze chase with player and ghost movement, a leaderboard persisted to JSON, a game map, and menus.
- Ghost AI with configurable velocity.

## Tech stack
- Python 3 (uses structural pattern matching, so 3.10+).
- pygame for rendering, input, audio, and the main loop.
- Standard library only otherwise (json, time, concurrent.futures for parallel search).

## Project layout
```
main.py                  # launcher: opens main menu, dispatches to games
constants.py             # shared colors and grid/offset constants per game
positions_per_second.py  # Connect Four engine benchmark
utils.py                 # shared drawing and helper utilities
src/
  main_menu/             # top-level arcade menu
  chess/                 # board, engine, PSQT, game modes, menus, assets, puzzles
  connect_four/          # board, engine, game modes, menus, assets
  pacman/                # player, ghosts, map, leaderboard, menus, assets
```

## How to run
1. Install pygame: `pip install pygame` (or `uv pip install pygame`).
2. Run the launcher: `python main.py` (or `py main.py`).
3. Pick a game from the main menu.

Each game returns to the main menu when you exit, so you can move between them without relaunching.

## Notes
- Some games write local state (for example the Pac-Man leaderboard and chess settings under `src/`). These JSON files are expected to be writable next to the source.
- The Connect Four benchmark writes results to `results.txt`. The repo ships with a sample `results.txt` from prior runs.
- Background art was created with DALL-E.

## Status
Personal project, actively tinkered with. The engines are functional and the arcade is playable end to end. There is no release packaging; run from source.
