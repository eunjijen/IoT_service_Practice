package chapter12

fun main(args: Array<String>) {
    val player = Player("Madrigal", 89, true, false)
    // 기본 생성자 호출
    // 디폴트 생성자가 자동으로 안 만들어져 - 이미 하나 만들어서
    
    println(player.name)
    println(player.healthPoints)
    println(player.isBlessed)
    // println(player.isImmortal)   // private이라서 접근 불가
}

