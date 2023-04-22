package chapter05_func_type

fun main(args: Array<String>) {
    val greetingFunction: (String, Int) -> String = { playerName, numBuildings ->
        val currentYear = 2023
        println("$numBuildings 채의 건물이 추가됨")
        "SimVillage 방문을 환영합니다. $playerName!(copyright $currentYear)"
    }
    println(greetingFunction("김선달", 2))
}

// 2 채의 건물이 추가됨
//SimVillage 방문을 환영합니다. 김선달!(copyright 2023)

// 1
//fun main(args: Array<String>) {      
//    val greetingFunction: () -> String = {   // String으로 추론 가능
//        val currentYear = 2021
//        "SimVillage 방문을 환영합니다. 촌장님!(copyright $currentYear)"
//    }
//}


// 2
//fun main(args: Array<String>) {          // 타입을 작성해줘야 추론 가능 (String, Int) -> String
//    val greetingFunction = { playerName: String, numBuildings: Int ->
//        val currentYear = 2021
//        println("$numBuildings 채의 건물이 추가됨")
//        "SimVillage 방문을 환영합니다. $playerName!(copyright $currentYear)"
//    }
//    println(greetingFunction("김선달", 2))
//}
