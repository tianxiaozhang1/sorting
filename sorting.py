import pygame, sys, random

def newarray_hover():
    if 690 <= pygame.mouse.get_pos()[0] <= 958 and 10 <= pygame.mouse.get_pos()[1] <= 100:
        pygame.draw.rect(screen, LAVENDER_HI, pygame.Rect(690, 10, 268, 90)) 
        screen.blit(newarray_surface1, newarray_rect1)
        screen.blit(newarray_surface2, newarray_rect2)
    else:
        pygame.draw.rect(screen, LAVENDER, pygame.Rect(690, 10, 268, 90)) 
        screen.blit(newarray_surface1, newarray_rect1)
        screen.blit(newarray_surface2, newarray_rect2)

def sizebutton_hover():
    if button_position-16 <= pygame.mouse.get_pos()[0] <= button_position+16 and 25-16 <= pygame.mouse.get_pos()[1] <= 25+16:
        pygame.draw.rect(screen, CLOUD_HI, pygame.Rect(button_position-16, 25, 32, 32))
        pygame.draw.rect(screen, (252, 220, 92), pygame.Rect(button_position-16+7, 25+7, 18, 18)) 
    else:
        pygame.draw.rect(screen, CLOUD, pygame.Rect(button_position-16, 25, 32, 32))
        pygame.draw.rect(screen, (252, 220, 92), pygame.Rect(button_position-16+7, 25+7, 18, 18))

def drawing_size_button(button_position):
    pygame.draw.rect(screen, DARKBLUE, pygame.Rect(380, 10, 300, 90))
    screen.blit(size_surface2, size_rect2)
    pygame.draw.rect(screen, (46, 46, 46), pygame.Rect(410, 33, 240, 16))
    pygame.draw.rect(screen, (36, 36, 36), pygame.Rect(410+4, 33+5, 232, 6))
    pygame.draw.rect(screen, CLOUD, pygame.Rect(button_position-16, 25, 32, 32))
    pygame.draw.rect(screen, (252, 220, 92), pygame.Rect(button_position-16+7, 25+7, 18, 18))

def bubble_hover():
    if 968 <= pygame.mouse.get_pos()[0] <= 1196 and 10 <= pygame.mouse.get_pos()[1] <= 100:
        pygame.draw.rect(screen, RED_HI, pygame.Rect(968, 10, 228, 90))
        screen.blit(bubble_surface1, bubble_rect1)
        screen.blit(bubble_surface2, bubble_rect2)
    else:
        pygame.draw.rect(screen, RED, pygame.Rect(968, 10, 228, 90))
        screen.blit(bubble_surface1, bubble_rect1)
        screen.blit(bubble_surface2, bubble_rect2)

def heap_hover():
    if 1206 <= pygame.mouse.get_pos()[0] <= 1434 and 10 <= pygame.mouse.get_pos()[1] <= 100:
        pygame.draw.rect(screen, YELLOW_HI, pygame.Rect(1206, 10, 228, 90))
        screen.blit(heap_surface1, heap_rect1)
        screen.blit(heap_surface2, heap_rect2)
    else:
        pygame.draw.rect(screen, YELLOW, pygame.Rect(1206, 10, 228, 90))
        screen.blit(heap_surface1, heap_rect1)
        screen.blit(heap_surface2, heap_rect2)

def merge_hover():
    if 1444 <= pygame.mouse.get_pos()[0] <= 1672 and 10 <= pygame.mouse.get_pos()[1] <= 100:
        pygame.draw.rect(screen, GREEN_HI, pygame.Rect(1444, 10, 228, 90))
        screen.blit(merge_surface1, merge_rect1)
        screen.blit(merge_surface2, merge_rect2)
    else:
        pygame.draw.rect(screen, GREEN, pygame.Rect(1444, 10, 228, 90))
        screen.blit(merge_surface1, merge_rect1)
        screen.blit(merge_surface2, merge_rect2)

def quick_hover():
    if 1682 <= pygame.mouse.get_pos()[0] <= 1910 and 10 <= pygame.mouse.get_pos()[1] <= 100:
        pygame.draw.rect(screen, BLUE_HI, pygame.Rect(1682, 10, 228, 90))
        screen.blit(quick_surface1, quick_rect1)
        screen.blit(quick_surface2, quick_rect2)
    else:
        pygame.draw.rect(screen, BLUE, pygame.Rect(1682, 10, 228, 90))
        screen.blit(quick_surface1, quick_rect1)
        screen.blit(quick_surface2, quick_rect2)

def new_array(array_size):

    #Initial setup
    array_size_raw = array_size
    array_list_raw = []
    array_list = []

    #Add random numbers
    while array_size_raw > 0:
        array_list_raw.append(random.randint(32, 400))
        array_size_raw -= 1

    #Avoid repetition - safety measure for mergesort and quicksort
    while len(set(array_list_raw)) < array_size:
        array_list_raw = list(set(array_list_raw))
        while len(array_list_raw) < array_size:
            array_list_raw.append(random.randint(32, 400))

    #Scaling columns up to the same max height every round
    max_j = max(array_list_raw)
    for j2 in range(array_size):
        array_list.append(int(array_list_raw[j2]*(400/max_j)))

    #Graphics
    pygame.draw.rect(screen, BOARD, pygame.Rect(10, 110, 1900, 960))

    bar_width = 1600//len(array_list)
    if bar_width > 32:
        bar_width = 32

    bar_spacing = 2

    s_pt = (1920 - (bar_width+bar_spacing)*len(array_list)) / 2 + 1

    for i in range(len(array_list)):
        i_h = int(array_list[i]*2.3)
        pygame.draw.rect(screen, DARKGREYBAR, pygame.Rect(s_pt+i*(bar_width+bar_spacing), 1052-i_h, bar_width, i_h))

    return array_list

def bubble_sort(cur_array):

    #Bubble sort is a simple process of repeatedly going through the array and compare
    #the two adjacent elements, and switching them if they're in the wrong order, i.e.
    #the left element is greater than the right element. It's not particularly efficient
    #on a large scale but is nevertheless fun to watch.

    #Initial setup
    length = len(cur_array)
    ori_array = []
    for o1 in cur_array:
        ori_array.append(o1)
    bubble_actions = []

    #Going through all numbers to compare all
    for i in range(length):
        for j in range(length - i - 1):
            #Left number bigger than right number
            if cur_array[j] > cur_array[j+1]:
                #Right before the switch
                bubble_actions.append(("c1", j, cur_array[j], j+1, cur_array[j+1]))
                cur_array[j], cur_array[j+1] = cur_array[j+1], cur_array[j]
                #Right after the switch
                bubble_actions.append(("c2", j, cur_array[j], j+1, cur_array[j+1]))
            #No need to change
            else:
                bubble_actions.append(("g0", j, cur_array[j], j+1, cur_array[j+1]))
                
    bar_width = 1600//len(ori_array)
    if bar_width > 32:
        bar_width = 32

    bar_spacing = 2
    s_pt = (1920 - (bar_width+bar_spacing)*len(ori_array)) / 2 + 1
    num_actions = len(bubble_actions)

    tl = -1
    while tl < num_actions:

        clock.tick(int(num_actions/16)) 

        #NB The four algorithms are different in efficiency but the clock rates are calibrated
        #so that they appear to reach a sorted array in roughly the same amound of time for
        #better human viewing pleasure. At the same time, the efficiency of the latter two 
        #algorithms should be easily noticeable.

        tl += 1
        
        if ori_array != cur_array:
            #No change
            if bubble_actions[tl][0] == "g0":
                pygame.draw.rect(screen, BOARD, pygame.Rect(10, 110, 1900, 960))
                for i3 in range(len(ori_array)):
                    if i3 != bubble_actions[tl][1] and i3 != bubble_actions[tl][3]:
                        pygame.draw.rect(screen, DARKGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3)))
                    else:
                        pygame.draw.rect(screen, DARKERGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3)))
                pygame.display.update()
            #Pre-switch
            elif bubble_actions[tl][0] == "c1":
                pygame.draw.rect(screen, BOARD, pygame.Rect(10, 110, 1900, 960))
                for i3 in range(len(ori_array)):
                    if i3 != bubble_actions[tl][1] and i3 != bubble_actions[tl][3]:
                        pygame.draw.rect(screen, DARKGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3)))
                    else:
                        pygame.draw.rect(screen, (222, 108, 122), pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3))) 
                pygame.display.update()

                #Updating sequence
                ori_array[bubble_actions[tl][1]] = bubble_actions[tl][4]
                ori_array[bubble_actions[tl][3]] = bubble_actions[tl][2]
            #Post-switch
            else: 
                pygame.draw.rect(screen, BOARD, pygame.Rect(10, 110, 1900, 960))
                for i3 in range(len(ori_array)):
                    if i3 != bubble_actions[tl][1] and i3 != bubble_actions[tl][3]:
                        pygame.draw.rect(screen, DARKGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3)))
                    else:
                        pygame.draw.rect(screen, (182, 56, 82), pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3)))
                pygame.display.update()    
                pass
        else:
            pygame.draw.rect(screen, BOARD, pygame.Rect(10, 110, 1900, 960))
            for i3 in range(len(ori_array)):
                pygame.draw.rect(screen, DARKGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3)))    
            break
    tlc = -1
    clen = len(cur_array) - 1
    while tlc < clen:
        clock.tick(16)
        tlc += 1
        pygame.draw.rect(screen, (int((166-210)*((clen-tlc)/clen)+210), int((126-72)*((clen-tlc)/clen)+72), int((182-52)*((clen-tlc)/clen)+52)), pygame.Rect(s_pt+tlc*(bar_width+bar_spacing), 1052-int(cur_array[tlc]*2.3), bar_width, int(cur_array[tlc]*2.3))) 
        pygame.display.update()   

def heap_sort(cur_array):

    #Heapsort is essentially two steps. One is to build a heap in the form of a binary tree.
    #Two is to constantly remove the largest number element and adding it to the array.
    #The heap is updated from each removal.

    #Initial setup
    ori_array = []
    for o1 in cur_array:
        ori_array.append(o1)
    heap_actions = []

    def sift_down(start, end):
        #First item as root
        root = start

        while True:
            child = 2 * root + 1
            #Past end
            if child > end:
                 break
            #If child is smaller than the root, move to the next
            if child + 1 <= end and cur_array[child] < cur_array[child+1]:
                child += 1
            #Switch since the child number is greater than the root number
            if cur_array[root] < cur_array[child]:
                #The two numbers right before switch
                heap_actions.append(("1a", root, cur_array[root], child, cur_array[child]))
                cur_array[root], cur_array[child] = cur_array[child], cur_array[root]
                #The two numbers right after switch
                heap_actions.append(("1b", root, cur_array[root], child, cur_array[child]))
                root = child
            #Completed
            else:
                break

    for start in range((len(cur_array)-2)//2, -1, -1):
        sift_down(start, len(cur_array)-1)
    
    for end in range(len(cur_array)-1,0,-1):
        #The two numbers right before switch
        heap_actions.append(("2a", 0, cur_array[0], end, cur_array[end]))
        cur_array[0],cur_array[end] = cur_array[end], cur_array[0]
        #The two numbers right after switch
        heap_actions.append(("2b", 0, cur_array[0], end, cur_array[end]))
        sift_down(0, end-1)

    bar_width = 1600//len(cur_array)
    if bar_width > 32:
        bar_width = 32

    bar_spacing = 2
    s_pt = (1920 - (bar_width+bar_spacing)*len(cur_array)) / 2 + 1# + 20
    num_actions = len(heap_actions)# - 1

    tl = -1
    while tl < num_actions:
        clock.tick(int(num_actions/16)) 

        tl += 1
        
        if ori_array != cur_array:
            #Before switch
            if heap_actions[tl][0] == "1a":
                
                pygame.draw.rect(screen, BOARD, pygame.Rect(10, 110, 1900, 960))
                for i3 in range(len(ori_array)):
                    if i3 != heap_actions[tl][1] and i3 != heap_actions[tl][3]:
                        pygame.draw.rect(screen, DARKGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3)))
                    else:                                                                                                                                                                                             
                        pygame.draw.rect(screen, (212, 180, 102), pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3)))
                pygame.display.update()

                #Updating array
                ori_array[heap_actions[tl][1]] = heap_actions[tl][4]
                ori_array[heap_actions[tl][3]] = heap_actions[tl][2]

            #After switch
            elif heap_actions[tl][0] == "1b":
                pygame.draw.rect(screen, BOARD, pygame.Rect(10, 110, 1900, 960))
                for i3 in range(len(ori_array)):
                    if i3 != heap_actions[tl][1] and i3 != heap_actions[tl][3]:
                        pygame.draw.rect(screen, DARKGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3)))
                    else:
                        pygame.draw.rect(screen, (192, 156, 82), pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3)))
                pygame.display.update()
                
            #Before switch
            elif heap_actions[tl][0] == "2a":

                pygame.draw.rect(screen, BOARD, pygame.Rect(10, 110, 1900, 960))
                for i3 in range(len(ori_array)):
                    if i3 != heap_actions[tl][1] and i3 != heap_actions[tl][3]:
                        pygame.draw.rect(screen, DARKGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3)))
                    else:                                                                                                                                                                                     
                        pygame.draw.rect(screen, LIGHTERGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3))) 
                pygame.display.update()
                ori_array[heap_actions[tl][1]] = heap_actions[tl][4]
                ori_array[heap_actions[tl][3]] = heap_actions[tl][2]

            #After switch
            else: 
                pygame.draw.rect(screen, BOARD, pygame.Rect(10, 110, 1900, 960))
                for i3 in range(len(ori_array)):
                    if i3 != heap_actions[tl][1] and i3 != heap_actions[tl][3]:
                        pygame.draw.rect(screen, DARKGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3)))
                    else:
                        pygame.draw.rect(screen, DARKERGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3))) 
                pygame.display.update()    
                pass
        else:
            pygame.draw.rect(screen, BOARD, pygame.Rect(10, 110, 1900, 960))
            for i3 in range(len(ori_array)):
                pygame.draw.rect(screen, DARKGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(ori_array[i3]*2.3), bar_width, int(ori_array[i3]*2.3)))    
            pygame.display.update()    
            break

    tlc = -1
    clen = len(cur_array) - 1
    while tlc < clen:
        clock.tick(16)
        tlc += 1
        pygame.draw.rect(screen, (int((242-202)*((clen-tlc)/clen)+202), int((142-182)*((clen-tlc)/clen)+182), int((96-28)*((clen-tlc)/clen)+28)), pygame.Rect(s_pt+tlc*(bar_width+bar_spacing), 1052-int(cur_array[tlc]*2.3), bar_width, int(cur_array[tlc]*2.3))) 
        pygame.display.update()  

    return cur_array

def merge_sort(cur_array, length, pro_array, res_array, workingon_array):

    #Mergesort is a divide and conquer algorithm, invented by (THE) John von Neumann in 1945.
    #It divides the sequence in half until the two halves are both one element in length.
    #Sublists are then merged back together to produce a longer list until there's only
    #one sublist left (with the same length as the original array), which is sorted.

    #Done if sequence down to one number
    if len(cur_array) < 2:
        return cur_array
    
    #Divide the current array down the middle
    mid = len(cur_array) // 2
    left = merge_sort(cur_array[:mid], length, pro_array, res_array, workingon_array)
    right = merge_sort(cur_array[mid:], length, pro_array, res_array, workingon_array)

    #For display purpose, showing the section currently studying
    working_on = left+right

    #Finding the bookends of the current array, for display purpose
    left_end = pro_array[-1].index(left[0])
    right_beginning = pro_array[-1].index(right[-1])+1
    left_ori = pro_array[-1][:left_end]
    right_ori = pro_array[-1][right_beginning:]

    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):

        #Left number greater
        if left[i] < right[j]:
            result.append(left[i])
            
            #Remove from working list
            working_on.remove(result[:len(result)][-1])

            #Update display sequence
            pro_entry = left_ori + result[:len(result)] + working_on + right_ori
            pro_array.append(pro_entry)
            res_array.append(result[:len(result)])
           
            #Update the pair being compared
            workingon_array.append([])
            workingon_array[-1] = [left[i], right[j]]

            i += 1

        #Right number greater
        else:
            result.append(right[j])
            
            #Remove from working list
            working_on.remove(result[:len(result)][-1])

            #Update display sequence
            pro_entry = left_ori + result[:len(result)] + working_on + right_ori
            pro_array.append(pro_entry)
            res_array.append(result[:len(result)])

            #Update the pair being compared
            workingon_array.append([])
            workingon_array[-1] = [left[i], right[j]]

            j += 1
 
    while i < len(left):

        result.append(left[i])
        working_on.remove(result[:len(result)][-1])

        #Update display sequence
        pro_entry = left_ori + result[:len(result)] + working_on + right_ori
        pro_array.append(pro_entry)
        res_array.append(result[:len(result)])

        #Update the added number
        workingon_array.append([])
        workingon_array[-1] = [left[i]]

        i += 1
        
    while j < len(right):

        result.append(right[j])

        working_on.remove(result[:len(result)][-1])

        #Update display sequence
        pro_entry = left_ori + result[:len(result)] + working_on + right_ori
        pro_array.append(pro_entry)
        res_array.append(result[:len(result)])

        #Update the added number
        workingon_array.append([])
        workingon_array[-1] = [right[j]]

        j += 1

    #Result covers the entire sequence => done
    if len(result) == length:
        
        #Graphics
        bar_width = 1600//length
        if bar_width > 32:
            bar_width = 32

        bar_spacing = 2
        s_pt = (1920 - (bar_width+bar_spacing)*length) / 2 + 1
        num_actions = len(pro_array) - 1

        cur_array = result

        tl = -1
        while tl < num_actions:

            clock.tick(int(num_actions/16))
            tl += 1

            pygame.draw.rect(screen, BOARD, pygame.Rect(10, 110, 1900, 960))
            for i3 in range(len(pro_array[tl])):
                #Entire array
                if pro_array[tl][i3] not in res_array[tl] and pro_array[tl][i3] not in workingon_array[tl]:
                    pygame.draw.rect(screen, DARKGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(pro_array[tl][i3]*2.3), bar_width, int(pro_array[tl][i3]*2.3)))  
                #The section being examined
                if pro_array[tl][i3] in res_array[tl]:
                    pygame.draw.rect(screen, (168, 182, 140), pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(pro_array[tl][i3]*2.3), bar_width, int(pro_array[tl][i3]*2.3))) 
                #The particular element in question
                if pro_array[tl][i3] in workingon_array[tl]:
                    pygame.draw.rect(screen, (112, 132, 96), pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(pro_array[tl][i3]*2.3), bar_width, int(pro_array[tl][i3]*2.3)))

            pygame.display.update() 

        pygame.draw.rect(screen, BOARD, pygame.Rect(10, 110, 1900, 960))
        for i3 in range(len(result)):
            pygame.draw.rect(screen, DARKGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(result[i3]*2.3), bar_width, int(result[i3]*2.3))) 
        pygame.display.update()    

        tlc = -1
        clen = length - 1
        while tlc < clen:
            clock.tick(16)
            tlc += 1
            pygame.draw.rect(screen, (int((182-42)*((clen-tlc)/clen)+42), int((212-110)*((clen-tlc)/clen)+110), int((50-62)*((clen-tlc)/clen)+62)), pygame.Rect(s_pt+tlc*(bar_width+bar_spacing), 1052-int(cur_array[tlc]*2.3), bar_width, int(cur_array[tlc]*2.3))) 
            pygame.display.update()  

    return result

def quick_sort(cur_array, o_length, pro_array, pivot_list, cur_pro_array, cur_pair_array):

    #Quicksort is another divide-and-conquer algorithm, invented by Tony Hoare in 1959.
    #An arbitrary element is selected (initial element in this case) and all remaining elements
    #in the current array are compared to it, and the once smaller will be moved to its left and
    #the ones greater will remain on the left. The initial element is now a pivot and its position
    #in the final sequence is now known since everything smaller than it is to its left, and all
    #greater elements on the right. The array is then divided into two with the pivot removed in
    #the middle. The process continues until the entire original array is finished.

    #Personal note:
    #The two divide-and-conquer algorithms (merge sort and quicksort) are particularly interesting
    #(and difficult) to visualize because divide-and-conquer intentionally works on a small section
    #at a time (hence the efficiency) and visualization requires the full picture to be maintained 
    #at all times. The scale here isn't significant enough but it would be fun to see how much the
    #visualization slows down the calculation process and how much edge the otherwise-efficient
    #algorithms would still have over the first two less efficient algorithms (especially bubble sort)
    #when the array is much larger.

    #Length of array
    length = len(cur_array)

    #Getting the two bookends of the current array
    if length > 0:
        pre_left = pro_array[-1][:pro_array[-1].index(cur_array[0])]
        pre_right = pro_array[-1][pro_array[-1].index(cur_array[-1])+1:]
    else:
        pre_left = []
        pre_right = pro_array[-1]

    pre_trio = pre_left + cur_array + pre_right

    #Make sure the all pivot numbers are at the right position
    if len(pivot_list) > 0:
        for pl in pivot_list:
            if pl[0] in pre_trio:
                pre_trio.remove(pl[0])
            pre_trio.insert(pl[1], pl[0])
    
    #Getting the updated sequence
    if length > 0:
        updated_left = pre_trio[:pre_trio.index(cur_array[0])]
        updated_right = pre_trio[pre_trio.index(cur_array[-1])+1:]
    else:
        updated_left = []#leftright_array[-1][0]
        updated_right = []#leftright_array[-1][1]

    #Done if the sequence is down to one number
    if length < 2:
        return cur_array

    cur_pos = 0

    #Going through the current array
    for i in range(1, length):
        if cur_array[i] <= cur_array[0]:
            
            cur_pos += 1

            #Adding current array to the display sequence
            processed_trio = updated_left + cur_array + updated_right
            pro_array.append(processed_trio)
            cur_pro_array.append(cur_array)
            cur_pair_array.append([cur_array[i], cur_array[0]])

            #If the compared number is less than pivot (condition above), switch the smaller number to the front
            temp = cur_array[i]
            cur_array[i] = cur_array[cur_pos]
            cur_array[cur_pos] = temp

            #This is the updated current array showing the switch
            processed_trio = updated_left + cur_array + updated_right
            pro_array.append(processed_trio)
            cur_pro_array.append(cur_array)
            cur_pair_array.append([cur_array[i], cur_array[0]])

    #Getting the pivot and registering it
    pivot = cur_array[0] #
    pivot_list.append([pivot, cur_pos+len(updated_left)]) #

    #Switching the pivot to its position
    temp = cur_array[0]
    cur_array[0] = cur_array[cur_pos]
    cur_array[cur_pos] = temp
    
    #Updating display sequence with the new pivot position
    processed_trio = updated_left + cur_array + updated_right
    pro_array.append(processed_trio)
    cur_pro_array.append(cur_array)
    cur_pair_array.append([cur_array[i], cur_array[0]])

    #Divide and conquer with two smaller sequences, divided by the pivot
    left = quick_sort(cur_array[0:cur_pos], o_length, pro_array, pivot_list, cur_pro_array, cur_pair_array)
    right = quick_sort(cur_array[cur_pos+1:length], o_length, pro_array, pivot_list, cur_pro_array, cur_pair_array)

    cur_array = left + [cur_array[cur_pos]] + right

    return cur_array

def quick_visual(o_length, pro_array, cur_pro_array, cur_pair_array):
    #displaying the quicksort process

    #All graphics
    bar_width = 1600//o_length
    if bar_width > 32:
        bar_width = 32

    bar_spacing = 2
    s_pt = (1920 - (bar_width+bar_spacing)*o_length) / 2 + 1# + 20
    num_actions = len(pro_array) - 1

    tl = 0
    while tl < num_actions:
        clock.tick(int(num_actions/16))
        tl += 1

        pygame.draw.rect(screen, BOARD, pygame.Rect(10, 110, 1900, 960))
        for i3 in range(len(pro_array[tl])):
            if pro_array[tl][i3] not in cur_pro_array[tl] and pro_array[tl][i3] not in cur_pair_array[tl]:
                pygame.draw.rect(screen, DARKGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(pro_array[tl][i3]*2.3), bar_width, int(pro_array[tl][i3]*2.3)))
            #Current array
            if pro_array[tl][i3] in cur_pro_array[tl]:
                pygame.draw.rect(screen, (110, 156, 198), pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(pro_array[tl][i3]*2.3), bar_width, int(pro_array[tl][i3]*2.3))) 
            #The two numbers getting compared
            if pro_array[tl][i3] in cur_pair_array[tl]:
                pygame.draw.rect(screen, (106, 128, 138), pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(pro_array[tl][i3]*2.3), bar_width, int(pro_array[tl][i3]*2.3))) 
        pygame.display.update() 

    #All grey when done
    pygame.draw.rect(screen, BOARD, pygame.Rect(10, 110, 1900, 960))
    for i3 in range(len(pro_array[-1])):
        pygame.draw.rect(screen, DARKGREYBAR, pygame.Rect(s_pt+i3*(bar_width+bar_spacing), 1052-int(pro_array[-1][i3]*2.3), bar_width, int(pro_array[-1][i3]*2.3)))
    pygame.display.update()    
    
    tlc = -1
    clen = o_length - 1
    while tlc < clen:
        clock.tick(16)
        tlc += 1
        pygame.draw.rect(screen, (int((136-0)*((clen-tlc)/clen)), int((172-108)*((clen-tlc)/clen)+108), int((218-136)*((clen-tlc)/clen)+136)), pygame.Rect(s_pt+tlc*(bar_width+bar_spacing), 1052-int(pro_array[-1][tlc]*2.3), bar_width, int(pro_array[-1][tlc]*2.3))) 
        pygame.display.update()  

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption('Sort of Sorting')

#Colours
DARKBACKGROUND = (202, 202, 196)
BOARD = (232, 232, 222)

LIGHTERGREYBAR = ((162, 162, 158))
DARKGREYBAR = (122, 122, 118)
DARKERGREYBAR = (82, 82, 88)

PANELCOLOUR = (242, 242, 222)

DARKGREY = (118, 118, 118)
DARKBLUE = (0, 62, 116)

RUYAOQING = (128, 164, 146)
CLOUD = (90, 162, 172)
CLOUD_HI = (146, 196, 206)
LAVENDER = (76, 76, 156)
LAVENDER_HI = (92, 92, 162)
RED = (210, 72, 52)
RED_HI = (206, 96, 66)
YELLOW = (202, 182, 28)
YELLOW_HI = (206, 192, 62)
GREEN = (42, 110, 62)
GREEN_HI = (72, 112, 62)
BLUE = (0, 108, 136)
BLUE_HI = (42, 112, 132)

button_position = 530
array_size = int((button_position - 410)/4)
if array_size < 4:
    array_size = 4

array_list = []

dragging = False
update_array = False
draw_button = False

#Control panel
button_font = pygame.font.Font('freesansbold.ttf', 30)

pygame.draw.rect(screen, DARKBACKGROUND, pygame.Rect(0, 0, 1920, 1080))
pygame.draw.rect(screen, BOARD, pygame.Rect(10, 110, 1900, 960))

current_array = new_array(array_size)

title_surface1 = button_font.render("SORT OF", True, PANELCOLOUR) 
title_rect1 = title_surface1.get_rect(midleft = (14, 60)) 
title_surface2 = button_font.render("SORTING", True, PANELCOLOUR) 
title_rect2 = title_surface2.get_rect(midleft = (14, 86)) 
pygame.draw.rect(screen, RUYAOQING, pygame.Rect(10, 10, 360, 90))
screen.blit(title_surface1, title_rect1)
screen.blit(title_surface2, title_rect2)

size_surface2 = button_font.render("ARRAY SIZE", True, PANELCOLOUR) 
size_rect2 = size_surface2.get_rect(midleft = (384, 86)) 

drawing_size_button(button_position)

newarray_surface1 = button_font.render("GENERATE", True, PANELCOLOUR)
newarray_rect1 = newarray_surface1.get_rect(midleft = (694, 60)) 
newarray_surface2 = button_font.render("NEW ARRAY", True, PANELCOLOUR) 
newarray_rect2 = newarray_surface2.get_rect(midleft = (694, 86)) 
pygame.draw.rect(screen, LAVENDER, pygame.Rect(690, 10, 268, 90))
screen.blit(newarray_surface1, newarray_rect1)
screen.blit(newarray_surface2, newarray_rect2)

bubble_surface1 = button_font.render("BUBBLE", True, PANELCOLOUR) 
bubble_rect1 = bubble_surface1.get_rect(midleft = (972, 60)) 
bubble_surface2 = button_font.render("SORT", True, PANELCOLOUR) 
bubble_rect2 = bubble_surface2.get_rect(midleft = (972, 86)) 
pygame.draw.rect(screen, RED, pygame.Rect(968, 10, 228, 90))
screen.blit(bubble_surface1, bubble_rect1)
screen.blit(bubble_surface2, bubble_rect2)

heap_surface1 = button_font.render("HEAP", True, PANELCOLOUR)
heap_rect1 = heap_surface1.get_rect(midleft = (1210, 60)) 
heap_surface2 = button_font.render("SORT", True, PANELCOLOUR) 
heap_rect2 = heap_surface2.get_rect(midleft = (1210, 86)) 
pygame.draw.rect(screen, YELLOW, pygame.Rect(1206, 10, 228, 90))
screen.blit(heap_surface1, heap_rect1)
screen.blit(heap_surface2, heap_rect2)

merge_surface1 = button_font.render("MERGE", True, PANELCOLOUR) 
merge_rect1 = merge_surface1.get_rect(midleft = (1448, 60)) 
merge_surface2 = button_font.render("SORT", True, PANELCOLOUR) 
merge_rect2 = merge_surface2.get_rect(midleft = (1448, 86)) 
pygame.draw.rect(screen, GREEN, pygame.Rect(1444, 10, 228, 90))
screen.blit(merge_surface1, merge_rect1)
screen.blit(merge_surface2, merge_rect2)

quick_surface1 = button_font.render("QUICK", True, PANELCOLOUR) 
quick_rect1 = quick_surface1.get_rect(midleft = (1686, 60)) 
quick_surface2 = button_font.render("SORT", True, PANELCOLOUR) 
quick_rect2 = quick_surface2.get_rect(midleft = (1686, 86)) 
pygame.draw.rect(screen, BLUE, pygame.Rect(1682, 10, 228, 90))
screen.blit(quick_surface1, quick_rect1)
screen.blit(quick_surface2, quick_rect2)

while True:

    if dragging == True:

        pre_array_size = array_size

        #Generating new array
        if 400 <= pygame.mouse.get_pos()[0] <= 660 and 25 <= pygame.mouse.get_pos()[1] <= 57:
            
            if 410 <= pygame.mouse.get_pos()[0] <= 650:
                button_position = pygame.mouse.get_pos()[0]
            elif 400 <= pygame.mouse.get_pos()[0] <= 410:
                button_position = 410 
            elif 650<= pygame.mouse.get_pos()[0] <= 660:
                button_position = 650

            #Array size depends on the position of the knob, but can't be less than 4
            array_size = int((button_position - 410)/4)
            if array_size < 4:
                array_size = 4
            if array_size != pre_array_size:
                current_array = new_array(array_size)
                
            drawing_size_button(button_position)
            
        #Slightly outside area
        elif 380 <= pygame.mouse.get_pos()[0] <= 680 and 10 <= pygame.mouse.get_pos()[1] <= 90:
            if 80 <= pygame.mouse.get_pos()[0] <= 410:
                button_position = 410
            elif 650 <= pygame.mouse.get_pos()[0] <= 980:
                button_position = 650

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #Buttons
            if 10 <= pygame.mouse.get_pos()[1] <= 100:

                #Generate new array
                if 690 <= pygame.mouse.get_pos()[0] <= 958:
                    array_size = int((button_position - 410)/4)
                    if array_size < 4:
                        array_size = 4
                    current_array = new_array(array_size)
                
                #Bubble sort
                if 968 <= pygame.mouse.get_pos()[0] <= 1196:
                    bubble_sort(current_array)
                    
                #Heap sort
                if 1206 <= pygame.mouse.get_pos()[0] <= 1434:
                    heap_sort(current_array)

                #Merge Sort
                if 1444 <= pygame.mouse.get_pos()[0] <= 1672:

                    length = len(current_array)
                    pro_array = []
                    pro_array.append(current_array)
                    res_array = [[]]
                    workingon_array = [[]]

                    current_array = merge_sort(current_array, length, pro_array, res_array, workingon_array)

                #Quicksort
                if 1682 <= pygame.mouse.get_pos()[0] <= 1910:
                    
                    pro_array = []
                    pro_array.append(current_array)
                    o_length = len(current_array)
                    pivot_list = []
                    cur_pro_array = [[]]
                    cur_pair_array = [[]]

                    current_array = quick_sort(current_array, o_length, pro_array, pivot_list, cur_pro_array, cur_pair_array)
                    
                    quick_visual(o_length, pro_array, cur_pro_array, cur_pair_array)

            #Full bar range
            if 398 <= pygame.mouse.get_pos()[0] <= 662:
                if 398 <= pygame.mouse.get_pos()[0] <= 410:
                    button_position = 410 
                elif 650<= pygame.mouse.get_pos()[0] <= 662:
                    button_position = 650

                #At right height
                if 25 <= pygame.mouse.get_pos()[1] <= 57:
                    #Clicking button
                    if button_position-16 <= pygame.mouse.get_pos()[0] <= button_position+16:
                        dragging = True 
                    #Clicking the bar itself
                    else:
                        button_position = pygame.mouse.get_pos()[0]
                        
                        array_size = int((button_position - 410)/4)
                        if array_size < 4:
                            array_size = 4
                        current_array = new_array(array_size)

                        drawing_size_button(button_position)
                        
        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    #When mouse is hovering over these buttons
    newarray_hover()
    merge_hover()
    quick_hover()
    heap_hover()
    bubble_hover()

    pygame.display.update()

    clock.tick(30)
