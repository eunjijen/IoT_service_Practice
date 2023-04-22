package chapter11_Class

class Player {
    var name = "mardrigal"      // val로 하면 name을 바꿀수 없어 / set을 쓸 수 없음 제할당x
        get() = field.capitalize()     // 변수 선언 바로 다음에 get, set을 정의해야 돼
        set(value) {                // name을 val로 하면 get밖에 못써  1개
            field = value.trim()
        }

    // 변수 정의해주려면 무조건 초기화 해야돼  - 안하면 오류

    fun castFireball(numFireballs: Int = 2) =
        println("한 덩어리의 파이어볼이 나타난다. (x$numFireballs)")

}