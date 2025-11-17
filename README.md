# Text-Based Auto-Battler
#### Video Demo: https://youtu.be/4E3n94io6AI
#### Description: A Python text-based game where two characters fight automatically using elemental powers. Each fighter gets random stats and abilities, then battles it out with colorful attacks until one wins.


## What It Does

Create two fighters by entering their names, and watch them battle automatically. Each character gets random stats (HP, attack, defense, luck) and one of four elements (fire, water, earth, air).

## Game Features

**Element System**
- 🔥 Fire beats Earth (1.5x damage)
- 🪨 Earth beats Water (1.5x damage)
- 💧 Water beats Fire (1.5x damage)
- ༄ Air is neutral against everything (1x damage)

This rock-paper-scissors system means element matchups actually matter

**Random Stats**
- HP: 50-100 (your health pool)
- Attack: 5-25 (bonus damage on all hits)
- Defense: 5-50 (reduces incoming damage)
- Luck: 1-10 (increases chance to use stronger abilities)

**Abilities Per Element**
Each element has four abilities with increasing power (10, 20, 30, 40 damage). Higher luck makes you use the strong ones more often.

**Combat Flow**
Each round starts with a coin flip to decide who attacks first. The attacker picks an ability based on their luck stat, then deals damage calculated as: ability damage + attack stat, multiplied by element effectiveness, minus target's defense (minimum 1 damage). If the defender survives, they counter-attack the same way. Battle continues until someone hits 0 HP.

## How to Run

Make sure Python 3 is installed, then:
python autobattler.py
Enter two names, check the stats, press Enter, and watch the battle!

## Code Structure

**Character class** - Handles individual fighters with their stats, element, abilities, and attack logic. Includes the element effectiveness system and luck-based ability selection with pre-calculated weights for performance.

**AutoBattler class** - Manages the battle flow between two characters, displays stats, handles turn order, and determines the winner.

**Color system** - ANSI color codes make each element visually distinct in the terminal. Fire shows red, water blue, earth yellow, and air white.

## Example Battle

```
Alice (fire 🔥) vs Bob (earth 🪨)
Battle begins!

Round 1:
Alice goes first! Uses firestorm for 38 damage! (Super effective!)
Bob HP: 62
Bob uses stone tomb for 25 damage!
Alice HP: 75
```

## Why This Project

I was inspired by my childhood favourite game Pokemon, I just thought that building a Pokemon type of auto-battler from scratch is the project I wanna build to practice and implement what I have learn soo far during this course.
