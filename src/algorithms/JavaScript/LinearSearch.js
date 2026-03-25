export default function linearSearch(arr, target) {
  const steps = [];

  for (let i = 0; i < arr.length; i++) {
    // Step: checking element
    steps.push({
      type: "compare",
      index: i,
      value: arr[i],
    });

    if (arr[i] === target) {
      // Step: found (green)
      steps.push({
        type: "found",
        index: i,
        value: arr[i],
      });
      return steps;
    } else {
      // Step: not match (red)
      steps.push({
        type: "not-found",
        index: i,
        value: arr[i],
      });
    }
  }

  return steps;
}
