# MergeSort(sequence S) {
#   if (size of S <= 1) return S;
#   split S into S_1 and S_2 of roughly the same size;
#   MergeSort(S_1);
#   MergeSort(S_2);
#   combine sorted S_1 and sorted S_2 to obtain sorted S;
#   return sorted S;
# }

def merge_sort(sequence):
    if (len(sequence) <= 1):
        print("when is one sequence is", sequence)
        return sequence
    mid = len(sequence) // 2
    s1 = sequence[:mid]
    s2 = sequence[mid:]
    sorted_1 = merge_sort(s1)
    sorted_2 = merge_sort(s2)
    print("at last", sorted_1 + sorted_2)
    return sorted_1 + sorted_2

sequence = [1,2,3,4,5]
merge_sort(sequence)