package chapter10_list_set_map

import chapter11_Class.Player

fun main(args: Array<String>) {
    val player = Player()     // 객체 생성   var이면 player2 생성 가능

    println(player.name)     // mardrigal    name의 get 함수 호출
    player.castFireball()
    // 한 덩어리의 파이어볼이 나타난다. (x2)

    player.name = "gagamel"      // name의 set()함수 호출
    println(player.name)     // gagamel   name의 get()함수 호출
}
