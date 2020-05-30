def perform_operation(operator, *values):
    print(operator, values)
    expression = ''
    for v in values[:-1]:
        expression += str(v) + " " + operator + " "
    expression += str(values[-1])

    print(expression, ' = ', eval(expression))


# perform_operation("+", 10, 20, 30)
# perform_operation("*", 5, 6, 7)


sum_tuple = (10, 20, 30)

multiply_tuple = (5, 6, 7)

# perform_operation("+", sum_tuple)
# perform_operation("*", multiply_tuple)

# unpacking arguments
perform_operation("+", *sum_tuple)
# perform_operation("+", 10, 20, 30)
perform_operation("*", *multiply_tuple)

