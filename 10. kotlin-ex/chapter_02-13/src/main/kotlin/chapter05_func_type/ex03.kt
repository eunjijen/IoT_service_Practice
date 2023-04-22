package chapter05_func_type

// 함수를 변수에 대입 --> 함수를 나타내는 타입이 필요
fun main(args: Array<String>) {
    val greetingFunction: () -> String = {
        val currentYear = 2023
        "SimVillage 방문을 환영합니다. 촌장님!(copyright $currentYear)"
    }
    println(greetingFunction())
    // SimVillage 방문을 환영합니다. 촌장님!(copyright 2023)
}
