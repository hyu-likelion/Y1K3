def solution(new_id):
    answer = ''
    #1
    new_id=new_id.lower()
    #2
    tmp_id=""
    for i in range(len(new_id)):
        target=new_id[i]
        if target.isalpha()   or target.isnumeric() or target == '-' or target == '_' or target=='.':
            tmp_id=tmp_id+target
    new_id=tmp_id
    #3
    for i in range(len(tmp_id)):
        new_id=new_id.replace("..",".")
    #4
    tmp=len(new_id)
    if tmp!=0 and new_id[0]=='.':
        new_id=new_id[1:tmp]
    tmp=len(new_id)
    if tmp!=0 and new_id[tmp-1]=='.':
        new_id=new_id[0:tmp-1]
    #5
    if len(new_id)==0:
        new_id="a"
    
    #6
    if len(new_id)>=16:
        new_id=new_id[0:15]
        if new_id[14]=='.':
            new_id=new_id[0:14]
    #7
    tmp=len(new_id)
    if len(new_id)<=2:
        new_id=new_id+new_id[tmp-1]
    tmp=len(new_id)
    if len(new_id)<=2:
        new_id=new_id+new_id[tmp-1]
    tmp=len(new_id)
    if len(new_id)<=2:
        new_id=new_id+new_id[tmp-1]
    answer=new_id
    return answer