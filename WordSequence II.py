"""WordSequence II"""
def main(first, sec):
    """main function"""
    counter = -len(first)+1
    print(first)
    if len(first) >= len(sec):
        for i in range(max(len(sec), len(first))-1):
            print(sec[:i+1] + first[i+(-len(first)+1):])
    else:
        for i in range(len(sec)):
            if i + counter >= 0:
                break
            print(sec[:i+1] + first[i+(-len(first)+1):])
        for j in range(len(sec)-len(first), 0, -1):
            print(sec[:-j])
    print(sec)
main(input(), input())
