function solution(n, arr1, arr2) {
    let result = [];
    // 지도(배열) 합치기
    for(let i=0; i<arr1.length; i++) {
        result.push(arr1[i] | arr2[i]);
    }
    
    // 2진수 변환
    let maxLen = Math.max(...result).toString(2).length;
    result = result.map(val => val.toString(2)).map(val => '0'.repeat(maxLen-val.length) + val);
    
    // 암호화
    result = result.map(str => str.split('').map(num => num == 1 ? '#' : ' ').join(''));
    return result;
}
