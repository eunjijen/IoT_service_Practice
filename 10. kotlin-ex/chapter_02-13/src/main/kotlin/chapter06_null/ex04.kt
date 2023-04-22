package chapter06_null

fun main(args: Array<String>) {
    var test: String? = "hello";    // null을 허용하는 타입이기 때문에 그냥은 못씀
    print(test?.capitalize())    // ?를 같이 써줘야 함

    //print(test.capitalize())  // 에러
}