# 기초

## Numbers

- division operator(/) 는 항상 소수점을 출력한다.
  - 정수형으로 출력하려면 floor division 사용

```python
>> 11 / 4
 2.75
>> 11 // 4
 2
```

- `**` operator

  - 승수

- 혼합 연산자 & 부동소수점
  - 연산자에 피연산의 자료형의 타입이 정수형이 아닌 실수형과 혼합되어 있을때 정수형 타입인 피연산자를 실수형 타입으로 변환한다.

```python
>> 4 * 3.75 - 1
1.5
```

## String

- \가 붙은 문자를 특수 문자로 해석하지 않기
  - 첫 번째 따옴표 앞에 r을 추가하여 원시 문자열을 사용

```python
>> print('hello\nworld') # \n means newline!
hello
world
>> print(r'hello\nworld') # r before the quote
hello\nworld
```

- 두개의 이상의 문자열 사이에 공백시 자동연결
  - 문자열 리터럴에서만 작용! 표현식이나 변수에는 적용하지 않는다.
  - 변수와 리터럴을 결합하고 싶을 때는 `+`연산자로 연결한다!

```python
>> 'hello ' 'world'
hello world
```
