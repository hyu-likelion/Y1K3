# REST, REST API, RESTful


## REST
REST란 *Representational State Transfer*의 약자로, 분산 하이퍼미디어 시스템을 위한 software architecture이다.  
최근의 서버 프로그램은 다양한 브러우저, 모바일 디바이스 등에서도 통신할 수 있어야 한다. 이를 위해 REST가 사용된다.  
- WWW(World Wide Web)과 같이 분산 하이퍼미디어 시스템을 위한 software architecture
  * 분산 하이퍼미디어 : 네트워크를 통해 서버로부터 멀티 미디어 타이틀 또는 멀티미디어 문서를 접근한다.
  > 참고 : 하이퍼미디어란? https://mmlab.snu.ac.kr/~shlee/MMCW/nmm8.htm
- 웹에 존재하는 모든 자원(이미지, 동영상, DB 자원)에 고유한 URI를 부여해 활용하는 것  
- 자원을 정의하고 자원에 대한 주소를 지정하는 방법론
- HTTP URI를 통해 resource을 명시하고, HTTP method를 통해 resource에 대한 CRUD를 적용한다.
  * HTTP method : POST, GET, PUT, DELETE
  * CRUD : Create, Read, Update, Delete
    
### 구성요소
REST는 자원(resource), 행위(verb), 표현(representation of resource)로 구성되어있다.
- 자원(resource) : URI
  - 모든 자원은 고유한 id를 갖고 있고, 이 자원은 서버에 존재한다.
  - 자원을 구별하는 id는 HTTP URI이고, 형식은 /groups/:group_id이다.
  - 클라이언트는 URI을 이용해서 자원을 선택하고, 그 자원 정보를 서버에 요청한다.
- 행위(verb) : HTTP method(POST, GET, PUT, DELETE)
  - HTTP method을 이용해서 CRUD을 적용한다.
  - Create : POST
  - Read : GET
  - Update : PUT
  - Delete : DELETE 
- 표현(representation of resource)

### 특징
- Server-Client 구조
  - 자원이 있는 쪽이 server, 자원을 요청하는 쪽이 client가 된다.
  - server : API을 제공하고, 로직 처리/저장을 책임진다.
  - client : user auth, context 등을 직접 관리하고 책임진다.
  - => 서로에 대한 의존성이 줄어든다.
- stateless
  - HTTP protocol을 이용하므로 stateless의 특성을 가진다.
  - client의 context(세션, 쿠키 등)를 server에 저장하지 않으므로, 구현이 단순해진다.
  - server는 각각의 요청을 완전히 별개의 것으로 인식하고 처리한다. 따라서 Server 처리 방식이 일관적이고, 부담이 줄어들고 서비스 자유도가 높다.
- cacheable
  - 웹 표준 HTTP protocol을 그대로 사용하므로 기존의 인프라를 그대로 활용할 수 있다.
  - 대량의 요청을 효율적으로 처리할 수 있다.
  -  캐시 사용을 통해 응답시간이 빨라지고 server에서 transaction이 발생하지 않기 때문에 전체 응답시간, 성능, 서버 자원 이용률이 높아진다.
- layerd system
  - client는 REST API server만 호출한다.
  - server는 다중 계층으로 구성될 수 있어서, 보안, 로드밸런싱, 암호화, 사용자 인증 등의 구조상에 유연성을 줄 수 있다.
  - 로드밸런싱, 공유 캐시 등을 통해 확장성, 보안성을 향상시킬 수 있다.
  - proxy, gateway와 같은 네트워크 기반의 중간 매체를 사용할 수 있다.
- 일관성있는 interface
  - URI로 지정한 resource에 대한 조직을 통일되고 한정적인 인터페이스로 수행한다.
  - HTTP 표준 프로토콜을 따르는 모든 플랫폼에서 사용이 가능하다. 즉, 특정 언어나 기술에 종속되지 않는다.

### 장단점
- 장점
  * 사용이 쉽다. : 별도의 인프라를 구축할 필요 없이 HTTP protocol infra을 그대로 이용할 수 있다.
  * HTTP protocol의 표준을 최대한 활용한다. : HTTP 표준 프로토콜을 따르는 모든 플랫폼에서 사용이 가능하다.
  * client / server 역할이 명확히 분리되어있다.
  * REST API 메시지가 의도하는 바가 명확하다. : REST API는 헤더부분에 URI 처리 메소드를 명시하고, 필요한 실제 데이터는 바디부분에 표현한다.
    
- 단점
  * 표준이 존재하지 않는다.
  * 사용할 수 있는 메소드가 4개 밖에 없다.(POST, GET, PUT, DELETE)
    
---
## REST API
REST를 기반으로 하여 서비스 API를 구현한 것이다.   
최근 open API나 마이크로서비스 등을 제공하는 업체는 대부분 REST API를 제공한다. (예 :카카오, 네이버, 구글맵, 공공데이터 포털 
 등)

### 특징
- REST 기반으로 시스템을 분산해서 확장성과 재사용성을 높일 수 있다. 이로 인해 유지보수와 운용이 편해진다.
- HTTP 표준을 기반으로 하므로, HTTP를 지원하는 언어로 클라이언트, 서버를 구현할 수 있다. 폭이 넓은 셈이다.
- REST API를 제작하면 델파이 클라이언트 뿐 아니라, 자바, C#, web 등을 이용해 클라이언트를 제작할 수 있다.
- 슬래시(/)을 통해 계층 관계를 나타낸다.

---
## RESTful
REST의 형식을 따르는 시스템을 RESTful이라 한다. 일반적으로 REST architecture을 구현하는 웹서비스를 나타내기 위해 사용된다.  
RESTful은 이해하기 쉽고, 사용하기 쉬운 REST API를 만드는 것으로, 성능 향상이 주된 목적이 아니라 인관적인 컨벤션을 통해서 API의 이해도, 호환성을 높이는 것이 주 목적이다.
따라서 성능이 중요한 상황에서는 RESTful API가 추천되지는 않는다.  
CRUD 기능을 모두 POST로 처리하는 경우, 혹은 route에 resource, id 외의 정보가 들어가는 경우는 RESTful하지 않다.