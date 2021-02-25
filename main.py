# This could be refactored to use classes instead but this was like scripting, so it was fun :D
program_start = 1000
memory = [0] * 3500  # Memory
dp = 3000  # Data pointer
ip = program_start  # Instruction pointer
input_buffer = ""  # input buffer
output_buffer = []  # output buffer
stack = []  # stack


def reset():
    global memory
    global dp
    global ip
    global input_buffer
    global output_buffer
    memory = [0] * 3500
    dp = 3000
    ip = program_start
    input_buffer = ""
    output_buffer = []
    stack = []


def dec_and_exec():
    global dp
    global ip
    global stack
    global memory
    global input_buffer

    if chr(memory[ip]) == ">":
        dp += 1
    elif chr(memory[ip]) == "<":
        dp -= 1
    elif chr(memory[ip]) == "+":
        memory[dp] = (memory[dp] + 1) % 256
    elif chr(memory[ip]) == "-":
        memory[dp] = (abs(memory[dp] - 1)) % 256
    elif chr(memory[ip]) == ".":
        output_buffer.append(chr(memory[dp]))
    elif chr(memory[ip]) == ",":
        memory[dp] = ord(input_buffer[:1]) % 256
        input_buffer = input_buffer[1:]
    elif chr(memory[ip]) == "[":
        if memory[dp] == 0:
            stack.append(ip)
            while stack:
                step()
                if chr(memory[ip]) == "[":
                    stack.append(ip)
                elif chr(memory[ip]) == "]":
                    stack.pop()
    elif chr(memory[ip]) == "]":
        if memory[dp] != 0:
            stack.append(ip)
            while stack:
                step_back()
                if chr(memory[ip]) == "]":
                    stack.append(ip)
                elif chr(memory[ip]) == "[":
                    stack.pop()
    else:
        return True


def step():
    global ip
    ip += 1


def step_back():
    global ip
    ip -= 1


def brain_luck(code, program_input):
    reset()
    global memory
    global input_buffer
    global dp
    global ip
    global stack

    input_buffer = program_input

    # Copy code to memory
    for bi in range(len(code)):
        memory[program_start + bi] = ord(code[bi])

    # Run program
    error_flag = None
    while error_flag != True:
        error_flag = dec_and_exec()
        step()

    return "".join(output_buffer)
