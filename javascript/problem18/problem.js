export const getNextSum = (currentSumLine, newLine) => {
  let maxSum = 0;
  let newSum = [];
  newLine.forEach((newItem, newLineIndex) => {
    currentSumLine.forEach((element, currentSumLineIndex) => {
      if (
        newLineIndex >= currentSumLineIndex &&
        newLineIndex - currentSumLineIndex <= 1
      ) {
        element.forEach(internal => {
          if (internal + newItem > maxSum) {
            maxSum = internal + newItem;
          }
          newSum[newLineIndex]
            ? newSum[newLineIndex].push(internal + newItem)
            : (newSum[newLineIndex] = [internal + newItem]);
        });
      }
    });
  });

  return newSum;
};

export const getSumLineOfTriangle = triangle => {
  let currentSumLine = [[0]];
  triangle.forEach(triangleLine => {
    currentSumLine = getNextSum(currentSumLine, triangleLine);
  });
  return currentSumLine;
};

export const getMaxSumOfLine = sumLine => {
  let maxSum = 0;
  sumLine.forEach(item => {
    item.forEach(sum => {
      if (sum > maxSum) {
        maxSum = sum;
      }
    });
  });
  return maxSum;
};