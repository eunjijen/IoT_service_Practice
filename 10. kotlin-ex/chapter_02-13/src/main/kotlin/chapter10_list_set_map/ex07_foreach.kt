package chapter10_list_set_map

fun main() {
    val map = mutableMapOf<String, Double>(
        Pair("Eli", 10.5),      // double 값
        Pair("Sophie", 5.5)    // key와 value
    )

    map += "Sophie" to 6.0

    // map 순회
    map.forEach{key, value ->
        println("Key: $key, Value: $value")
    }
}

// Key: Eli, Value: 10.5
// Key: Sophie, Value: 6.0