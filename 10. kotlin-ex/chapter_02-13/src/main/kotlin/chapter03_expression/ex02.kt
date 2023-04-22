package chapter03_expression
// 간소화, 범위 지정
fun main(args: Array<String>) {
    val name = "마드리길 "
    var healthPoints = 89
    val isBlessed = true
    val isImmortal = false

    // 아우라
    val auraVisible = isBlessed && healthPoints > 50 || isImmortal
    val auraColor = if(auraVisible) "GREEN" else "NONE"  // if에 의해 값이 하나 결정됨
    // 조건식 if가 참이면 GREEN 거짓이면 NONE (조건식으로 쓰면 else가 무조건 있어야돼)
    println(auraColor)

    val healthStatus = if(healthPoints == 100) "최상의 상태임!"
        else if (healthPoints in 90..99) "약간의 찰과상만 있음."
        else if (healthPoints in 75..89)
            if (isBlessed) "경미한 상처가 있지만 빨리 치유됨!"
            else "경미한 상처만 있음"
        else if (healthPoints in 15..74) "많이 다친 것 같음"
        else "최악의 상태임!"

    // 플레이어의 상태 출력
    println(name + " " + healthStatus)
}