# Python Blackjack

Welcome to Python Blackjack by Josh Baker! To start the game, run the `blackjack.py` file located in this folder, and type 'Y' to play.

## Rules

The aim of blackjack is to get a higher score than the dealer, whilst remaining under 21. Each card is worth face value, with the exception of the King, Queen and Jack all being worth 10, and the ace being worth the most desirable score of either 1 or 11.

Both the player and dealer begin with two cards. The dealer shows the player one card, and the player can see all of their cards at any given time. The score is also indicated at all stages of the game.

Betting rules for this game are simple. You begin with 50 chips, and the rules are as follows:

- If you and the dealer both go bust, nobody wins, and the player gets their chips back.
- If the dealer goes bust, you win 1.5x your initial stake.
- If you go bust, the dealer wins your stake.
- If neither you nor the dealer go bust, then either
    - You win 1.5x your stake if you have the higher score, OR
    - The dealer wins your stake if they have a higher score.
- If you get Blackjack (21), then you win 2x your stake.