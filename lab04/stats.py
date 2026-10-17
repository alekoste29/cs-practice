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
    return {"city": city, "temperature": temp, "date": date}


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

def _means(records):
    total, count = {}, {}
    for r in records:
        total[r["city"]] = total.get(r["city"], 0) + r["temperature"]
        count[r["city"]] = count.get(r["city"], 0) + 1
    return {c: total[c] / count[c] for c in total}

def average_by_city(records):
    return {c: round(m, 1) for c, m in _means(records).items()}

def warmest_city(records):
    means = _means(records)
    return min(means, key=lambda c: (-means[c], c))

