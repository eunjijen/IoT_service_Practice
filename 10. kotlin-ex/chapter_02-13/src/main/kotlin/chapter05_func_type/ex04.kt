package chapter05_func_type

fun main(args: Array<String>) {
    val greetingFunction: (String) -> String = {playerName ->
        val currentYear = 2023
        "SimVillage 방문을 환영합니다. $playerName!(copyright $currentYear)"
    }
    println(greetingFunction("김선달"))
    // SimVillage 방문을 환영합니다. 김선달!(copyright 2023)
}