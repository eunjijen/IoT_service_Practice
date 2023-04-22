package chapter13

// 자식 클래스 정의 (class 자식 클래스: 부모 클래스())
class TownSquare : Room("Town Square") {
    override val dangerLevel = super.dangerLevel - 3   // val도 재정의 가능
    private val bellSound = "댕댕"

    final override fun load() = "당신의 참여를 주민들이 다 함께 환영합니다!\r\n" + ringBell()
    // final: 더 이상 override를 못하게 함

    private fun ringBell() = "당신의 도착을 종탑에서 알립니다. $bellSound"
}

// 부모 클래스의 생성자 호출, 매개변수가 없으면 디폴트 생성자 호출
