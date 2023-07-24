import sys
import os
import openai

## openAI API Key
openai.api_key = "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"

def test_createKORsentance() -> str :
    answer = """1. "우리는 여러 사람을 수용할 수 있는 숙소를 예약해야 합니다." (accommodate)
2. "비즈니스 출장 중에 동행자가 필요합니다." (accompany)
3. "이메일을 수령했음을 알려주세요." (acknowledge)
4. "새로운 기술을 습득해야 합니다." (acquire)
5. "문제를 해결하기 위해 주소를 찾아야 합니다." (address)
6. "그는 그 명예로운 임무를 맡을 수 있을 만큼 부유하다." (afford)
7. "자금을 할당하여 프로젝트를 진행해야 합니다." (allocate)
8. "사용자는 애플리케이션을 분석하여 데이터를 추출할 수 있습니다." (analyze)

"""

    return answer

def createKORsentance() -> str:
    answer = str()

    ## words file Load
    words = open("Words.txt", 'r').read()

    ## gpt Call; system set (First Call)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """
                                accompany
                                acknowledge
                                acquire
                                address
                                afford
                                allocate
                                allow
                                analyze
                                apply
                                assume

                                위와 같이 영단어들이 제공되면, AI는 아래와 같은 형식으로 한국어 문장을 출력합니다.

                                1. “여행 중에 우리를 동행할 가이드가 있을 것입니다.” (accompany)
                                2. “이 편지의 수령을 확인해 주세요.” (acknowledge)
                                3. “그녀는 경매에서 희귀한 골동품을 얻을 수 있었습니다.” (acquire)
                                4. “회사는 직원들이 제기한 우려 사항을 다룰 것입니다.” (address)
                                5. “그는 다가올 여행의 비용을 충당할 수 있어야 합니다.” (afford)
                                6. “위원회는 새 프로젝트를 위해 자금을 할당할 것입니다.” (allocate)
                                7. “규칙은 허가 받은 인원만 제한된 지역에 접근할 수 있도록 허용합니다.” (allow)
                                8. “우리는 데이터를 분석하여 트렌드와 패턴을 파악해야 합니다.” (analyze)
                                9. “그녀는 공부를 후원하기 위해 장학금을 신청하기로 결정했습니다.” (apply)
                                10. “2시에 회의가 진행된다고 가정해 봅시다.” (assume)
                            """
            },
            {
                "role": "user",
                "content": words
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    answer += response.choices[0].message.content



    return answer

def main() :
    print("Processing...")

    korSentances = list(map(str, createKORsentance().split('\n')))

    for i in korSentances :
        print(i)
    print(len((korSentances)))



if (__name__ == "__main__") :
    main()