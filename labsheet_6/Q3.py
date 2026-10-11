def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    tower_of_hanoi(n - 1, source, destination, helper)

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(n - 1, helper, source, destination)
n = 3
tower_of_hanoi(n, 'A', 'B', 'C')