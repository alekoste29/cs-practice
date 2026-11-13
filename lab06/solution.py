paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

# count_by_extension(paths)   # {"pdf": 1, "txt": 1, "png": 1, "": 1}
# deepest_path(paths)         # "docs/img/logo.png"

# human_size(900)             # "900 Б"
# human_size(1536)            # "1.5 КБ"
# human_size(5 * 1024 * 1024) # "5.0 МБ"


def count_by_extension(paths):
    extensions = {}
    for path in paths:
        name = path.split('/')[-1]          # смотрим только на имя файла, не на папки
        if '.' in name:
            extension = name.split('.')[-1].lower()
        else:
            extension = ''
        extensions[extension] = extensions.get(extension, 0) + 1
    return extensions


def deepest_path(paths):
    # глубина = количество частей пути; при равенстве берётся первый
    return max(paths, key=lambda path: len(path.split('/')))


def human_size(size):
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    if size < 1024:
        return f"{size} Б"
    value = size
    unit = 0
    while value >= 1024 and unit < len(units) - 1:
        value /= 1024
        unit += 1
    return f"{value:.1f} {units[unit]}"


if __name__ == "__main__":
    print(count_by_extension(paths))
    print(deepest_path(paths))
    print(human_size(900))
    print(human_size(1536))
    print(human_size(5 * 1024 * 1024))
