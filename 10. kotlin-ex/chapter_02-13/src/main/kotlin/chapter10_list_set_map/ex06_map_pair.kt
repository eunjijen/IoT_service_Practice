package chapter10_list_set_map

fun main() {
    val map = mutableMapOf<String, Double> (
        Pair("Eli", 10.5),      // double 값
        Pair("Sophie", 5.5)    // key와 value
    )

    map += "Sophie" to 6.0
    println(map)
    // {Eli=10.5, Sophie=6.0}

    // println(map["Sophie"].toInt())   // 에러  null일 수도 있어서
//    println(map["Sophie"]?.toInt())
}

