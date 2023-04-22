package chapter07_String

const val TAVERN_NAME2 = "Taernly's Folly"

fun main(args: Array<String>) {
    placeOrder("shandy,Dragon's Breath,5.91")
}

private fun placeOrder(menuData: String) {
    val indexofApostrophe = TAVERN_NAME2.indexOf('\'')
    val tarvernMaster = TAVERN_NAME2.substring(0 until indexofApostrophe)

    println("마드리갈은 $tarvernMaster 에게 주문한다.")

//    val data = menuData.split(',')  // List<String> 리턴 객체
//    val type = data[0]
//    val name = data[1]
//    val price = data[2]

    // 부분 문자열 추출
    val (type, name, price)= menuData.split(',')   // 해체 선언 - 한줄로 작성 가능
    val message = "마드리드갈은 금화 $price 로 $name ($type)를 구입한다."
    println(message)
}

// 마드리갈은 Taernly 에게 주문한다.
// 마드리드갈은 금화 5.91 로 Dragon's Breath (shandy)를 구입한다.