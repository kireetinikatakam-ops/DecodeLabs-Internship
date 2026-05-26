#!/usr/bin/env python3
"""
Rule-Based AI Chatbot - Project 1
Industrial Training Kit | DecodeLabs | Batch 2026

A simple, deterministic chatbot using explicit if-else logic and dictionary-based
intent matching. This implements the IPO model: Input → Process → Output.

Key Features:
- Continuous input loop (heartbeat)
- Input sanitization (lowercase, strip whitespace)
- Knowledge base with 5+ intents
- Dictionary lookup with O(1) complexity
- Fallback response for unknowns
- Clean exit command
"""


def main():
    """Main chatbot loop - The Logic Skeleton."""
    
    # ============================================================================
    # PHASE 1: KNOWLEDGE BASE (The Rules Engine)
    # ============================================================================
    # Key-Value pairs: user_input -> bot_response
    # This is a hash map for instant O(1) lookup instead of if-elif chains
    
    responses = {
        'hello': 'Hi there! How can I help you today?',
        'hi': 'Hello! Nice to meet you.',
        'hey': 'Hey! What\'s up?',
        'how are you': 'I\'m doing great! How about you?',
        'what is your name': 'I\'m a Rule-Based AI Chatbot created by DecodeLabs.',
        'who are you': 'I\'m an AI assistant powered by explicit logic rules.',
        'thanks': 'You\'re welcome! Happy to help.',
        'thank you': 'My pleasure! Glad I could assist.',
        'help': 'I can chat with you about various topics. Try: "hello", "how are you", "what is your name"',
        'bye': 'Goodbye! See you next time.',
        'goodbye': 'Take care! Come back soon.',
        'exit': 'Exiting chatbot. Thanks for the conversation!',
        'quit': 'Session ended. Have a great day!',
        'how does this work': 'I use a dictionary of predefined intents and responses. Each input is matched exactly to a rule.',
        'what can you do': 'I can greet you, answer basic questions, and chat. Type "help" for more options.',
    }
    
    # ============================================================================
    # STARTUP MESSAGE
    # ============================================================================
    print("\n" + "="*70)
    print("  RULE-BASED AI CHATBOT v1.0 | DecodeLabs Industrial Training Kit")
    print("="*70)
    print("  Type your message and press Enter. Type 'exit' or 'quit' to leave.")
    print("  Type 'help' to see available commands.")
    print("="*70 + "\n")
    
    # ============================================================================
    # PHASE 2: THE HEARTBEAT - INFINITE LOOP
    # ============================================================================
    # "The organism stays alive until the Kill Command"
    
    while True:
        try:
            # INPUT: Get raw user input
            raw_input = input("You: ").strip()
            
            # SANITIZATION: Handle empty input
            if not raw_input:
                print("Bot: Please say something!\n")
                continue
            
            # SANITIZATION: Convert to lowercase for case-insensitive matching
            clean_input = raw_input.lower().strip()
            
            # ====================================================================
            # PHASE 3: PROCESS - Intent Matching (The Logic Skeleton)
            # ====================================================================
            
            # Check for exit commands first (Kill Command)
            if clean_input in ['exit', 'quit', 'bye', 'goodbye']:
                response = responses.get(clean_input, "Goodbye!")
                print(f"Bot: {response}\n")
                break  # KILL COMMAND - Exit the loop
            
            # Dictionary lookup with fallback (O(1) complexity)
            # This is the ".GET() METHOD" - Atomic operation: Lookup + Fallback
            response = responses.get(
                clean_input,
                "I do not understand. Type 'help' for available commands."
            )
            
            # ====================================================================
            # PHASE 4: OUTPUT - Response Generation
            # ====================================================================
            print(f"Bot: {response}\n")
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\nBot: Interrupted. Session ended.\n")
            break
        except Exception as e:
            # Catch any unexpected errors
            print(f"Bot: An error occurred: {e}\n")
            continue
    
    print("="*70)
    print("  Thank you for using the Rule-Based AI Chatbot!")
    print("  Built with explicit logic, deterministic guardrails, and precision.")
    print("="*70 + "\n")


# ============================================================================
# ENHANCEMENT OPTIONS (Extend this chatbot)
# ============================================================================
# 
# 1. EXPANDED VOCABULARY:
#    Add more intents to the 'responses' dictionary
#    
# 2. NESTED CONDITIONS:
#    Add follow-up logic based on user input patterns
#    Example: if 'weather' in clean_input, provide weather-specific responses
#    
# 3. PERSONALITY:
#    Give the bot a unique tone - formal, casual, humorous, etc.
#    
# 4. STATE MANAGEMENT:
#    Keep track of conversation context across multiple exchanges
#    
# 5. PARTIAL MATCHING:
#    Use fuzzy matching or keyword detection for flexible input handling
#    
# 6. LOGGING:
#    Save conversation history to a file for analysis
#    
# 7. SENTIMENT ANALYSIS:
#    Detect user mood and respond accordingly
#


if __name__ == "__main__":
    main()