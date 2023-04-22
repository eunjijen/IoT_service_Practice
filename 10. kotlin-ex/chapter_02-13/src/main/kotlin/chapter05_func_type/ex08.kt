package chapter05_func_type

fun printConstructionCost(numBuildings: Int) {
    val cost = 500
    println("건축 비용: ${cost * numBuildings} 억")
}

// 이름있는 함수에 대한 참조
inline fun runSimulation(playerName: String,
                        costPrinter: (Int) -> Unit,   // 이름 있는 함수를 매개변수로 전달
                        greetingFunction: (String, Int) -> String) {
    val numBuildings = (1..3).shuffled().last()     // 1, 2, 3 중 무작위로 선택
    costPrinter(numBuildings)    // 호출
    println(greetingFunction(playerName, numBuildings))
}

fun main(args: Array<String>) {
    runSimulation("김선달", ::printConstructionCost) {   // 반드시 ::을 붙여야 함수 참조
            playerName, numBuildings ->
        val currentYear = 2023
        println("$numBuildings 채의 건물이 추가됨")
        "SimVillage 방문을 환영합니다. $playerName!(copyright $currentYear)"
    }
}

// 건축 비용: 500 억
// 1 채의 건물이 추가됨
// SimVillage 방문을 환영합니다. 김선달!(copyright 2023)