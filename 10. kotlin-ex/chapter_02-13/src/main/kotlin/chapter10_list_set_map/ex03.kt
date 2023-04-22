package chapter10_list_set_map

private val patronList = mutableListOf<String>("Eli", "Mordoc", "Sophie")
// 3가지 방법
fun main(args: Array<String>) {
    for(patron in patronList) {
        println("좋은 밤입니다. $patron 님")
    }

    println("================================")
    patronList.forEach {patron ->
        println("좋은 밤입니다. $patron 님")
    }

    println("==================================")
    patronList.forEach { println("좋은 밤입니다. $it 님") }

}

// 좋은 밤입니다. Eli 님
//좋은 밤입니다. Mordoc 님
//좋은 밤입니다. Sophie 님
//================================
//좋은 밤입니다. Eli 님
//좋은 밤입니다. Mordoc 님
//좋은 밤입니다. Sophie 님
//==================================
//좋은 밤입니다. Eli 님
//좋은 밤입니다. Mordoc 님
//좋은 밤입니다. Sophie 님