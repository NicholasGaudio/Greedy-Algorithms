def InputHandling(filepath):
    with open(filepath, 'r') as input:
        lines = input.readlines()

    rows = []
    for line in lines:
        rows.append(line.strip().split())
    try:
        k = int(rows[0][0])
        m = int(rows[0][1])
    except (IndexError, ValueError):
        print("Error: Invalid input format.")
        return

    # Input error handling
    if (len(rows) != 2):
        print("Error: Number of requests does not match the number of rows in the input file.")
        return
    if (len(rows[1]) != m):
        print("Error: Number of requests does not match the number of requests specified in the input file.")
        return
    
    return k, m, rows