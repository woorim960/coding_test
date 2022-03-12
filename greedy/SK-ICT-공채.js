// 1번 문제
function solution(money, costs) {
    const MONEY_UNITS = [1, 5, 10, 50, 100, 500];
    const dUNITS = [500, 100, 50, 10, 5, 1];
    const samedUnits = costs.reduce((acc, cost, idx) => {
        return [ ...acc, cost * dUNITS[idx]];
    }, []);
    
    let minCost = samedUnits[0];
    const notUsed = samedUnits.reduce((acc, unit) => {
        if (minCost < unit) {
            return [ ...acc, false ];
        }
        minCost = unit;
        return [ ...acc, true ];
    }, []);
    
    let resultMoney = 0;
    let restMoney = money;
    for (let i = costs.length; i >= 0; i--) {
        if (notUsed[i]) {
            let goalCnt = Math.floor(restMoney / MONEY_UNITS[i]);
            restMoney %= MONEY_UNITS[i];
            resultMoney += goalCnt * costs[i];
        }
    }
    return resultMoney;
}
