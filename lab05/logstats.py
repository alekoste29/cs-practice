def parse_event(line):
    line = line.split(' ')
    if len(line) >= 3 and line[1] in ('DEBUG','INFO','WARNING','ERROR'):
        time,level,*message = line
        message = ' '.join(message).strip()
        return { 'time': time,'level': level,'message': message}
    raise ValueError('негодная строка')

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

'''def format_report(counts, errors):
    out = ['Отчёт по журналу', '']
    for level in sorted(counts):
        out.append(f'{level}: {counts[level]}')
    out.append('')
    out.append('Частые ошибки:')
    for message, count in errors:
        out.append(f'- {message} — {count}')
    return '\n'.join(out) + '\n'''

