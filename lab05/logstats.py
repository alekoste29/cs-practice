def parse_event(line):
    parts = line.strip().split(maxsplit=2)
    if len(parts) < 3 or parts[1] not in ('DEBUG', 'INFO', 'WARNING', 'ERROR'):
        raise ValueError('негодная строка')
    time, level, message = parts
    return {'time': time, 'level': level, 'message': message}

def count_levels(lines):
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            level = parse_event(line)['level']
        except ValueError:
            level = 'BROKEN'
        counts[level] = counts.get(level, 0) + 1
    return counts


def top_errors(lines, n):
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event['level'] == 'ERROR':
            counts[event['message']] = counts.get(event['message'], 0) + 1
    result = sorted(counts.items(), key=lambda p: (-p[1], p[0]))
    return [[message, count] for message, count in result[:n]]

def format_report(counts, errors):
    out = ['Отчёт по журналу', '']
    for level in sorted(counts):
        out.append(f'{level}: {counts[level]}')
    out.append('')
    out.append('Частые ошибки:')
    for message, count in errors:
        out.append(f'- {message} — {count}')
    return '\n'.join(out) + '\n'

