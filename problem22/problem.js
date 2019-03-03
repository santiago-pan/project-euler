export const getWordScore = word =>
  word
    .toLocaleLowerCase()
    .split("")
    .map(letter => letter.charCodeAt() - "a".charCodeAt() + 1)
    .reduce((acc, value) => acc + value, 0);

export const solution = list =>
  list
    .sort()
    .map(word => getWordScore(word))
    .map((wordScore, position) =>  wordScore * (position + 1))
    .reduce((acc, value) => acc + value, 0);

