#!/usr/bin/env python3
"""
Coin Flip Program - A HILARIOUSLY goofy coin flipping simulator
Now with 200% more chaos, confusion, and cosmic randomness! 🌌
"""

import random
import time
import sys
import datetime

# Global variables for maximum chaos
flip_count = 0
cosmic_energy = 0
quantum_entanglement_level = 0

def get_cosmic_energy():
    """Calculate cosmic energy based on current time and quantum state"""
    global cosmic_energy
    now = datetime.datetime.now()
    cosmic_energy = (now.second * now.microsecond + flip_count * 42) % 1000
    return cosmic_energy

def quantum_flip_logic():
    """The most scientifically accurate (and totally made up) quantum coin flip logic"""
    global quantum_entanglement_level
    
    # Quantum mechanics simulation (totally real, trust me)
    schrodinger_cat = random.choice(['alive', 'dead', 'both', 'neither', 'confused'])
    quantum_entanglement_level += random.randint(1, 10)
    
    # The coin exists in a superposition until observed
    if quantum_entanglement_level > 50:
        quantum_entanglement_level = 0
        return 'Quantum Tails (it flipped in another dimension)'
    
    # Normal quantum flip
    if schrodinger_cat == 'alive':
        return 'Heads (the cat is happy)'
    elif schrodinger_cat == 'dead':
        return 'Tails (the cat is... not)'
    elif schrodinger_cat == 'both':
        return 'Both (quantum superposition achieved!)'
    elif schrodinger_cat == 'neither':
        return 'Neither (the coin is questioning reality)'
    else:
        return 'Confused (the coin needs therapy)'

def animate_chaotic_coin_flip():
    """Animate the coin flipping with maximum chaos"""
    symbols = ['🪙', '💰', '🌌', '🐱', '🤯', '🎭', '🌈', '⚡', '🔮', '🎪']
    messages = ['Flipping...', 'Consulting the cosmos...', 'Asking the quantum field...', 
                'Checking with Schrodinger...', 'Summoning chaos...', 'Reality.exe has stopped working...']
    
    for i in range(15):
        symbol = random.choice(symbols)
        message = random.choice(messages)
        print(f"\r{symbol} {message}", end="", flush=True)
        time.sleep(0.08)
    print()

def flip_coin():
    """The most goofy coin flip function ever created"""
    global flip_count
    flip_count += 1
    
    cosmic_energy = get_cosmic_energy()
    
    # Special cases for maximum goofiness
    if flip_count == 7:
        return 'Lucky 7! (The coin landed on its edge and is now a ruler)'
    elif flip_count % 13 == 0:
        return 'Unlucky 13! (The coin is now cursed and follows you around)'
    elif cosmic_energy > 800:
        return f'Cosmic Energy Overflow! (The coin exploded into {random.randint(5, 20)} smaller coins)'
    elif flip_count == 42:
        return 'The Answer to Everything! (The coin has achieved enlightenment)'
    elif random.random() < 0.05:  # 5% chance
        return 'The coin got stuck in a time loop and is still flipping...'
    elif random.random() < 0.03:  # 3% chance
        return 'The coin landed in another dimension. Please try again.'
    else:
        return quantum_flip_logic()

def get_goofy_commentary():
    """Generate hilariously goofy commentary"""
    comments = [
        "The quantum field is pleased with this result!",
        "Schrodinger's cat approves!",
        "The cosmic balance has been maintained!",
        "Reality.exe is running smoothly!",
        "The multiverse is in harmony!",
        "The coin has spoken with the wisdom of ages!",
        "Physics has been successfully violated!",
        "The universe just winked at you!",
        "Time itself is confused by this result!",
        "The coin has achieved sentience!"
    ]
    return random.choice(comments)

def main():
    """Main program loop with maximum goofiness"""
    print("🌌 Welcome to the CHAOTIC COIN FLIP PROGRAM! 🌌")
    print("Now with 200% more quantum mechanics and cosmic randomness!")
    print("⚠️  Warning: Side effects may include reality distortion, time loops, and existential crises")
    print("=" * 80)
    
    print(f"\n🔮 Current cosmic energy level: {get_cosmic_energy()}")
    print(f"🐱 Schrodinger's cat status: {random.choice(['alive', 'dead', 'both', 'confused'])}")
    
    while True:
        print(f"\n🌌 What would you like to do? (Flip count: {flip_count})")
        print("1. 🌟 Flip a coin (with cosmic energy)")
        print("2. 🎭 Flip multiple coins (quantum batch mode)")
        print("3. 🔮 Check quantum entanglement level")
        print("4. 🐱 Pet Schrodinger's cat")
        print("5. 🚪 Exit the dimension")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            print(f"\n🎯 Single coin flip! (Cosmic energy: {get_cosmic_energy()})")
            animate_chaotic_coin_flip()
            result = flip_coin()
            print(f"🎉 Result: {result}!")
            print(f"💭 {get_goofy_commentary()}")
            
        elif choice == '2':
            try:
                num_flips = int(input("\nHow many coins do you want to flip? (Warning: May cause reality distortion): "))
                if num_flips <= 0:
                    print("❌ The quantum field doesn't understand negative numbers!")
                    continue
                if num_flips > 100:
                    print("⚠️  That many flips might tear a hole in spacetime!")
                    
                print(f"\n🎯 Initiating quantum batch flip mode... ({num_flips} coins)")
                results = {}
                
                for i in range(num_flips):
                    animate_chaotic_coin_flip()
                    result = flip_coin()
                    results[result] = results.get(result, 0) + 1
                    print(f"Flip {i+1}: {result}")
                    
                    # Special quantum effects
                    if i == num_flips // 2:
                        print("🌌 Mid-flip quantum anomaly detected!")
                        print("🔮 The coin is now in a superposition of all possible results!")
                
                print(f"\n📊 Final Results (Quantum Analysis):")
                for result, count in results.items():
                    percentage = (count / num_flips) * 100
                    print(f"{result}: {count} ({percentage:.1f}% of the multiverse)")
                
                print(f"\n🔮 Quantum entanglement level: {quantum_entanglement_level}")
                print(f"🌌 Total cosmic energy generated: {get_cosmic_energy()}")
                
            except ValueError:
                print("❌ The quantum field only understands numbers! (And cats)")
                
        elif choice == '3':
            print(f"\n🔮 Quantum entanglement level: {quantum_entanglement_level}")
            print(f"🌌 Current cosmic energy: {get_cosmic_energy()}")
            print(f"🐱 Schrodinger's cat: {random.choice(['purring', 'plotting', 'existing', 'not existing', 'both'])}")
            
        elif choice == '4':
            cat_states = ['purring happily', 'plotting world domination', 'existing', 'not existing', 
                         'in a quantum superposition', 'demanding treats', 'questioning reality']
            print(f"\n🐱 You pet Schrodinger's cat...")
            print(f"🐱 The cat is {random.choice(cat_states)}")
            if random.random() < 0.3:
                print("🐱 The cat has granted you a quantum blessing! Your next flip will be extra chaotic!")
                
        elif choice == '5':
            print("\n👋 Thanks for visiting our dimension!")
            print("🌌 Remember: In an infinite multiverse, this conversation happened an infinite number of times!")
            print("🐱 Schrodinger's cat waves goodbye (maybe)")
            break
            
        else:
            print("❌ The quantum field doesn't recognize that choice!")
            print("🔮 Please try again (the multiverse is watching)")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🌌 Program interrupted by cosmic forces!")
        print("🐱 Schrodinger's cat is disappointed")
        print("👋 Reality.exe has stopped working. Goodbye!")
        sys.exit(0)