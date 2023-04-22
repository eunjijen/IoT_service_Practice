package chapter07_String

const val TAVERN_NAME = "Taernly's Folly"
fun main(args: Array<String>) {
    placeOrder()
}

private fun placeOrder() {
    val indexofApostrophe = TAVERN_NAME.indexOf('\'')  // indexofApostrophe는 int
    val tarvernMaster = TAVERN_NAME.substring(0 until indexofApostrophe)
    // until로 범위 지정, 상한값 포함 X
    // 0 .. (indexofApostrophe-1)
    println("마드리갈은 $tarvernMaster 에게 주문한다.")
}
 // 마드리갈은 Taernly 에게 주문한다.