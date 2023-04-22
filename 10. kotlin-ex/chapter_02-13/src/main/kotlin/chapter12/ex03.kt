package chapter12

fun main(args: Array<String>) {
    // 주 생성자 호출
    // val player = Player("Hong", 90, true, true)

    // 보조 생성자 호출
    val player2 = Player("Kim")
    player2.castFireball()
    
    println(player2.hometown)  // 최초로 읽어서 초기화 - by lazy lamda 실행 
    println("--------------------------------------------------")
    println(player2.hometown)  // 초기화된 값을 사용
}

// 결과창
// init 초기화 블럭
// 보조 생성자 블럭
// 한 덩어리의 파이어볼이 나타난다. (x2)
// by lazy 호출
// downtown
//--------------------------------------------------
// downtown