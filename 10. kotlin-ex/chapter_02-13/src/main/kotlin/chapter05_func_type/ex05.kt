package chapter05_func_type

fun main(args: Array<String>) {
    val greetingFunction: (String) -> String = {// 매개변수 한개면 생략 가능
        val currentYear = 2023
        "SimVillage 방문을 환영합니다. $it!(copyright $currentYear)"
        // String --> it으로 들어가
    }
    println(greetingFunction("김선달"))
}