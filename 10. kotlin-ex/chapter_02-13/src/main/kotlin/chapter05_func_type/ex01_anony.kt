package chapter05_func_type

//fun check(letter: Char):Boolean {
//    return letter == 's'
//}
//
//val numLetters = "Mississippi".count(check)
//println(numLetters)

// 한번만 사용되는 함수 - 재사용성 X
// 아예 함수 정의를 count()안에 해줘 / 함수의 마지막 문장이 표현식이므로 return 값

fun main(args: Array<String>) {
    val numLetters = "Mississippi".count{letter -> letter == 's'}  // 왼쪽이 매개변수 오른쪽이 함수
    // 마지막 매개변수가 함수 타입일 때 () 생략
    println(numLetters)
}

// 함수를 다른 함수에서 호출할 일이 없어서 함수 이름이 필요 없음
//
//fun main(args: Array<String>) {
//    val numLetters = "Mississippi".count({ it == 's'})  // it으로 대체 가능
//    println(numLetters)
//}
