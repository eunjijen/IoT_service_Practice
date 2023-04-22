package chapter06_null

// 변수가 null을 허용하는지 안하는지 지정
// 디폴트: 허용하지 않음(null 불가능)

//fun main(args: Array<String>) {
//    var signatureDrink = "맥주"
//    signatureDrink = null // 에러
//}


// 명시적 null 타입 - 변수 선언시 타입뒤에 ? 지정
//public fun readLine(): String ?

//fun main(args: Array<String>) {
//    var beverage = readLine()?.capitalize()
//    beverage = null   // 에러가 아님
//    println(beverage)
//}

// 안전 호출 연산자  ?.
fun main(args: Array<String>) {
    var beverage = readLine()?.capitalize()
    println(beverage)
}