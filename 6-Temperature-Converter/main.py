# main.py

def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9
def c_to_k(c): return c + 273.15
def k_to_c(k): return k - 273.15
def f_to_k(f): return c_to_k(f_to_c(f))
def k_to_f(k): return c_to_f(k_to_c(k))

def convert(value, from_unit, to_unit):
    u = from_unit.lower()
    v = to_unit.lower()
    if u == v: return value
    if u == "c":
        if v == "f": return c_to_f(value)
        if v == "k": return c_to_k(value)
    elif u == "f":
        if v == "c": return f_to_c(value)
        if v == "k": return f_to_k(value)
    elif u == "k":
        if v == "c": return k_to_c(value)
        if v == "f": return k_to_f(value)
    raise ValueError("Unsupported unit. Use C, F, or K.")

def main():
    print("Temperature Converter (C/F/K)")
    print("Enter value and units like: 100 C F (from C to F)")
    while True:
        try:
            line = input("> ").strip()
            if line.lower() in {"q", "quit", "exit"}:
                print("Goodbye.")
                break
            parts = line.split()
            if len(parts) != 3:
                print("Format: <value> <from_unit> <to_unit> (e.g., 32 F C)")
                continue
            value = float(parts[0])
            from_unit = parts[1]
            to_unit = parts[2]
            result = convert(value, from_unit, to_unit)
            print(f"{value} {from_unit.upper()} = {result:.2f} {to_unit.upper()}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
