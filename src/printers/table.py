def print_table(headers, body):
    # Calcula o tamanho da maior string e o tamanho da linha completa

    all_values = []

    for cell in body:
        all_values.append(str(cell))

    min_cell_width = int(len(max(headers + all_values, key=len)) / 2)

    full_line_width = len(headers) * (min_cell_width) + len(headers) + 1

    # Imprime linha antes do cabeçalho

    print('=' * full_line_width)

    # Imprime celulas do cabeçalho

    print("|", end='')
    for heading in headers:
        print(str(heading).center(min_cell_width), end='|')

    # Imprime linha após o cabeçalho

    print()
    print('=' * full_line_width)

    # Imprime cada linha com divisórias

    for row in body:
        print("|", end='')

        for cell in row:
            print(str(cell).center(min_cell_width), end='|')

        print()
        print('-' * full_line_width)
