package chapter04_func

private fun fromHealthStatus (healthPoints: Int, isBlessed: Boolean) =
    when (healthPoints) {  // when 표현식
        100 -> "최상의 상태임!"
        in 90..99 -> "약간의 찰과상만 있음"
        in 75..89 -> if (isBlessed) "경미한 상처가 있지만 빨리 치유됨!"
        else "경미한 상처만 있음"
        in 15..74 -> "많이 다친 것 같음"
        else -> "최악의 상태임!"
    }


private fun auraColor(isBlessed: Boolean, healthPoints: Int,
                      isImmortal: Boolean): String {
    val auraVisible = isBlessed && healthPoints > 50 || isImmortal
    val auraColor = if (auraVisible) "GREEN" else "NONE"

    return auraColor
}

private fun printPlayerStatus(auraColor: String, isBlessed: Boolean,
                              name: String, healthStatus: String) {
    println(
        "(Aura: $auraColor)" +
        "(Blessed: ${if (isBlessed) "YES" else "NO"})"  // 표현식 else 필수
    )
    println("$name $healthStatus")
}

private fun castFireball(numFireballs: Int = 2) =  // 디폴트 값을 줄 수 있음
    println("한 덩어리의 파이어볼이 나타난다. (x$numFireballs)")  // 변수의 값을 출력하라 $: 단일변수
    // 단일변수가 아니면 ${표현식}


fun performCombat() = println("적군이 없다!")

fun performCombat (enemyName: String) = println("$enemyName 과 전투를 시작함.")

fun performCombat(enemyName: String, isBlessed: Boolean) =
    if(isBlessed) {
        println("$enemyName 과 전투를 시작함. 축복을 받음.")
    } else {
        println("$enemyName 과 전투를 시작함.")  // $변수명이랑 붙어서 문자열을 표기하면 오류
    }


// main 함수에 logic이 나오면 안돼 logic은 다 func으로 만들어--> 깔끔
fun main(args: Array<String>) {
    val name = "마드리길 "
    var healthPoints = 89
    val isBlessed = true
    val isImmortal = false

    // 아우라
    val auraColor = auraColor(isBlessed, healthPoints, isImmortal)
    val healthStatus = fromHealthStatus(healthPoints, isBlessed)
    // 플레이어의 상태 출력
    printPlayerStatus(auraColor, isBlessed, name, healthStatus)
    castFireball(5)
}

