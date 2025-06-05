import os

def compare():
    file1 = input("Enter the first filename: ").strip()
    file2 = input("Enter the second filename: ").strip()

    firstlist = []
    try:
        with open(file1) as x:
            for line in x:
                firstlist.append(line.strip())
    except FileNotFoundError:
        print(f"\nError: Filename '{file1}' does not exist in current directory (don't forget to specify file/script type - .py, .txt, .csv...etc)")
        return

    secondlist = []
    try:
        with open(file2) as y:
            for line in y:
                secondlist.append(line.strip())
    except FileNotFoundError:
        print(f"\nError: Filename '{file2}' does not exist in current directory (don't forget to specify file/script type - .py, .txt, .csv...etc)")
        return

    overlaplist = [elem for elem in firstlist if elem in secondlist]

    if not overlaplist:
        print("No IP's added")
    else:
        output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'overlap.csv')
        print(f"\nThe following IPs have been added to 'overlap.csv' in {os.path.dirname(os.path.abspath(__file__))}:\n{', '.join(overlaplist)}")
        with open(output_path, 'w') as f:
            f.write("\n".join(overlaplist))
