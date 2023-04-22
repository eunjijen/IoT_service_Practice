package chapter06_null

fun main(args: Array<String>) {
    var beverage = readLine()?.let {
        if(it.isNotBlank()) {
            it.capitalize()// capitalize(): String' is deprecated. Use replaceFirstChar instead
        } else {
            "맥주"
        }
    }
    println(beverage)
}

// let 함수: 함수를 매개변수로 받는다
// 매개변수가 1개라면 it을 사용  수신객ㅈ체 -> it
// lamda 함수의 return 값이 let함수의 return 값이다.


// !! - null이 아님을 단언
//fun main(args: Array<String>) {
//    var beverage = readLine()!!.capitalize()
//    println(beverage)
//}
