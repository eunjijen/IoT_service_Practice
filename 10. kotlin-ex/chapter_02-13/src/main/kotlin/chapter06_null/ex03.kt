package chapter06_null

fun main(args: Array<String>) {
    var beverage = readLine()
    if(beverage != null ) {
        beverage = beverage.capitalize()
    } else {
        print("beverage가 null입니다!")
    }
    val beverageServed: String = beverage ?: "맥주"   // null이면 맥주가 String으로 return
    println(beverageServed)
}


// ?.   null 아니면 수신객체를 기반으로 하여 메서드 호출
// ?:   null이면 뒤의 값을 return
// !!   null이 아님을 개발자가 단정