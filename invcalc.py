#!/usr/bin/python3

import sys;

def help():
    print("usage: ./invcalc.py input.txt");
    return 1;

def mergeSort(array):
    length = len(array);
    inversions = 0;

    if length == 1:
        return array, inversions;
    elif length == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0];
            inversions += 1;
        return array, inversions;

    unsortedSubarrayA = array[0:(length // 2)];
    unsortedSubarrayB = array[(length // 2):length];

    subarrayA, inversionsA = mergeSort(unsortedSubarrayA);
    subarrayB, inversionsB = mergeSort(unsortedSubarrayB);

    inversions += inversionsA;
    inversions += inversionsB;

    i = 0;
    j = 0;
    sortedArray = [];

    for k in range(length):
        if i >= len(subarrayA) and j >= len(subarrayB):
            break;
        elif i >= len(subarrayA):
            sortedArray.append(subarrayB[j]);
            j += 1;
        elif j >= len(subarrayB):
            sortedArray.append(subarrayA[i]);
            i += 1;
        elif subarrayA[i] < subarrayB[j]:
            sortedArray.append(subarrayA[i]);
            i += 1;
        else:
            inversions += len(subarrayA[i:])
            sortedArray.append(subarrayB[j]);
            j += 1;

    return sortedArray, inversions;

def main():
    if len(sys.argv) == 2:
        numbers = [];

        with open(sys.argv[1]) as infile:
            for line in infile:
                numbers.append(int(line));

        sortedArray, inversions = mergeSort(numbers);
        print(inversions);

        return 0;
    else:
        return help();

if __name__ == "__main__":
    main();
