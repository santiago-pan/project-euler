import { getWordScore, solution } from "./problem";
import { LIST } from "./data";

it("calculate the score of a word", () => {
  expect(getWordScore("COLIN")).toEqual(53);
});

it("should get the solution", () => {
  expect(solution(LIST)).toEqual(871198282)
})
