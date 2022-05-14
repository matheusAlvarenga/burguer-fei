def find_one_in_array(array, filter_func, default=False):
    # returna o primeiro item do array que filtro(item) é True
    # se nenhum for encontrado retorna o valor default
    return next(filter(filter_func, array), default)
