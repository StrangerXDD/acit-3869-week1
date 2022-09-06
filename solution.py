def our_shared_values(left, right):
    # this is the output list
    output = []

    # return empty if one of the list is empty
    if len(left) or len(right) == 0:
        return output
    else:
        # if both list is not empty
        for left_i in left:
            # iterate through each element in left list
            if left_i in output:
                # if that element is already checked, check the next element
                continue
            for right_i in right:
                # iterate through each element in right list
                if left_i == right_i:
                    # compare left element with right element
                    # if they are the same string, count the minimum occurence
                    left_i_occurence = min(left.count(left_i),right.count(right_i))
                    
                    # append that matches string to the output by the minimum occurence
                    for i in left_i_occurence:
                        output.append(left_i)
                    
                    # stop checking the rest of the right list, continue back to check next element in left list
                    break

