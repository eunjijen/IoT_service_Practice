package chapter12

fun main(args: Array<String>) {
    // 주 생성자 호출
    val player = Player("Hong", 90, true, true)

    // 보조 생성자 호출
    val player2 = Player("Kim")
}
// 결과:
// init 초기화 블럭
// init 초기화 블럭
// 보조 생성자 블럭



// 생성자 호출 방법

// Player("Madrigal", 64, true, false)
// Player("Madrigal", true, false)
// Player("Madrigal")