def parse_record(line):
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"нужно 3 поля, получено {len(parts)}")
    city, temp, date = (p.strip() for p in parts)
    if not city or not date:
        raise ValueError("пустой город или дата")
    try:
        temp = float(temp)
    except ValueError:
        raise ValueError(f"температура не число: {parts[1]!r}")
    return {"city": city, "temp": temp, "date": date}


def read_valid(lines):
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records

