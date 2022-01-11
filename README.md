# Opensea floor price check
## Description
- 디스코드 봇 명령어를 통해 바닥가 정보 수집
  - Opensea API를 활용하여 원하는 프로젝트 바닥가 측정
  - 빗썸 오픈 API를 통하여 "ETH/KLAY - KRW" 실시간 시세 반영

## Installation
1. 레포지토리 클론  
```git clone https://github.com/pYsson/Opensea-floor-price-Check.git```
2. 필요한 라이브러리 설치  
```pip install -r requirements.txt```
3. 디스코드 봇 [TOKEN](https://discord.com/developers/docs/intro) 발급

## How to run your Bot
1. floorcheck.py 파일 실행  
```python3 floorcheck.py``` or ```python floorcheck.py```  

    1-1. floorcheck.py 파일 내 디스코드 봇 토큰 입력  
2. 봇 토큰 입력  
- 서버 내 백그라운드 실행하고 싶은 경우 (봇 토큰 미리 입력 필수)  
```nohup python3 floorcheck.py &``` or ```nohup python floorcheck.py &```

## Command
- !floor 프로젝트명  
ex) ```!floor metakongz```  
<img width="381" alt="floorcheck" src="https://user-images.githubusercontent.com/97378861/148893847-4382861b-6b0e-4d58-a049-de159cd981e1.png">

## Site List
- opensea.json 파일을 참고
- 현재 기본으로 등록된 리스트
> metakongz   =>    [THE META KONGZ](https://opensea.io/collection/the-meta-kongz)  
> eleckongz   =>    [ElectroPixelKongz](https://opensea.io/collection/electropixelkongz)  
> cyberthug   =>    [CyberTHUG V2](https://opensea.io/collection/cyberthug-v2)  
> spoon       =>    [Project Spoon DAO](https://opensea.io/collection/project-spoon-dao)  
> k3k         =>    [Klay 3 Kingdoms](https://opensea.io/collection/klay-3-kingdoms)  
> metacat     =>    [META CATS V1](https://opensea.io/collection/meta-cats-v1)  
