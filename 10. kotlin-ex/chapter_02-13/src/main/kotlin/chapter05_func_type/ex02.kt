package chapter05_func_type

// 익명함수
fun main(args: Array<String>) {
    println({    // 익명 함수   매개변수가 없으므로 -> 생략
        val currentYear = 2021
        "SimVillage 방문을 환경합니다. 촌장님! (copyright $currentYear)"
        // 마지막 표현식이 return값
    }())   // ()로 바로 호출
}