def parse_event(line):
    line = line.split(' ')
    if len(line) >= 3:
        time,level,*massage = line
        massage = ' '.join(massage).strip()
        return { 'time': time,'level': level,'massage': massage}
    return{}

