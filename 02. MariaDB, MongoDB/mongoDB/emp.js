use mydb
var empArr=[
        {
                "empno" : 7499,
                "ename" : "ALLEN",
                "job" : "SALESMAN",
                "mgr" : 7698,
                "hiredate" : "1981-02-20",
                "sal" : 1600.00,
                "comm" : 300.00,
                "deptno" : 30
        },
        {
                "empno" : 7521,
                "ename" : "WARD",
                "job" : "SALESMAN",
                "mgr" : 7698,
                "hiredate" : "1981-02-22",
                "sal" : 1250.00,
                "comm" : 500.00,
                "deptno" : 30
        },
        {
                "empno" : 7654,
                "ename" : "MARTIN",
                "job" : "SALESMAN",
                "mgr" : 7698,
                "hiredate" : "1981-09-28",
                "sal" : 1250.00,
                "comm" : 1400.00,
                "deptno" : 30
        },
        {
                "empno" : 7844,
                "ename" : "TURNER",
                "job" : "SALESMAN",
                "mgr" : 7698,
                "hiredate" : "1981-09-08",
                "sal" : 1500.00,
                "comm" : 0.00,
                "deptno" : 30
              },

{"empno":7369, "ename":"SMITH","job":"CLERK",mgr:7902,"hiredate" : "1980-12-17","sal":800.0, "comm" : 0.00,"deptno":20},
{"empno":7566, "ename":"JONES","job":"MANAGER",mgr:7839,"hiredate" : "1981-04-02","sal":2975.0, "comm" : 0.00,"deptno":20.0},
{"empno":7782,"ename":"CLARK","job":"MANAGER",mgr:7839,"hiredate" : "1981-09-08","sal":2450.0, "comm" : 0.00,"deptno":10.0},
{"empno":7934,"ename":"MILLER","job":"CLERK",mgr:7782,"hiredate" : "1981-09-08","sal":1300.0, "comm" : 0.00,"deptno":10.0},
{"empno":7788,"ename":"SCOTT","job":"ANALYST",mgr:7566,"hiredate" : "1982-12-09","sal":3000.0, "comm" : 0.00,"deptno":10.0},
{"empno":7839,"ename":"KING","job":"PRESIDENT","hiredate" : "1981-11-17","sal":5000.0, "comm" : 0.00,"deptno":10.0},
{"empno":7876,"ename":"ADAMS","job":"CLERK",mgr:7788,"hiredate" : "1983-01-12","sal":1100.0, "comm" : 0.00,"deptno":20.0},
{"empno":7902,"ename":"FORD","job":"ANALYST",mgr:7566,"hiredate" : "1981-12-03","sal":3000.0, "comm" : 0.00,"deptno":20.0},
{"empno":7934,"ename":"MILLER","job":"CLERK",mgr:7782,"hiredate" : "1982-01-23","sal":1300.0, "comm" : 0.00,"deptno":10.0}
]
db.emp.insertMany(empArr)

var deptArr=[{
                "deptno" : 10,
                "dname" : "ACCOUNTING",
                "loc" : "NEW YORK"
        },
        {
                "deptno" : 20,
                "dname" : "RESEARCH",
                "loc" : "DALLAS"
        },
        {
                "deptno" : 30,
                "dname" : "SALES",
                "loc" : "CHICAGO"
        },
        {
                "deptno" : 40,
                "dname" : "OPERATIONS",
                "loc" : "BOSTON"
        }
  ]
db.dept.insertMany(deptArr)

db.emp.find()