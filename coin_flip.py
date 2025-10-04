#!/usr/bin/env python3
"""
Coin Flip Program - A simple but entertaining coin flipping simulator
"""

import random
import time
import sys

def animate_coin_flip():
    """Animate the coin flipping with some visual flair"""
    symbols = ['🪙', '💰', '🪙', '💰']
    for _ in range(10):
        print(f"\r{random.choice(symbols)} Flipping...", end="", flush=True)
        time.sleep(0.1)
    print()

def flip_coin():
    """Flip a coin and return the result"""
    return random.choice(['Heads', 'Tails'])

def main():
    """Main program loop"""
    print("🪙 Welcome to the Amazing Coin Flip Program! 🪙")
    print("=" * 50)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Flip a coin")
        print("2. Flip multiple coins")
        print("3. Quit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            print("\n🎯 Single coin flip!")
            animate_coin_flip()
            result = flip_coin()
            print(f"🎉 Result: {result}!")
            
        elif choice == '2':
            try:
                num_flips = int(input("\nHow many coins do you want to flip? "))
                if num_flips <= 0:
                    print("❌ Please enter a positive number!")
                    continue
                    
                print(f"\n🎯 Flipping {num_flips} coins...")
                results = {'Heads': 0, 'Tails': 0}
                
                for i in range(num_flips):
                    animate_coin_flip()
                    result = flip_coin()
                    results[result] += 1
                    print(f"Flip {i+1}: {result}")
                
                print(f"\n📊 Final Results:")
                print(f"Heads: {results['Heads']}")
                print(f"Tails: {results['Tails']}")
                
            except ValueError:
                print("❌ Please enter a valid number!")
                
        elif choice == '3':
            print("\n👋 Thanks for playing! Goodbye!")
            break
            
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. Goodbye!")
        sys.exit(0)