package chapter12

class Player (
    _name: String,      // 주생성자(기본 생성자)에 속성 정의 : 제일 먼저 초기화됨
    var healthPoints: Int = 100,    // 기본 인자 배정
    var isBlessed: Boolean,
    private val isImmortal: Boolean) {
    // 2번째 호출
    var name = _name   // 주생성자에서만 적용되는 규칙 - var, val이 멤버변수가 돼
        get() = field.capitalize()
        set(value) {
            field = value.trim()
        }

    // 1. 보조 생성자 호출 - constructor 사용 / 보조 생성자 호출 안하면 실행 X
    constructor(name:String) :this(name,    // this는 주생성자, 2. 주생성자 호출(필수)
                            // healthPoints = 100,    // if문 들어오기 전의 값은 100
                            isBlessed = true,
                            isImmortal = false) {
        println("보조 생성자 블럭")
        if(name.toLowerCase() == "kar") healthPoints = 45  // 3. 속성 초기화 추가 / 4번째 초기화(옵션)
        // toLowerCase - 소문자로 변경할 때 쓰이는 메소드
    }

    init {  // 주 생성자 호출 이후에 실행 / 3번째로 초기화
        println("init 초기화 블럭")
        require(healthPoints > 0, {"healthPoints는 0보다 커야 합니다."})
        require(name.isNotBlank(), {"플레이어는 이름이 있어야 합니다."})
    }

    // val hometown: String? = null   // null 허용하고 null을 배정 (?) 사용 / 나머지 코드에서 사용할 때마다 null 검사해야돼
    val hometown by lazy {   // type String 생략 가능
        println("by lazy 호출")
        "downtown"    // lamda의 return이 문자열
    }

    fun castFireball(numFireballs: Int = 2) =
        println("한 덩어리의 파이어볼이 나타난다. (x$numFireballs)")
}