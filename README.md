# DRF 게시판 만들기

## Users 유효성 검사 전략

serializers에서 User 생성, 로그인 시 유효성 검사를 한다.
view, model 에서도 가능하지만 가독성을 위해 serializers에 작성한다.

## 시리얼라이저의 의의

요청으로 부터 온 데이터를 검증하고 목적에 맞게 사용하기 위함.
하나의 모델을 사용하더라도 게시물 작성, 조회등 목적에 따라 여러 시리얼라이저가 필요하다.

## RegisterView는 CreateAPIView를 사용한다.

Viewset이 필요하지 않은 경우 APIView를 사용하면 된다.
GeneralAPIView 사용 시 사이트에서 request param을 명시해주지 않아 헷갈린다.

## 권한 설정 관련 이슈

게시물 조회/생성 등 에 대한 권한 설정 시 DjangoRestFramework에서 제공하는 Form 이 사라진다… 이슈 원인은 파악했으나 해결 방법은 아직 찾지 못했다.

`permission_classes = [CustomReadOnly]`

## 구글 로그인 관련 설정

- 공식문서만으로는 적용이 힘들어서 블로그 추천

https://dduniverse.tistory.com/entry/Django-django-alluth%EB%A1%9C-%EA%B5%AC%EA%B8%80-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EA%B8%B0%EB%8A%A5-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0


## 권태풍님 자료

[React 게시판](https://github.com/TaeBbong/React-Board)
c6a265d1df7e5f4b1c208391278f99a6af3b18ce