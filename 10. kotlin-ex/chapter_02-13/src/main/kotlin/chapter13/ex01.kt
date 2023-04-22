package chapter13

fun printRoomInfo(room: Room) {  // 부모의 클래스 타입으로 자식을 운영 가능
    println(room.description())    // open 사용하지 않음
    println(room.load())   // open으로 오버라이드 허용
}

fun main(args: Array<String>) {
    var currentRoom:Room = Room("Foyer")
    // currentRoom의 타입은 --> Room class 타입
    printRoomInfo(currentRoom)
    // println(currentRoom.description())
    // println(currentRoom.load())

    var room:TownSquare = TownSquare()
    // room의 타입 --> TownSquare class
    printRoomInfo(room)
    // println(room.description())    // open 사용하지 않음
    // println(room.load())   // open으로 오버라이드 허용

}

// Room: Foyer
// 위험 수준: 5
// 아무도 여기에 오지 않았습니다.
// Room: Town Square
// 위험 수준: 2
// 당신의 참여를 주민들이 다 함께 환영합니다!
// 당신의 도착을 종탑에서 알립니다. 댕댕
