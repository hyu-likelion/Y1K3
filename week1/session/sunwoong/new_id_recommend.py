import re

def solution(new_id):
    # Step 0. id copy
    id = new_id

    # Step 1. replace upper case to lower case
    id = id.lower() 

    # Step 2. remove other characters
    # -), 밑줄(_), 마침표(.)
    # pattern = "[a-z0-9-_.~!@#$%^&*=+:?,\(\)\[\{\]\}\<\>\/]"
    pattern = "[a-z0-9_.\-]"
    remove = list(re.sub(pattern, "", id))
    for i in remove:
        id = id.replace(i, "")
    
    # Step3. 
    id = re.sub("[.]+", ".", id)

    # Step 4.
    id = re.sub("^[.]|[.]$", "", id)

    # Step 5.
    if len(id) == 0:
        id = "a"
    
    # Step 6.
    if len(id) >= 16:
        id = id[:15]
    if id[len(id)-1] == ".":
        id = id[:-1]
    
    # Step 7.
    if len(id) <= 2:
        id += id[len(id)-1] * (3-len(id))
    
    return id


input = "=.="
print("input : " + input)
print(solution(input))
