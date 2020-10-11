
ele = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

base = len(ele)

def encode_id(num_val, min_len = 1):
    "This Function Convert The ID to Appropriate Base 62 ID"
    itr_val = int(num_val)

    # Out Items
    out = []

    # Gathering Outs
    while(itr_val != 0):
        rem = itr_val % base
        out.append(rem)
        itr_val -= rem
        itr_val /= base
        itr_val = int(itr_val)

    # Return String
    rtn = ''

    # Atteching Items
    for i in out:
        rtn = ele[i] + rtn

    # Atteching Extra
    for i in range( min_len - len(rtn)):
        rtn = ele[0] + rtn

    return rtn

def decode_id(str_val):
    "This Function Convert The Appropriate Base 62 ID to ID"
    
    # Validation Tag
    valid = True

    # Gethare Elements And Validate
    if len(str_val) > 0:
        itr_lst = list(str_val)
        for i in itr_lst:
            if i not in ele:
                valid = False
    else: 
        valid = False
    
    if valid:
        # Geting Actual ID
        num_val = 0
        for i in range(1 , len(itr_lst)):
            num_val = (num_val + ele.index(itr_lst[i -1])) * base
        num_val += ele.index(itr_lst[-1])
        return num_val
    else:
        return 'Invalid Irgument'