const clockwise = (keys, length) =>
  keys.map(key => [key[1], length - 1 - key[0]]);

const get_targets = (keys, length) =>
  Array(3)
    .fill(0)
    .reduce(arr => [...arr, clockwise(arr[arr.length - 1], length)], [keys]);

const adjust = (target, locks, length) => {
  const bench_mark = locks[0];

  for (let coord of target) {
    const x_gap = coord[0] - bench_mark[0];
    const y_gap = coord[1] - bench_mark[1];

    const check = Array(locks.length).fill(0);
    let is_false = false;
    for (let c of target) {
      let idx;
      const [x, y] = [c[0] - x_gap, c[1] - y_gap];

      if (
        (idx = locks.findIndex(lock => lock[0] === x && lock[1] === y)) !== -1
      )
        check[idx] = 1;
      else if (x >= 0 && x < length && y >= 0 && y < length) {
        is_false = true;
        break;
      }
    }
    if (is_false) continue;
    if (check.every(c => c === 1)) return true;
  }
  return false;
};

const compare = (keys, locks, keyLength, lockLength) => {
  const targets = get_targets(keys, keyLength);

  for (let target of targets) {
    if (adjust(target, locks, lockLength)) return true;
  }
  return false;
};

const find_target = (board, target) =>
  board.reduce(
    (arr, row, i) =>
      row.reduce(
        (coords, val, j) => (val === target ? [...coords, [i, j]] : coords),
        arr
      ),
    []
  );

function solution(key, lock) {
  const keys = find_target(key, 1);
  const locks = find_target(lock, 0);

  if (locks.length === 0) return true;
  if (keys.length === 0) return false;

  return compare(keys, locks, key.length, lock.length);
}
