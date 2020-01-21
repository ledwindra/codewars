def sort_nested_list(l=None):

    if len(l) == 1:
        l[0][0].sort()
        l_final = l

    else:
        
        l2 = []
        for i in l:
            for j in i:
                for k in j:
                    l2.append(k)
                    l2.sort()

        l3 = []

        for i in 0, int(len(l2) / len(l)):
            l3.append(l2[i : i + int(len(l2) / len(l))])

        l4 = []
        for i in range(len(l3)):
            for j in range(0, len(l3[0]), int(len(l3[0]) / len(l[0]))):
                l4.append(l3[i][j : j + int(len(l3[0]) / len(l[0]))])

        l_final = []
        for i in 0, int(len(l4) / len(l4[0])):
            l_final.append(l4[i : i + int(len(l4) / len(l4[0]))])

    
    return l_final

if __name__ == "__main__":
    sort_nested_list()    