function solution(numbers) {
  const strNumbers = numbers.map(String);

  strNumbers.sort((a, b) => (b + a).localeCompare(a + b));

  const result = strNumbers.join('');

  return result[0] === '0' ? '0' : result;
}
