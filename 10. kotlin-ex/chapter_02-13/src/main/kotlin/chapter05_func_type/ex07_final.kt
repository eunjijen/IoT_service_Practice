package chapter05_func_type

// 함수를 인자로 받는 함수 정의
// 익명함수 -> 람다 / 익명함수 정의 -> 람다표현식/람다식

//fun main(args: Array<String>) {
//    val greetingFunction = { playerName: String, numBuildings: Int ->
//        val currentYear = 2023
//        println("$numBuildings 채의 건물이 추가됨")    // print 하겠다
//        "SimVillage 방문을 환영합니다. $playerName!(copyright $currentYear)"  // 문자열을 리턴하겠다
//    }
//    runSimulation("김선달", greetingFunction)  // 함수를 인자로 받는 함수
//}

// 최종적으로 이렇게 표현
fun main(args: Array<String>) {
    runSimulation("김선달") { playerName, numBuildings ->
        val currentYear = 2021
        println("$numBuildings 채의 건물이 추가됨")
        "SimVillage 방문을 환영합니다. $playerName!(copyright $currentYear)"
    }
}

// 랜덤 표현
fun runSimulation(playerName: String,
                  greetingFunction: (String, Int) -> String) {
    val numBuildings = (1..3).shuffled().last()   // 1, 2, 3 중 무작위로 선택
    // shuffled() - 섞을 때 사용 랜덤한 숫자
    println(greetingFunction(playerName, numBuildings))
}

// 2 채의 건물이 추가됨
// SimVillage 방문을 환영합니다. 김선달!(copyright 2023)

// 3 채의 건물이 추가됨
// SimVillage 방문을 환영합니다. 김선달!(copyright 2023)
