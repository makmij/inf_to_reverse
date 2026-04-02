def priority(op):
    if op in '+-':
        return 1
    if op in '*/':
        return 2
    if op == '^':
        return 3
    return 0


def infix_to_reverse(expr):
    output = []
    stack = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
            continue
        if expr[i].isdigit() or (expr[i] == '.'
                                 and i + 1 < len(expr)
                                 and expr[i + 1].isdigit()):
            num = ''
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                num += expr[i]
                i += 1
            output.append(num)
            continue
        if expr[i] == '(':
            stack.append('(')
            i += 1
            continue
        if expr[i] == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack:
                stack.pop()
                i += 1
                continue
        if expr[i] in '+-*/^':
            while (stack and stack[-1] != '('
                   and priority(stack[-1]) >= priority(expr[i])
                   + (1 if expr[i] == '^' else 0)):
                output.append(stack.pop())
            stack.append(expr[i])
            i += 1
    while stack:
        output.append(stack.pop())
    return ' '.join(output)


def evaluate_rpn(rpn):
    stack = []
    for token in rpn.split():
        if token.replace('.', '').isdigit():
            stack.append(float(token))
        elif token in '+-*/^':
            b, a = stack.pop(), stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)
    return stack[0]


def main():
    print("Введите 'exit' для выхода")

    while True:
        expr = input(">> ").strip()
        if expr.lower() == 'exit':
            break

        try:
            rpn = infix_to_reverse(expr)
            result = evaluate_rpn(rpn)
            print(f"Обратная польская запись: {rpn}")
            print(f"Результат: {result}\n")
        except Exception as e:
            print(f"Ошибка: {e}\n")


if __name__ == "__main__":
    main()
