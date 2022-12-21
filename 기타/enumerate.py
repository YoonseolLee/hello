#https://pearlluck.tistory.com/466
#대부분 for루프를 돌면서 인덱스 변수를 증가시킨다.
#하지만 enumerate() 내장함수를 이용해서 이런 인덱스 변수 없이 반복문을 돌릴 수 있다.

## for 예시
# for <원소> in <목록> -> 목록부분에 넘긴 객체가 담고있는 원소들이 루프가 도는동안 하나씩 차례로 할당이 됨
import enum


for letter in ['a','b','c']:
    print(letter)
    
#또는 리스트의 인덱스와 같이 출력하고 싶다면?
letters = ['a','b','c']
for i in range(len(letters)): # i = 0,1,2
    letter = letters[i] # letter = a,b,c
    print(i,letter) # 0 a / 1 b / 2 c
    
## enumerate 예시
#for <원소> in enumerate <목록>
#기본적인 for문과 같지만, output이 튜플형식으로 리턴됨
#결국 인덱스와 같이 리턴되기 때문에 range(len(리스트)) 를 갖고 수행한 결과와 같다. 
for letter in enumerate(['a','b','c']):
    print(letter)
#튜플형식을 유지하고 싶지 않으면, 아예 range(len(리스트))를 갖고 수행한 결과와 같다.
for i,letter in enumerate(['a','b','c']):
    print(i,letter)
#인덱스를 0이 아닌 1로 시작하고 싶다면, enumerate()의 start인자에 시작하고 싶은 숫자를 넣으면 된다
for i, letter in enumerate(['a','b','c'],start=1):
    print(i,letter)


item = ["first", "second", "third"]
for val in enumerate(item):
    print(val)
for i,val in enumerate(item):
    print(f'{i}번째 값은 {val}입니다')
