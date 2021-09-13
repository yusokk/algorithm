// you can write to stderr for debugging purposes, e.g.
// process.stderr.write('this is a debug message');

function solution(A, K) {
    let table = ''
    const colSize = Math.max(...A).toString().length
    const rows = Math.ceil(A.length / K)
    const lastCols = A.length % K === 0 ? K : A.length % K

    if (A.length / K <= 1) {
        table += makeCols(lastCols, colSize)
        table += writeTable(0, lastCols, A, colSize)
        table += makeCols(lastCols, colSize)
    }
    else {
        table += makeCols(K, colSize)
        for (let i = 0; i < rows; i++) {
            if (i !== rows - 1) {
                table += writeTable((K * i), K, A, colSize)
                table += makeCols(K, colSize)
            }
            else {
                table += writeTable((K * i), lastCols, A, colSize)
                table += makeCols(lastCols, colSize)
            }
        }
    }

    process.stdout.write(table)
}


function makeCols(cols, colSize) {
    let line = '+'
    let width = '-'.repeat(colSize) + '+'

    line += width.repeat(cols) + '\n'
    return line
}

function writeTable(start, count, array, colSize) {
    let row = '|'

    for (let i = start; i < start + count; i++) {
        const num = array[i].toString()
        row += ' '.repeat(colSize - num.length)
        row += num + '|'
    }

    return row + '\n'
}


//


// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution() {
    // write your code in Javascript
    //
    // you can access DOM Tree using DOM Object Model:
    //    document.getElementsByTagName
    // or using jQuery:
    //    $('some_tag')
    //
    // please note that element.innerText is not supported,
    // you can use element.textContent instead.
    let answer = ''
    const trArr = document.getElementsByTagName('tr')

    for (let i = 0; i < trArr.length; i++) {
        const tdArr = trArr[i].childNodes

        for (let j = 1; j < tdArr.length; j += 2) {
            const tdTag = tdArr[j]
            const text = tdTag.textContent
            const color = tdTag.style.color
            const hexColor = getHexColor(color)
            const backgroundColor = tdTag.style.backgroundColor
            const hexBackgroundColor = getHexColor(backgroundColor)

            if (hexColor !== hexBackgroundColor) {
                answer += text
            }
        }
    }

    return answer
}

function getHexColor(string) {
    let upperStr = string.toUpperCase()
    let hexStr = upperStr

    if (upperStr.length < 6) {
        hexStr += '#'
        for (let i = 1; i < upperStr.length; i++) {
            hexStr += upperStr[i].repeat(2)
        }
    }

    return hexStr
}
