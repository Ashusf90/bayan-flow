def linear_search(arr, target):
    steps = []

    for i in range(len(arr)):
        steps.append({
            "type": "compare",
            "index": i,
            "value": arr[i]
        })

        if arr[i] == target:
            steps.append({
                "type": "found",
                "index": i,
                "value": arr[i]
            })
            return steps
        else:
            steps.append({
                "type": "not-found",
                "index": i,
                "value": arr[i]
            })

    return steps
