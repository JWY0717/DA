# GC 분석을 위한 데이터 분석 및 과정

- 목적 :  여러 선박 종류들 중에서 2가지로 한정(어선, 화물선, 여객선 등), 선박의 크기(가로, 세로) 한정 하여AIS 및 해양기상데이터를 학습하여 전송 구간 사이에 최적의   선박위치를 웹서비스로 표출  

## 실행방법

- 
-

### 서버
-
-

### 데이터 분석

```bash
- python 3.10.10 버전
- pip numpy
- pip pandas
- pip seaborn
- pip tensorflow
- train_test_splitfrom sklearn.model_selection,
- MinMaxScalerfrom sklearn.preprocessing, 
- Sequentialand Densefrom tensorflow.keras.layers, 
```


### 프로젝트 실행 시 주의사항
-
-

#

## 진행상황

## Week2
- 데이터 형식 : excel 파일
- 데이터 구조 : 1. 해양기상_통계자료_신항유도등
               2. GC (AIS데이터) 

- 독립변수 : 풍향,유향,기온,풍속,유속,기압,습도(기상청 데이터),  mmis(Ais데이터)  
- 종속변수 : 예측하고자 하는 대상 => 선박의 위치(위도, 경도)

## Week3
- 기상청 데이터와 AIS데이터를 시간을 기준으로 merge하기 

## ToDo
-  각 팀별 전처리된 데이터는 플라토에 업로드 하기
-  폴더 및 파이썬 스크립트,노트북 파일 정리해서 github.
-  README.md 파일 작성 


- 1. 조별 게시판에 데이터를 업로드 하기 (각 조별 플라토 게시판)
- 2. 반드시 플라스크가 돌아가도록 개선해서 올려두기
- 3. README.md 파일 적어서 다른 분들이 실행 가능하도록 합시다.
