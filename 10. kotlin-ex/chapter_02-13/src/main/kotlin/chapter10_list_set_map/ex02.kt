package chapter10_list_set_map

private  val patronList = mutableListOf<String>("Eli", "Mordoc", "Sophie")

fun main(args: Array<String>) {
    println(patronList)
    // [Eli, Mordoc, Sophie]
    patronList.remove("Eli")
    patronList.add("Alex")          // 마지막에 추가
    patronList.add(0, "Alex")

    println(patronList)
    // [Alex, Mordoc, Sophie, Alex]
}


