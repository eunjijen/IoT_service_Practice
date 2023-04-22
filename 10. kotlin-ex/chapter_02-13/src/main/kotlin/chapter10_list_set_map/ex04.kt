package chapter10_list_set_map

private val patronList = mutableListOf<String>("Eli", "Mordoc", "Sophie")
// 인텍스가 필요한 경우    forEachIndexed
fun main(args: Array<String>) {
    patronList.forEachIndexed { index, patron ->
        println("좋은 밤입니다. $patron 님 - 당신은 ${index+1} 번째 입니다.")
    }
}

// 좋은 밤입니다. Eli 님 - 당신은 1 번째 입니다.
// 좋은 밤입니다. Mordoc 님 - 당신은 2 번째 입니다.
// 좋은 밤입니다. Sophie 님 - 당신은 3 번째 입니다.