def next_id(arr):
    if 0 not in arr or not arr:
        return 0
        
    list_not_id = []
    for i in range(min(arr), len(arr)):
        if i not in arr:
            list_not_id.append(i)
            
    if not list_not_id:
        return max(arr) + 1
        
    return min(list_not_id)