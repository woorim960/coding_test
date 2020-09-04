function solution(dartResult) {
    const score = { 'S':'**1', 'D':'**2', 'T':'**3', '#':'*-1' };
    const pattern = /\d+[SDT][*#]?/g;
    
    dartResult = dartResult.match(pattern).map((val, i) => {
        val = val.split('').map(v => {
            return Object.keys(score).includes(v) ? score[v] : v;
        }).join('');
        return val;
    });
    
    for(let i=0; i<dartResult.length; i++) {
        if(i >= 1) {
            dartResult[i-1] = dartResult[i][dartResult[i].length-1] === '*' ? dartResult[i-1]+'*2' : dartResult[i-1];
        }
        dartResult[i] = dartResult[i][dartResult[i].length-1] === '*' ? dartResult[i]+'2' : dartResult[i];
    }

    dartResult = dartResult.map(val => eval(val));
    return dartResult.reduce((acc, cur) => acc+cur);
    
}
