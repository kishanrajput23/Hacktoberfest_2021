const bubbleSort = (array: number[]): number[] => {
    const resultArr = [...array];
    let itemMoved = false;
    do {
        itemMoved = false;
        for (let i = 0; i < resultArr.length - 1; i++) {
            if (resultArr[i] > resultArr[i + 1]) {
                var lowerValue = resultArr[i + 1];
                resultArr[i + 1] = resultArr[i];
                resultArr[i] = lowerValue;
                itemMoved = true;
            }
        }
    } while (itemMoved);
    return resultArr;
};

const testInput: number[] = [9, 10, 1, 5, 3, 4];

const sortedArray = bubbleSort(testInput);
console.log(`Sorted list: ${sortedArray} `);
