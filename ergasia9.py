# ergasia 9

def maxsequence(arithmoi):
    if not arithmoi: return None

    start_index, end_index = -1, 0
    current_start_index = -1
    max_so_far = 0
    current_sum = 0

    for index, arithmos in enumerate(arithmoi):
        current_sum += arithmos

        if current_sum >= max_so_far:
            max_so_far = current_sum
            start_index = current_start_index
            end_index = index

        elif current_sum <= 0:
            max_so_far = current_sum
            current_sum = 0
            current_start_index = index

    return (start_index + 1, end_index + 1)

# kwdikas me ton opoio tha dokimasoume
# to parapanw programma

if __name__ == "__main__":
    lista = []

    lista.append([1, -2, 3, 4, 5, -1])

    for number_list in lista:
        print "Ypolista me to megisto athrisma: =>", maxDistance(number_list)
