package chapter09

fun main() {
    val firstItemSquared = listOf(1, 2, 3).first().let {
        it * it
    }
}

