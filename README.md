# Rule-Based AI Chatbot v1.0

**Industrial Training Kit | DecodeLabs | Batch 2026**

A simple, lightweight, and deterministic chatbot implementation using explicit rule-based logic and dictionary-based intent matching. Perfect for understanding fundamental chatbot architecture and the IPO (Input → Process → Output) model.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Available Commands](#available-commands)
- [Architecture](#architecture)
- [Enhancement Options](#enhancement-options)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Overview

This chatbot demonstrates core concepts in conversational AI without external dependencies. It uses a rule-based approach with a knowledge base of predefined intents and responses, making it ideal for:

- Learning chatbot fundamentals
- Understanding the IPO model in action
- Building deterministic, rule-based systems
- Prototyping before moving to ML-based solutions

The chatbot runs in your terminal and maintains a continuous conversation loop until you exit.

---

## Features

✅ **Lightweight & Self-Contained** - No external dependencies, pure Python  
✅ **O(1) Lookup Complexity** - Instant response matching using dictionary lookup  
✅ **Input Sanitization** - Lowercase conversion and whitespace handling  
✅ **Graceful Error Handling** - Handles empty input, keyboard interrupts, and exceptions  
✅ **Clean Exit** - Multiple exit commands ('exit', 'quit', 'bye', 'goodbye')  
✅ **Extensible Design** - Easy to add new intents and responses  
✅ **Fallback Responses** - Handles unknown inputs gracefully  

---

## Requirements

- Python 3.6 or higher
- No external packages required

To check your Python version:

```bash
python3 --version
```

---

## Installation

1. **Clone or download the script:**
   ```bash
   # If using git
   git clone <repository-url>
   cd chatbot
   ```

2. **Make it executable (optional, on Linux/Mac):**
   ```bash
   chmod +x chatbot.py
   ```

3. **Verify the file exists:**
   ```bash
   ls -la chatbot.py
   ```

---

## Usage

### Run the Chatbot

```bash
python3 chatbot.py
```

Or, if you made it executable on Linux/Mac:

```bash
./chatbot.py
```

### Example Conversation

```
======================================================================
  RULE-BASED AI CHATBOT v1.0 | DecodeLabs Industrial Training Kit
======================================================================
  Type your message and press Enter. Type 'exit' or 'quit' to leave.
  Type 'help' to see available commands.
======================================================================

You: hello
Bot: Hi there! How can I help you today?

You: how are you
Bot: I'm doing great! How about you?

You: what is your name
Bot: I'm a Rule-Based AI Chatbot created by DecodeLabs.

You: thanks
Bot: You're welcome! Happy to help.

You: exit
Bot: Exiting chatbot. Thanks for the conversation!

======================================================================
  Thank you for using the Rule-Based AI Chatbot!
  Built with explicit logic, deterministic guardrails, and precision.
======================================================================
```

---

## How It Works

### The IPO Model

The chatbot follows a simple **Input → Process → Output** pattern:

1. **Input Phase**
   - Captures raw user input from the terminal
   - Removes leading/trailing whitespace
   - Validates for empty input

2. **Process Phase**
   - Converts input to lowercase for case-insensitive matching
   - Performs dictionary lookup in the knowledge base
   - Returns predefined response or fallback message

3. **Output Phase**
   - Displays the bot's response to the user
   - Continues the conversation loop

### The Knowledge Base

The `responses` dictionary stores intent-response pairs:

```python
responses = {
    'hello': 'Hi there! How can I help you today?',
    'how are you': 'I\'m doing great! How about you?',
    # ... more intents
}
```

This design provides **O(1) constant-time lookup**, making the chatbot fast and efficient even with thousands of intents.

### The Heartbeat Loop

The infinite `while True:` loop keeps the chatbot "alive" until an exit command is received:

- **Continuous listening** for user input
- **Exception handling** for interrupts (Ctrl+C)
- **Kill commands** ('exit', 'quit', 'bye', 'goodbye') to cleanly exit

---

## Available Commands

| Command | Response | Action |
|---------|----------|--------|
| `hello`, `hi`, `hey` | Greeting message | Initiates friendly conversation |
| `how are you` | Status response | Shows bot is responsive |
| `what is your name` | Identity response | Reveals bot's origin |
| `who are you` | Identity response | Alternative identity query |
| `thanks`, `thank you` | Appreciation response | Acknowledges gratitude |
| `help` | Instruction list | Shows available commands |
| `how does this work` | Explanation | Describes bot's mechanics |
| `what can you do` | Capability list | Lists bot features |
| `bye`, `goodbye`, `exit`, `quit` | Farewell message | Exits the chatbot cleanly |
| *(anything else)* | Fallback message | Handles unknown inputs |

---

## Architecture

### File Structure

```
chatbot.py
├── main()                          # Entry point
├── PHASE 1: Knowledge Base         # Intent-response dictionary
├── PHASE 2: Heartbeat              # Infinite loop / input capture
├── PHASE 3: Process                # Intent matching logic
├── PHASE 4: Output                 # Response display
└── Exception Handling              # KeyboardInterrupt, general errors
```

### Code Flow

```
START
  ↓
[Initialize Knowledge Base]
  ↓
[Display Welcome Message]
  ↓
[Enter Heartbeat Loop]
  ├─ Get User Input
  ├─ Sanitize & Validate
  ├─ Check for Exit Commands
  ├─ Dictionary Lookup
  ├─ Display Response
  └─ Loop Back to Start (unless exit)
  ↓
[Display Goodbye Message]
  ↓
END
```

---

## Enhancement Options

The code includes suggestions for extending functionality:

### 1. **Expanded Vocabulary**
Add more intents to the `responses` dictionary for broader conversational coverage.

```python
responses['favorite color'] = 'I like all colors equally!'
responses['tell me a joke'] = 'Why did the chatbot go to school? To improve its responses!'
```

### 2. **Nested Conditions**
Implement pattern-based logic for complex interactions.

```python
if 'weather' in clean_input:
    response = "I can't check the weather, but you should try a weather app!"
```

### 3. **Personality**
Customize tone and style (formal, casual, humorous, supportive).

```python
responses['hello'] = 'Yo! What\'s good? 🤖'  # Casual tone
```

### 4. **State Management**
Track conversation context across exchanges.

```python
conversation_history = []
conversation_history.append((raw_input, response))
```

### 5. **Partial Matching**
Use keyword detection for flexible input handling.

```python
if any(word in clean_input for word in ['hello', 'hi', 'hey']):
    response = "Hello! Glad to see you."
```

### 6. **Logging**
Save conversations to a file for analysis.

```python
with open('conversation_log.txt', 'a') as log:
    log.write(f"User: {raw_input}\nBot: {response}\n\n")
```

### 7. **Sentiment Analysis**
Detect user mood and respond accordingly.

```python
if 'sad' in clean_input or 'upset' in clean_input:
    response = "I'm sorry to hear that. How can I help?"
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution:** This script has no dependencies. If you see this error, ensure you're using Python 3.6+.

### Issue: Empty responses or bot doesn't answer
**Solution:** Make sure your input matches an intent exactly (case-insensitive). Use `help` to see available commands.

### Issue: Program won't exit
**Solution:** Type `exit`, `quit`, `bye`, or `goodbye`. You can also press `Ctrl+C` to force exit.

### Issue: "command not found: python3"
**Solution:** 
- On Windows, use `python` instead of `python3`
- On Mac/Linux, install Python 3 via your package manager
  ```bash
  # macOS
  brew install python3
  
  # Ubuntu/Debian
  sudo apt-get install python3
  ```

---

## Learning Objectives

By studying this code, you'll understand:

- ✅ Basic chatbot architecture
- ✅ The IPO (Input → Process → Output) model
- ✅ Dictionary-based lookup systems (O(1) complexity)
- ✅ Exception handling in Python
- ✅ Input validation and sanitization
- ✅ Infinite loops and control flow
- ✅ String manipulation and case normalization

---

## Project Context

This project is part of the **DecodeLabs Industrial Training Kit (Batch 2026)** and serves as a foundational project for understanding:

- Rule-based systems
- Conversational AI basics
- Python best practices
- Clean code principles

---

## Author

**Kireetini Katakam**| DecodeLabs Industrial Training Kit  
**Batch:** 2026

*This project was completed as part of the DecodeLabs training program.*

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for full details.

MIT License allows anyone to use this code freely while giving you credit.

---

## Next Steps

1. **Test all commands** - Try different inputs and explore responses
2. **Modify the knowledge base** - Add your own intents and responses
3. **Experiment with enhancements** - Pick one enhancement option and implement it
4. **Build a variant** - Create a chatbot with a specific personality or domain (e.g., customer support, tutor)

---

## Support & Questions

For questions or issues:
- Review the code comments (they're detailed!)
- Check the "How It Works" section
- Try the "Troubleshooting" section
- Refer to the enhancement options for extending functionality

Happy chatting! 🤖
