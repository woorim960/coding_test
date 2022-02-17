function solution(fees, records) {
  const cars = getCars(records);

  for (const car in cars) {
    cars[car].주차시간 = 0;
    cars[car].청구요금 = 0;
    for (let i = 0; i < cars[car].length; i++) {
      if (cars[car][i][1] === "OUT") continue;
      if (cars[car][i][1] === "IN" && cars[car][i + 1]) {
        cars[car].주차시간 += get주차시간(
          cars[car][i][0],
          cars[car][i + 1][0],
          fees[0]
        );
      } else {
        cars[car].주차시간 += get주차시간(cars[car][i][0], "23:59", fees[0]);
      }
    }
  }

  for (const car in cars) {
    if (cars[car].주차시간 <= fees[0]) {
      cars[car].청구요금 += fees[1];
      continue;
    } else cars[car].청구요금 += get청구요금(cars[car], fees);
  }

  return Object.entries(cars)
    .sort((a, b) => a[0] - b[0])
    .map((el) => el[1].청구요금);
}

function get청구요금(car, fees) {
  const [기본시간, 기본요금, 단위시간, 단위요금] = fees;
  const 남은시간 = car.주차시간 - 기본시간;

  return Math.ceil(남은시간 / 단위시간) * 단위요금 + 기본요금;
}

function get주차시간(start, end, 기본시간) {
  const [sH, sM] = start.split(":");
  const [eH, eM] = end.split(":");
  const time =
    new Date(2020, 6, 1, eH, eM, 0) - new Date(2020, 6, 1, sH, sM, 0);
  return time / 1000 / 60;
}

function getCars(records) {
  return records.reduce((acc, car) => {
    acc = typeof acc === "undefined" ? {} : acc;
    const [time, num, info] = car.split(" ");

    return {
      ...acc,
      [num]: num in acc ? [...acc[num], [time, info]] : [[time, info]],
    };
  }, {});
}
