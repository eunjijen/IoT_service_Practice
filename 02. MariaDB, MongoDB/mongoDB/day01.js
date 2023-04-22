use mydb;

db.memo.find();
//F6 : 현재 커서를 실행
//F5 : 파일 전체를 실행
show collections;

db.createCollection('mycol',{capped:true,size:10000})
//capped:true => 제한된 공간에서만 데이터를 저장하겠다는 설정
//저장공간이 차면 오랜된 데이터는 지운다.

db.mycol.stats()
//maxSize: 10240 설정되어 있음

for(i=0;i<1000;i+=1){
    db.mycol.insertOne({x:i})}

db.mycol.find();
db.mycol.find().count();
//처음에 삽입된 데이터가 사라진것 확인


