package chapter13

open class Room(val name:String) {  // open을 써야 부모 클래스로 상용 가능 - 상속을 허용
    protected open val dangerLevel = 5   // 멤버 변수 open

    fun description() = "Room: $name\r\n" + "위험 수준: $dangerLevel"

    open fun load() = "아무도 여기에 오지 않았습니다."   // open fun: 오버라이드 허용

}

