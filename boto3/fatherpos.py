def main():
    import sys
    input_lines = [line.strip() for line in sys.stdin if line.strip()]
    fatherPos = int(input_lines[0])
    martinPos = int(input_lines[1])
    velFather = int(input_lines[2])
    steps = int(input_lines[3])
    father_footprints = set()
    max_pos = fatherPos + steps * velFather
    for k in range(steps + 1):
        pos = fatherPos + k * velFather
        father_footprints.add(pos)
    best_F = 0
    best_V2 = 0
    D =fatherPos - martinPos
    V2_upper = max_pos - martinPos


    if V2_upper <= 0:

        print(0,0)
        return

    for V2 in range(1,V2_upper + 1):
        count = 0
        current = martinPos
        while current <= max_pos:
            if  current in father_footprints:
                 count += 1
            current += V2

        if count > best_F:
            best_F = count
            best_V2 = V2
        elif count == best_F:
            if V2 > best_V2:
                best_V2 = V2
    print(best_F,best_V2)
if __name__ == "__main__":
    main()

