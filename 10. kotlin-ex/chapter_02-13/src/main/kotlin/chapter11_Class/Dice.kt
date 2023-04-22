package chapter11_Class

class Dice {
    val rolledValue
        get() = (1..6).shuffled().first()

}