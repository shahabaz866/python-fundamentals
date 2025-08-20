import math
import datetime

# Memory and history
memory = 0
history = []
last_result = None

def evaluate(expr):
    """Evaluate a math expression safely with memory, history, and ans."""
    global memory, last_result

    # Allowed names/functions
    allowed = {
        "pi": math.pi,
        "e": math.e,
        "sqrt": math.sqrt,
        "abs": abs,
        "round": round,
        "mem": memory,
        "ans": last_result,
    }

    try:
        result = eval(expr, {"__builtins__": None}, allowed)
        history.append((datetime.datetime.now(), expr, result))
        last_result = result
        return result
    except Exception as e:
        return f"Error: {e}"

def show_history(n=None):
    for i, (ts, expr, res) in enumerate(history[-n:] if n else history, 1):
        print(f"{i}. [{ts.strftime('%H:%M:%S')}] {expr} = {res}")

def calculator():
    global memory
    print("\n🔢 Real-World Calculator")
    print("Type math expressions directly (e.g. 5+2*3)")
    print("Commands: :h (history), :m+ <expr>, :m- <expr>, :mr, :mc, :q (quit)")
    print("-" * 50)

    while True:
        expr = input("calc> ").strip()

        # Quit
        if expr == ":q":
            print("👋 Goodbye!")
            break

        # History
        elif expr.startswith(":h"):
            parts = expr.split()
            n = int(parts[1]) if len(parts) > 1 else None
            show_history(n)

        # Memory recall
        elif expr == ":mr":
            print("MEM =", memory)

        # Memory clear
        elif expr == ":mc":
            memory = 0
            print("Memory cleared.")

        # Memory add/subtract
        elif expr.startswith(":m+"):
            val = evaluate(expr[3:].strip())
            if isinstance(val, (int, float)):
                memory += val
                print("MEM =", memory)

        elif expr.startswith(":m-"):
            val = evaluate(expr[3:].strip())
            if isinstance(val, (int, float)):
                memory -= val
                print("MEM =", memory)

        # Normal expression
        else:
            print(evaluate(expr))

# Run calculator
if __name__ == "__main__":
    calculator()
